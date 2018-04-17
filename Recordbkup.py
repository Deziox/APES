from sys import byteorder
from array import array
from struct import pack
import pyaudio
import wave
import time
import math
import sys
import queue

CHUNKS = 1024
FORMAT = pyaudio.paInt16
RATE = 44100 # or less so my laptop can keep running
THRESH = 500
STEREO = False

def negInf(data):
    return max(data)< THRESH


def normalize(data,MAX = 16384):
    x = float(MAX)/max(abs(i) for i in data)

    ret = array('h')
    for i in data:
        ret.append(int(i*x))
    return ret


def setChannels(c):
    if c >= 2:
        STEREO = True
        return
    STEREO = False


def trim(data):
    def _trim(data):
        started = False
        ret = array('h')

        for i in data:
            if not started and abs(i)>THRESH:
                started = True
                ret.append(i)
            elif started:
                ret.append(i)
        return ret

    data = _trim(data)
    data.reverse()
    data = _trim(data)
    data.reverse()
    return data


def add_silence(snd_data, seconds):
    "Add silence to the start and end of 'snd_data' of length 'seconds' (float)"
    r = array('h', [0 for i in range(int(seconds*RATE))])
    r.extend(snd_data)
    r.extend([0 for i in range(int(seconds*RATE))])
    return r


def record():
    p = pyaudio.PyAudio()
    stream = p.open(format=FORMAT,channels=(2 if STEREO else 1),rate=RATE,input=True,output=True,
                    frames_per_buffer=CHUNKS)
    num_silent = 0
    started = False
    ret = array('h')
    x = 0
    while True:
        # little endian signed
        data = array('h',stream.read(CHUNKS))
        # data2 = data
        # data2 = array('h',map(int,str(int.from_bytes(bytes(data),byteorder='big',signed=False))))
        # data = data2
        print(x,data)
        if byteorder == 'big':
            data.byteswap()
        ret.extend(data)
        silent = negInf(data)
        if silent and started:
            num_silent += 1
        elif not silent and not started:
            started = True
        x += 1
        if (started and num_silent>30) or x > 650:
            break
        # if x > 650:
        #   break

    sample_width = p.get_sample_size(FORMAT)
    stream.stop_stream()
    stream.close()
    p.terminate()

    ret = normalize(ret)
    ret = trim(ret)
    ret = add_silence(ret,0.5)
    return sample_width,ret


def record_to_file(q,path="C://"):
    sample_width,data = record()
    raw = data
    S = sample_width
    data = pack('<' + ('h'*len(data)),*data)
    D = data
    print(S,D)
    with wave.open(path,'wb') as wf:
        # wf = wave.open(path,'wb')
        wf.setnchannels((2 if STEREO else 1))
        wf.setsampwidth(sample_width)
        wf.setframerate(RATE)
        wf.writeframes(data)
        wf.close()
    f = open("C:/Users/yetski/Music/Recordings/Raw.txt", "w+")
    print(raw)
    for i in raw:
        f.write(str(i) + "\n")
    f.close()
    return S,D,raw

def test_to_file(S,D,raw,path="C://"):
    # sample_width,data = S,D
    sample_width = S
    data = pack('<' + ('h'*len(raw)),*raw)
    print(data)
    with wave.open(path,'wb') as wf:
        wf.setnchannels((2 if STEREO else 1))
        wf.setsampwidth(sample_width)
        wf.setframerate(RATE)
        wf.writeframes(data)
        wf.close()

def fbdistort(raw,thresh=THRESH):
    for i in range(len(raw)):
        '''if(i > thresh or i < -thresh):
            raw[i] = abs(abs(divmod(raw[i] - thresh,thresh*4)[1]) - thresh*2)'''
        if raw[i] > 0:
            raw[i] = int((1 - math.exp(-raw[i]))*50)
        else:
            raw[i] = int((math.exp(raw[i]) - 1)*50)

        # print(raw[i])

    return normalize(raw,13500)

def newSound():
    S, D, raw = record_to_file("C:/Users/yetski/Music/Recordings/Recording.wav")
    f = open("C:/Users/yetski/Music/Recordings/Raw.txt", "w+")
    for i in raw:
        f.write(str(i) + "\n")
    f.close()
    raw = fbdistort(raw, 400)
    f = open("C:/Users/yetski/Music/Recordings/Raw2.txt", "w+")
    for i in raw:
        f.write(str(i) + "\n")
    f.close()
    print("done")
    test_to_file(S, D, raw, "C:/Users/yetski/Music/Recordings/Recording2.wav")
    print("done2")
    with wave.open("C:/Users/yetski/Music/Recordings/Recording.wav") as wf:
        print(wf.readframes(wf.getnframes()))
        wf.close()

if __name__ == "__main__":
    S,D,raw = record_to_file("C:/Users/yetski/Music/Recordings/Recording.wav")
    f = open("C:/Users/yetski/Music/Recordings/Raw.txt","w+")
    print(raw)
    for i in raw:
        f.write(str(i) + "\n")
    f.close()

    raw = fbdistort(raw,400)
    f = open("C:/Users/yetski/Music/Recordings/Raw2.txt","w+")
    for i in raw:
        f.write(str(i) + "\n")
    f.close()
    print("done")
    test_to_file(S,D,raw,"C:/Users/yetski/Music/Recordings/Recording2.wav")
    print("done2")
    with wave.open("C:/Users/yetski/Music/Recordings/Recording.wav") as wf:
        print(wf.readframes(wf.getnframes()))
        wf.close()

