import math
import pyaudio
from PitchGenerator import PitchGenerator

x = PitchGenerator()
waveD = x.generateWaveData("C5", 'q')
x.playWaveData(waveD)
waveD = x.generateWaveData("D5", 'q')
x.playWaveData(waveD)
waveD = x.generateWaveData("E5", 'q')
x.playWaveData(waveD)
waveD = x.generateWaveData("F5", 'q')
x.playWaveData(waveD)
waveD = x.generateWaveData("G5", 'q')
x.playWaveData(waveD)
waveD = x.generateWaveData("A5", 'q')
x.playWaveData(waveD)
waveD = x.generateWaveData("B5", 'q')
x.playWaveData(waveD)
waveD = x.generateWaveData("C6", 'q')
x.playWaveData(waveD)

