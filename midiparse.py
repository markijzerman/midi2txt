import sys, os
from music21 import converter

# get current path
pathname = os.path.abspath(os.path.dirname(sys.argv[0]))

# parse notes of midi file that is passed through argument in command line
curMidiFile = converter.parse(pathname + '/' + sys.argv[1])

# open file to write to
f = open(sys.argv[1][:-3] + 'txt', 'w')


for part in curMidiFile.parts:
    for event in part:

        if getattr(event, 'isChord', None) and event.isChord:
            tempchordlist = []
            tempchordlist = list(event.pitches)
            finishchordlist = []
            for item in tempchordlist:
                finishchordlist.append(item.midi)
            print ("%s %s %s" % (event.offset, event.duration.quarterLength, " ".join([str(x) for x in finishchordlist])))
            f.write("%s %s %s \n" % (event.offset, event.duration.quarterLength, " ".join([str(x) for x in finishchordlist])))

        if getattr(event, 'isNote', None) and event.isNote:
            print ("%s %s %s %s" % ("NOTE", event.pitch.midi, event.duration.quarterLength, event.offset))
            f.write("%s %s %s %s \n" % ("NOTE", event.pitch.midi, event.duration.quarterLength, event.offset))

        if getattr(event, 'isRest', None) and event.isRest:
            print("%s %s" % ("REST", event.duration.quarterLength))
            f.write("%s %s \n" % ("REST", event.duration.quarterLength))
    
f.close()

