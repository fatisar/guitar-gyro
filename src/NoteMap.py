__author__ = 'Daniel'

# A Note models the basic elements of a note: name, duration, ...
class Note:
    def __init__(self, note_name, duration):
        self.note_name = note_name
        self.duration = duration
        self.positions = NoteMap.note_map[note_name]    # a list of possible positions this note could be played in

    # return all the possible combinations of positions and distances
    def distance(self,note):
        dists = []
        for i in range(len(self.positions)):
            my_pos = self.positions[i]
            for j in range(len(note.positions)):
                other_pos = note.positions[j]
                dists.append((my_pos,other_pos,my_pos.distance(other_pos)))

        return dists



# A FrettedNote represents a note as found on a guitar
class FrettedNote(Note):

    def __init__(self, note_name, string, fret):
        self.note_name = note_name
        self.string = string
        self.fret = fret
        self.id = "%s-%s" % (string, fret)

    def distance(self,note):
        # 'note - self' for string since moving 'up' the fretboard (i.e. towards a higher string) is +
        # 'self - note' for fret since moving across towards the bridge is -
        return (note.string - self.string, self.fret - note.fret)

    def __str__(self):
        return "%s [%s]" % (self.note_name,self.id)



# Encodes a mapping from notes to string-fret tuples
class NoteMap:
    # NOTE: The notes on a guitar range from E, to D#''

    postfix = (",","","'","''")
    letters = ("E","F","F#","G","G#","A","A#","B","C","C#","D","D#")

    note_map = dict()
    octave = 0
    oct_cnt = 16        # a count to determine when to increment 'octave'. starts at 16 to accommodate the layout of the guitar
    str_offset = 0      # an offset to determine the appropriate fret since letters[0] always starts with 'E'

    # NOTE: contrary to standard notation, the strings are numbered from 0-5, where 0 is the low E string
    def generate_note_map(self):
        for string in range(6):
            if string == 4: self.str_offset -= 1     # modify the offset to adjust for the B string
            for fret in range(12):
                note = "%s%s" % (self.letters[(fret+self.str_offset) % 12], self.postfix[self.octave])
                str_frt = [FrettedNote(note,string,fret)]

                def_note = self.note_map.setdefault(note,str_frt)        # def_note returns the value for the given key if one exists
                if def_note != str_frt:      # if the key already exists, chain the string-fret tuples
                    def_note.append(str_frt[0])
                    self.note_map.update(note = def_note)

                self.oct_cnt += 1
                if (self.oct_cnt % 24) == 0: self.octave += 1

            self.str_offset += 5        # increase the string offset for the next string

    def __init__(self):
        self.generate_note_map()