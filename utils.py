import os
import wave
import pyaudio
import datetime

def mkdir_unless_exist(folder_name):
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

def find(folder_path, file_name):
    mkdir_unless_exist(folder_path)
    file_list = os.listdir(folder_path)
    if file_name in file_list:
        return True
    else:
        return False
    
def remove_all_files(folder_path):
    '''
    remove all files in folder
    '''
    file_list = os.listdir(folder_path)
    for file_name in file_list:
        file_path = os.path.join(folder_path, file_name)
        if os.path.isfile(file_path):
            os.remove(file_path)

def save_wave_segment(frames, segment_folder, segment_base, format, channels, rate):
    '''
    save wavfile
    '''

    mkdir_unless_exist(segment_folder)
    
    output_path = os.path.join(segment_folder, f"{segment_base}_{len(os.listdir(segment_folder)) + 1}.wav")

    wf = wave.open(output_path, 'wb')
    wf.setnchannels(channels)
    wf.setsampwidth(pyaudio.PyAudio().get_sample_size(format))
    wf.setframerate(rate)
    wf.writeframes(b''.join(frames))
    wf.close()
    return output_path

def save_recognized_text(text, log_folder, log_name):
    mkdir_unless_exist(log_folder)

    output_path = os.path.join(log_folder, f"{log_name}.txt")

    f = open(output_path,'a', encoding='UTF-8')
    f.write(str(datetime.datetime.now()) + " | " + text+'\n')
    f.close()
   