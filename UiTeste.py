'''import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
import wave
style.use('fivethirtyeight')

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

def animate(i):
    data = open('C:/Users/yetski/Music/Recordings/Raw.txt','r').read()
    lines = data.split('\n')
    xs = []
    ys = []
    x = 0.1
    for line in lines:
        xs.append(x)
        x += 0.1
        ys.append(line)

    ax1.clear()
    ax1.plot(xs,ys)

ani = animation.FuncAnimation(fig,animate,interval=1000)
plt.show()'''
# Load the required libraries:
#   * scipy
#   * numpy
#   * matplotlib
from scipy.io import wavfile
from matplotlib import pyplot as plt
import numpy as np


def showAmplitudeGraph(path='C:/Users/yetski/Music/Recordings/Recording.wav'):
    # Load the data and calculate the time of each sample
    print('test')
    samplerate, data = wavfile.read(path)
    d = open('C:/Users/yetski/Music/Recordings/Raw.txt', 'r').read()
    lines = d.split('\n')
    print("test", list(data))
    print("test2", lines)
    times = np.arange(len(data)) / float(samplerate)

    # Make the plot
    # You can tweak the figsize (width, height) in inches
    plt.figure(figsize=(6.5, 4))
    plt.fill_between(times, data, color='k')
    plt.xlim(times[0], times[-1])
    plt.xlabel('time (s)')
    plt.ylabel('amplitude')
    # You can set the format by changing the extension
    # like .pdf, .svg, .eps
    # plt.savefig('plot.png', dpi=100)
    plt.show()

if __name__ == "__main__":
    showAmplitudeGraph()