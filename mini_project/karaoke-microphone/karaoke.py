import pyaudio # brew install portaudio, pip install pyaudio
import numpy as np
import wave, os
from datetime import datetime
from audioop import mul, add, bias

INPUT_INDEX = 1 # change this to microphone
OUTPUT_INDEX = 6 # change this to main speaker
# 입력된 음성을 저장
OUTPUT_FILENAME = 'output/%s.wav' % (datetime.now().strftime('%Y-%m-%d_%H-%M-%S'))
os.makedirs('output', exist_ok=True)

# 스트리밍의 양(적을 수록 딜레이 적음)
CHUNK = 512
RATE = 48000
SAMPLE_WIDTH = 2
# 에코 딜레이
DELAY_INTERVAL = 15
DELAY_VOLUME_DECAY = 0.6
# 딜레이 반복
DELAY_N = 10

# delay sound
original_frames = []
index = 0

def add_delay(input):
    global original_frames, index

    # 원본 저장
    original_frames.append(input)
    output = input

    if len(original_frames) > DELAY_INTERVAL:
        for n_repeat in range(DELAY_N):
            # 딜레이 제작
            delay = original_frames[max(index - n_repeat * DELAY_INTERVAL, 0)]

            # 딜레이의 볼륨이 반복마다 작아지게
            delay = mul(delay, SAMPLE_WIDTH, DELAY_VOLUME_DECAY ** (n_repeat + 1))
            # 작업한 소리들 합성
            output = add(output, delay, SAMPLE_WIDTH)

        index += 1

    return output

def start_stream():
    # open devices
    # 인풋과 아웃풋 설정
    stream = pa.open(
        format=pyaudio.paInt16,
        channels=1,
        rate=RATE,
        frames_per_buffer=CHUNK,
        input=True,
        output=True,
        input_device_index=INPUT_INDEX,
        output_device_index=OUTPUT_INDEX
    )

    frames = []

    # start stream
    while stream.is_active():
        try:
            # 저장된 음성을 읽어온다
            input = stream.read(CHUNK, exception_on_overflow=False)
            # 음성 변조 적용
            input = add_delay(input)

            # 결과를 스피커에 출력
            stream.write(input)
            # 목소리 저장
            frames.append(input)  
            # crtl c 입력시 프로그램 종료
        except KeyboardInterrupt:
            break
        except Exception as e:
            print('[!] Unknown error!', e)
            exit()

    # write audio as a file
    # 변조된 목소리 저장
    total_frames = b''.join(frames)
 
    with wave.open(OUTPUT_FILENAME, 'wb') as f:
        f.setnchannels(1)
        f.setsampwidth(pa.get_sample_size(pyaudio.paInt16))
        f.setframerate(RATE)
        f.writeframes(total_frames)
        
    stream.stop_stream()
    stream.close()
    pa.terminate()

# main
pa = pyaudio.PyAudio()

# 디바이스 정보 출력
for i in range(pa.get_device_count()):
    print(pa.get_device_info_by_index(i))

start_stream()
