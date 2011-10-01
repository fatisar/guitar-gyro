# A Note represents a fret-computed note in the final output
class Note:

    def __init__(self, fnote, duration=None):
        self._duration = duration           # the duration of the note, as a fraction of a measure
        self._fnote = fnote                 # the FrettedNote for this object, representing the guitar position where this note is played
