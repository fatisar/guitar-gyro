__author__ = 'Daniel'
# PhraseGraph is a graph-representation of a currently-being-proccessed phrase
#  Input is a single, pre-computed phrase of notes
#  PhraseGraph builds a graph of all the possible combinations of finger-positions for the set of notes

from NoteMap import NoteMap
from LeftHand import LeftHand

lhand = LeftHand()

class Transition:
    def __init__(self, start_node, end_node):
        self._start_node = start_node
        self._end_node = end_node
        self._dist = start_node.distance(end_node)
        self._combos = lhand.get_combo_by_distance(self._dist)

    def __str__(self):
        cstr = "hi"#".join(["%s," % c for c in self._combos])
        print "new:%s" % self._start_node
        for c in self._combos:
            print c
        return "< %s ->  %s  %s : %s >" % (self._start_node,self._end_node,self._dist,cstr)

class Node:

    def __init__(self, fnote, transitions):
        self._fnote = fnote
        self._transitions = [Transition(fnote,t) for t in transitions]

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
                self._graph.append((Node(fn,trans)))


    def __str__(self):
        str = []
        for node in self._graph:
            str.append("{ %s } \n" % node)

        return "".join(str)