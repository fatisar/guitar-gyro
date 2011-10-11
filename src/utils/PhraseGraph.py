__author__ = 'Daniel'
# PhraseGraph is a graph-representation of a currently-being-proccessed phrase
#  Input is a single, pre-computed phrase of notes
#  PhraseGraph builds a graph of all the possible combinations of finger-positions for the set of notes

from NoteMap import NoteMap
from LeftHand import LeftHand

lhand = LeftHand()

class Transition:
    def __init__(self, start_note, end_note):
        self._start_note = start_note
        self._end_note = end_note
        self._dist = start_note.distance(end_note)
        self._combos = lhand.get_combo_by_distance(self._dist)

    def __str__(self):
        cstr = "".join(["{0},".format(c) for c in self._combos])

        return "< %s ->  %s  %s : %s >" % (self._start_node,self._end_node,self._dist,cstr)

class PhraseNode:

    def __init__(self, fnote, transitions):
        self._fnote = fnote
        all_trans = [Transition(fnote,t) for t in transitions]
        self._transitions = [tr for tr in all_trans if len(tr._combos) > 0]        # clear out any transitions that are impossible

        
    def __str__(self):
        trans = "".join(["%s" % t for t in self._transitions])
        return "%s" % trans

class PhraseGraph:

    def __init__(self, phrase):
        self._graph = []
        self._note_map = NoteMap()._note_map
        self.build_phrase_graph(phrase)

    def build_phrase_graph(self, phrase):
        for n in range(len(phrase) - 1):
            fnotes = self._note_map[phrase[n]]
            trans = self._note_map[phrase[n+1]]
            for fn in fnotes:
                self._graph.append(PhraseNode(fn,trans))


    def __str__(self):
        str = []
        for node in self._graph:
            str.append("{ %s } \n" % node)

        return "".join(str)