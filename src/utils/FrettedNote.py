# A FrettedNote represents a note as found on a guitar
class FrettedNote:

    def __init__(self, note_name, string, fret):
        self._note_name = note_name
        self._string = string
        self._fret = fret
        self._id = "%s-%s" % (string, fret)
        self._name = "%s [%s]" % (self._note_name,self._id)

    def distance(self,other_note):
        # 'other - self' for string since moving 'up' the fretboard (i.e. towards a higher string) is +
        # 'self - other' for fret since moving across towards the bridge is -
        return (other_note._string - self._string, other_note._fret - self._fret)

    def __str__(self):
        return "%s" % self._name
