__author__ = 'Daniel'

# A Note models the basic elements of a note: name, duration, ...
class Note:
    _positions = []     # a list of possible positions where this note could be played
    
    def __init__(self, fnote, duration):
        self._note_name = note_name         # _note_name contains octave information (i.e. E' for an E in the second octave above middle C
        self._duration = duration
        self._positions.append(fnote)

    # return all the possible combinations of positions and distances
    def distance(self,note):
        dists = []
        for i in range(len(self._positions)):
            my_pos = self._positions[i]
            for j in range(len(note.positions)):
                other_pos = note.positions[j]
                dists.append((my_pos,other_pos,my_pos.distance(other_pos)))

        return dists



# A FrettedNote represents a note as found on a guitar
class FrettedNote(Note, object):

    def __init__(self, note_name, string, fret):
        super(FrettedNote,self).__init__(note_name, None)
        self._string = string
        self._fret = fret
        self._id = "%s-%s" % (string, fret)
        print "I am: %s" % self

    def distance(self,note):
        # 'note - self' for string since moving 'up' the fretboard (i.e. towards a higher string) is +
        # 'self - note' for fret since moving across towards the bridge is -
        return (note._string - self._string, self._fret - note._fret)

    def __str__(self):
        return "%s [%s]" % (self._note_name,self._id)



# Encodes a mapping from notes to string-fret 2-tuples
class NoteMap:
    # NOTE: The notes on a guitar range from E, to D#''

    postfix = (",","","'","''")
    letters = ("E","F","F#","G","G#","A","A#","B","C","C#","D","D#")

    _note_map = dict()
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
                print str_frt[0]

                def_note = self._note_map.setdefault(note,str_frt)        # def_note returns the value for the given key if one exists
                if def_note != str_frt:      # if the key already exists, chain the string-fret tuples
                    def_note.append(str_frt[0])
                    self._note_map.update(note = def_note)

                self.oct_cnt += 1
                if (self.oct_cnt % 24) == 0: self.octave += 1

            self.str_offset += 5        # increase the string offset for the next string

    def __init__(self):
        self.generate_note_map()