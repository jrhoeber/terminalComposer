import math
import pyaudio
from PitchGenerator import PitchGenerator

print "\n\n\n\n\n\n\n\n\n\nWelcome to Terminal Composer!\n" \
        "Enter keys of the keyboard, a space, then the first leter of the note value\n" \
        "For example: D4 Q F#4 Q A4 Q would play an arpeggiated D major chord starting on the\n" \
        "D after middle C\nType 'exit' to close\n"
BPM = input("First enter a tempo (in BPM) between 40 and 200   ")

#timeSig = raw_input("Enter a time signature (4/4, 6/8, 3/4, etc.)  ")
#while not(BPM.is_integer()):
#    BPM = input("Enter new tempo within 40 and 200   ")
while (BPM > 200) or (BPM < 40):
    BPM = input("Enter new tempo within 40 and 200   ")

pitchGen = PitchGenerator(int(BPM))#, timeSig)
while True:
    line = raw_input("Enter line of notes to play\n")
    line = line.upper()
    if line == "EXIT":
        quit()
    pitchGen.playLine(line)


