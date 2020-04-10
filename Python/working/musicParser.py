#!/usr/local/bin/python3.7

import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
import librosa as lbr  
import librosa.display  
import IPython.display as ipd 
from scipy.fftpack import fft 
from glob import glob 

# Music source Directory 
#sourceDirectory = 'myDirectoryWithFiles' 
audioFiles = glob('*.wav') # reads all music files from directory, example uses .wav  
amplitude, freqHz = lbr.load(audioFiles[0]) #freqHz is sampling rate default 22KHz 
fftAudioFile = fft(amplitude) 
tempo, beats = lbr.beat.beat_track(y=amplitude, sr=freqHz) 
timeS = np.arange(0, len(amplitude)) / freqHz # time [s]  
#librosa.display.waveplot(amplitude, freqHz) 

# Plot Spectrogram 
stftData = lbr.stft(amplitude) #Short term Fourier transform 
stftDb = lbr.amplitude_to_db(abs(stftData)) 
librosa.display.specshow( stftDb, sr=freqHz, x_axis='time', y_axis='hz' )
librosa.display.specshow( stftDb, sr=freqHz, x_axis='time', y_axis='log' )
plt.colorbar()             
import pdb; pdb.set_trace() 



# Plot 
#plt.plot(timeS, amplitude) 
#plt.rcParams['agg.path.chunksize'] = 10000  #helps to plot long data set 
plt.plot(amplitude, np.abs(fftAudioFile) ) 
plt.xlabel('Time [s]')
plt.ylabel('Amplitude [ ]') 
plt.title('Amplitude Vs. Time') 
#plt.xlim(0, 5)
plt.show() 
