# E, to D#''
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
        str_frt = [(string,fret)]
        note = "%s%s" % (letters[(fret+str_offset) % 12], postfix[octave])

        def_note = note_map.setdefault(note,str_frt)        # def_note returns the value for the given key if one exists
        if(len(def_note) > 1):      # if the key already exists, chain the string-fret tuples
            def_note.append(str_frt)
            note_map.update(note = def_note)

        oct_cnt += 1
        if (oct_cnt % 24) == 0: octave += 1

    str_offset += 5

