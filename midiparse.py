import sys, os
from music21 import converter

# get current path
pathname = os.path.abspath(os.path.dirname(sys.argv[0]))

# parse notes of midi file that is passed through argument in command line
parseNotes = converter.parse(pathname + '/' + sys.argv[1])

# open file to write to
f = open(sys.argv[1][:-3] + 'txt', 'w')


for p in parseNotes.parts:
    for n in p.flat.notes:
        print ("%s %s" % (n.pitch.midi, n.duration.quarterLength))
        f.write("%s %s \n" % (n.pitch.midi, n.duration.quarterLength))

f.close()