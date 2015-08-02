import math
from pyaudio import PyAudio


class PitchGenerator(object):
    def __init__(self, beatsPerMinute = 60, timeSignature = "4/4", key = "c"):
            
        self.BPM = beatsPerMinute
        self.timeSig = timeSignature.split('/')
        beatLength = 60 / beatsPerMinute
        self.key = key
        self.bitRate = 16000
        self.generateNoteDictionary()
        self.noteValueDict = { 'w' : beatLength * 4,
                               'h' : beatLength * 2,
                               'q' : beatLength,
                               'e' : beatLength / 2,
                               's' : beatLength / 4 }


    def generateNoteDictionary(self):
        initFreq = 27.5
        twthOfTwo = 2^(1/12)
        keyNoteDict = {  0  : ['A'],
                         1  : ['A#', 'Bb'],
                         2  : ['B', 'Cb'],
                         3  : ['C', 'B#'],
                         4  : ['C#', 'Db'],
                         5  : ['D'],
                         6  : ['D#', 'Eb'],
                         7  : ['E', 'Fb'],
                         8  : ['F', 'E#'],
                         9  : ['F#', 'Gb'],
                         10 : ['G'],
                         11 : ['G#', 'Ab']  }
        self.noteDict = { 'A0' : initFreq }
        for i in range(1,88):
            tempKeyNotes = keyNoteDict[i%12]
            for j in range(0, len(tempKeyNotes)):
                if i < 3:
                    self.noteDict[tempKeyNotes[j] + '0'] = (initFreq * (2.0 ** (1.0/12.0)) ** i)
                else:
                    self.noteDict[tempKeyNotes[j] + str(int(math.floor((i - 3) / 12) + 1))] =\
                            (initFreq * (2.0 ** (1.0/12.0)) ** i)

    def generateWaveData(self, note, noteValue):
        noteLen = self.noteValueDict[noteValue]
        noteFreq = self.noteDict[note]
        numFrames = int(self.bitRate * noteLen)
        restFrames = numFrames % self.bitRate
        waveData = ''
        for x in xrange(numFrames):
            waveData = waveData + chr(int(math.sin(x / ((self.bitRate / noteFreq) / math.pi)) *127 + 128))
        for x in xrange(restFrames):
            waveData = waveData + chr(128)

        return waveData

    def playWaveData(self, waveData):
        p = PyAudio()
        stream = p.open(format = p.get_format_from_width(1),
                        channels = 1,
                        rate = self.bitRate,
                        output = True)
        stream.write(waveData)
        stream.stop_stream()
        stream.close()
        p.terminate()
