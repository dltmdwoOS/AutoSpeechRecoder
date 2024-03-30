# AutoSpeechRecord

## Summary

 * A tool that automates a series of processes that records a user's speech and recognizes the speech using `whisper-large-v3`, open-ai's Automatic Speech Recognition model.
 * Supports GPU inference through CUDA on Windows
 * Also supports CPU inference at slow speed on Windows

## Setup Environment(Windows)

 1. clone project.

    ```bash
    git clone https://github.com/dltmdwoOS/AutoSpeechRecord
    ```
 
 2. Create a Python virtual environment(assuming Anaconda environment)

    ```bash
    conda create -n py311 python=3.11
    conda activate py311
    ```
 
 3. Install [PyTorch](https://pytorch.org/get-started/locally/).
 4. Install project dependencies.

    ```bash
    pip install -r requirements.txt
    ```

## How to use(jupyter notebook)

1. Import `AutoSpeechRecord.py`.
  
  ```python
  import AutoSpeechRecord
  ```

2. Construct an `auto_speech_record` object.
  
  ```python
  recorder = AutoSpeechRecord.auto_speech_record()
  ``` 

3. Use `auto_speech_record()` method.
  
  ```python
  recoder.auto_speech_record()
  ```
  
  * Reference : [Example.ipynb](https://github.com/dltmdwoOS/AutoSpeechRecord/blob/main/example.ipynb)

## License

  * Apache License 2.0

## Contact

  * Email : coex03@cau.ac.kr
