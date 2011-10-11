import FrettedNote

# NoteMap encodes a mapping from notes to string-fret 2-tuples
class NoteMap:
    
    # NOTE: The notes on a guitar range from E, to D#''
    postfix = (",","","'","''")
    letters = ("E","F","F#","G","G#","A","A#","B","C","C#","D","D#")

    octave = 0
    oct_cnt = 16        # a count to determine when to increment 'octave'. starts at 16 to accommodate the layout of the guitar
    str_offset = 0      # an offset to determine the appropriate fret since letters[0] always starts with 'E'

    def __init__(self):
        self._note_map = dict()
        self.generate_note_map()
    
    # NOTE: contrary to standard notation, the strings are numbered from 0-5, where 0 is the low E string
    def generate_note_map(self):
        for string in range(6):
            if string == 4: self.str_offset -= 1     # modify the offset to adjust for the B string
            for fret in range(12):
                note = "%s%s" % (self.letters[(fret+self.str_offset) % 12], self.postfix[self.octave])
                str_frt = [FrettedNote.FrettedNote(note,string,fret)]

                def_note = self._note_map.setdefault(note,str_frt)        # def_note returns the value for the given key if one exists
                if def_note != str_frt:      # if the key already exists, chain the string-fret tuples
                    def_note.append(str_frt[0])
                    self._note_map.update(note = def_note)
                
                self.oct_cnt += 1
                if not (self.oct_cnt % 24): self.octave += 1        # if (self.oct_cnt % 24) == 0, change the octave

            self.str_offset += 5        # increase the string offset for the next string
