__author__ = 'Daniel'

import Note

# Encodes a mapping from notes to string-fret tuples
# NOTE: The notes on a guitar range from E, to D#''

postfix = (",","","'","''")
letters = ("E","F","F#","G","G#","A","A#","B","C","C#","D","D#")

note_map = dict()
octave = 0
oct_cnt = 16        # a count to determine when to increment 'octave'. starts at 16 to accommodate the layout of the guitar
str_offset = 0      # an offset to determine the appropriate fret since letters[0] always starts with 'E'

# NOTE: contrary to standard notation, the strings are numbered from 0-5, where 0 is the low E string

for string in range(6):
    if string == 4: str_offset -= 1     # modify the offset to adjust for the B string
    for fret in range(12):
        note = "%s%s" % (letters[(fret+str_offset) % 12], postfix[octave])
        str_frt = [Note.FrettedNote(note,string,fret)]

        def_note = note_map.setdefault(note,str_frt)        # def_note returns the value for the given key if one exists
        if def_note != str_frt:      # if the key already exists, chain the string-fret tuples
            def_note.append(str_frt[0])
            note_map.update(note = def_note)
        print def_note
        oct_cnt += 1
        if (oct_cnt % 24) == 0: octave += 1

    str_offset += 5

print note_map
