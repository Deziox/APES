import pylab as plt
import numpy as np
import time

from sys import byteorder
from array import array
from struct import pack
import pyaudio
import wave
import time
import math
import sys
import queue

'''
with open("C:/Users/yetski/Music/Recordings/Raw.txt") as f:
    data = f.read()

data = data.split('\n')
data.pop()
'''

CHUNKS = 1024
FORMAT = pyaudio.paInt16
RATE = 44100 # or less so my laptop can keep running
THRESH = 1000
STEREO = False

def normalize(data,MAX = 16384):
    x = float(MAX)/max(abs(i) for i in data)

    ret = array('h')
    for i in data:
        ret.append(int(i*x))
    return ret

def negInf(data):
    return max(data) < THRESH

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

def live(q):
    p = pyaudio.PyAudio()
    stream = p.open(format=FORMAT, channels=(2 if STEREO else 1), rate=RATE, input=True, output=True,
                    frames_per_buffer=CHUNKS)
    num_silent = 0
    started = False
    ret = array('h')

    print(q.get())

    j = array('h')
    j = []
    X = []
    # print(X)
    # print(j)

    plt.ion()
    # graph = plt.plot(X, j)[0]
    i = 0

    plt.setbufsize(4096)
    xs = 0
    while True:
        # little endian signed
        data = array('h', stream.read(CHUNKS))
        # data2 = data
        # data2 = array('h',map(int,str(int.from_bytes(bytes(data),byteorder='big',signed=False))))
        # data = data2
        print(xs,data)
        if byteorder == 'big':
            data.byteswap()
        j.extend(data)
        # print(len(j),len(j),j,j)
        # j = array('h',j)
        silent = negInf(data)
        if silent and started:
            num_silent += 1
        elif not silent and not started:
            started = True
        #if num_silent > 200:
        #   break
        # print(num_silent)
        # xs += 1
        # if (started and num_silent > 30) or xs > 650:
        #    break
        # if x > 650:
        #   break
        # print(j)
        j = normalize(j)
        X = [i for i in range(len(j))]
        graph = plt.plot(X, j)[0]
        graph.set_xdata(X)
        graph.set_ydata(j)
        plt.cla
        plt.draw()
        plt.pause(0.01)
        i += 4000
        # print(i)
        xs += 1
        print(xs,num_silent)
        if (started and num_silent > 15) or xs > 650:
            print('test')
            break

    sample_width = p.get_sample_size(FORMAT)
    stream.stop_stream()
    stream.close()
    p.terminate()
    plt.close()

    j = normalize(j)
    j = trim(j)
    j = add_silence(j, 0.5)

    print("test lol", j)
    '''
    raw = j
    f = open("C:/Users/yetski/Music/Recordings/Raw.txt", "w+")
    for i in raw:
        f.write(str(i) + "\n")
    f.close()

    data = pack('<' + ('h' * len(j)), *j)
    with wave.open('C:/Users/yetski/Music/Recordings/Recording.wav', 'wb') as wf:
        # wf = wave.open(path,'wb')
        wf.setnchannels((2 if STEREO else 1))
        wf.setsampwidth(sample_width)
        wf.setframerate(RATE)
        wf.writeframes(data)
        wf.close()
'''