# AutoSpeechRecord

## Summary

 * 사용자가 발화를 시작하는 지점과 끝내는 지점을 인식하여 발화를 녹음하고, openai의 Auto Speech Recognition 모델인 `whisper-large-v3`를 사용해 녹음된 발화를 인식하여 문자열로 반환하는 일련의 과정을 자동화한 도구입니다. 
 * Windows에서 CUDA를 통한 GPU 추론, CPU 추론을 지원합니다.

## Setup Environment(Windows)

 1. git을 clone합니다.
    
    ```bash
    git clone https://github.com/dltmdwoOS/AutoSpeechRecord
    ```
 2. 파이썬 가상환경을 생성합니다.(Anaconda 환경을 가정합니다.)
    ```bash
    conda create -n py311 python=3.11
    conda activate py311
    ```
 3. [PyTorch](https://pytorch.org/get-started/locally/)를 설치합니다.
 4. 프로젝트 종속성을 설치합니다.
    ```bash
    pip install -r requirements.txt
    ```

## How to use(jupyter notebook)

1. `AutoSpeechRecord.py`를 import합니다.
  ```python
  import AutoSpeechRecord
  ```
2. 객체 `auto_speech_record`를 생성합니다.
  ```python
  recorder = AutoSpeechRecord.auto_speech_recorder()
  ``` 
3. 메소드 `auto_speech_record()`를 사용합니다.
  ```python
  recoder.auto_speech_record()
  ```
  * 참조 : [Example.ipynb](https://github.com/dltmdwoOS/AutoSpeechRecord/blob/main/example.ipynb)

## License

  * Apache License 2.0

## Contact

  * Email : coex03@cau.ac.kr
