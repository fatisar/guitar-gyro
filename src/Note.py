import NoteMap

# A FrettedNote represents a note as found on a guitar
class FrettedNote:
    
    def __init__(self, note_name, string, fret):
        self.note_name = note_name
        self.string = string
        self.fret = fret
        self.id = "%s-%s" % (string, fret)

    def distance(self,note):
        # note - self for string since moving 'up' the fretboard (i.e. towards a higher string) is +
        # self - note for fret since moving across towards the bridge is -
        return (note.string - self.string, self.fret - note.fret)

    def __str__(self):
        return "%s [%s]" % (self.note_name,self.id)


# A Note represents a note as found on a score
class ScoreNote:
    def __init__(self, note_name, duration):
        self.note_name = note_name
        self.duration = duration
        self.positions = NoteMap.note_map[note_name]    # a list of possible positions this note could be played in
        
    def distance(self,note):
        dists = []
        for i in range(len(self.positions)):
            my_pos = self.positions[i]
            for j in range(len(note.positions)):
                other_pos = note.positions[j]
                dists.append((my_pos,other_pos,my_pos.distance(other_pos)))

        return dists
