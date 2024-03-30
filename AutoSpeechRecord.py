import numpy as np
import pyaudio
from torch.cuda import is_available
from torch import float16, float32
from transformers import AutoModelForSpeechSeq2Seq, AutoProcessor, pipeline
import utils

CUDA_device = "cuda:0" if is_available() else "cpu"
torch_dtype = float16 if is_available() else float32
model_path = "cache/models--openai--whisper-large-v3/snapshots/1ecca609f9a5ae2cd97a576a9725bc714c022a93"
model_name = "openai/whisper-large-v3"

class auto_speech_record():
    def __init__(self, segment_folder="output_segment", segment_base="segment", log_folder="log", log_name="recognized_text_log"):
        self.processor = AutoProcessor.from_pretrained(model_path, local_files_only=True) if utils.find(model_path, "preprocessor_config.json") else AutoProcessor.from_pretrained(model_name, cache_dir="cache")
        self.model = AutoModelForSpeechSeq2Seq.from_pretrained(model_path, torch_dtype=torch_dtype, local_files_only=True).to(CUDA_device) if utils.find(model_path, "config.json") else AutoModelForSpeechSeq2Seq.from_pretrained(model_name, torch_dtype=torch_dtype, cache_dir="cache").to(CUDA_device)
        self.pipeline = pipeline(
            "automatic-speech-recognition",
            model=self.model,
            tokenizer=self.processor.tokenizer,
            feature_extractor=self.processor.feature_extractor,
            max_new_tokens=128,
            chunk_length_s=30,
            batch_size=16,
            return_timestamps=True,
            torch_dtype=torch_dtype,
            device=CUDA_device,
        )
        
        self.segment_folder = segment_folder
        self.segment_base = segment_base
        self.log_folder = log_folder
        self.log_name = log_name
        
    def record(self, silence_limit=1.0, record_limit=0.03, threshold=400, format=pyaudio.paInt16, channels=1, rate=44100, chunk=1024):
        p = pyaudio.PyAudio()

        stream = p.open(format=format,
                        channels=channels,
                        rate=rate,
                        input=True,
                        frames_per_buffer=chunk)
        
        path = None
        frames = []
        silence_counter = 0
        record_counter = 0
        record = False
        
        while True:
            data = stream.read(chunk)
            audio_data = np.frombuffer(data, dtype=np.int16)
        
            # 볼륨 변수
            # Volume variable
            vol = np.max(np.abs(audio_data))
            
            if record:
                is_silent = vol < threshold
        
                if is_silent:
                    silence_counter += 1
                else:
                    silence_counter = 0
        
                frames.append(data)

                # 일정 시간 이상의 공백이 감지되면 파일로 저장
                # Save as a file when a space is detected for more than a certain amount of time
                if silence_counter > int(silence_limit * rate / chunk):
                    path = utils.save_wave_segment(frames, segment_folder=self.segment_folder , segment_base=self.segment_base, format=format, channels=channels, rate=rate)
                    break
            else:
                # 일정 음량 이상일 때부터 녹음 시작
                # Start recording when the volume is above a certain level
                if record_counter > int(record_limit * rate / chunk):
                    record = True
                
                if vol > threshold:
                    record_counter += 1
                else:
                    record_counter = 0

        stream.stop_stream()
        stream.close()
        p.terminate()
        return path
    
    def audio_recognition(self, path):
        output = self.pipeline(path, generate_kwargs={"language": "korean"})
        text = output["text"][1:]
        utils.save_recognized_text(text, log_folder=self.log_folder, log_name=self.log_name)
        return text

    def auto_speech_record(self, silence_limit=1.0, record_limit=0.03, threshold=400, format=pyaudio.paInt16, channels=1, rate=44100, chunk=1024):
        path = self.record(silence_limit, record_limit, threshold, format, channels, rate, chunk)
        return self.audio_recognition(path)

