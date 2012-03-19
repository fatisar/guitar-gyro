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
        self._best_combo = None

    def set_combos_by_finger(self, finger):
        self._combos = lhand.get_combo_by_finger(finger)
        self._best_combo = min(self._combos, key = lambda combo: combo[2])

    def get_best_combo(self):
        if self._best_combo is None:
            self._best_combo = min(self._combos, key = lambda combo: combo[2])
        return self._best_combo

    def __str__(self):
        cstr = "".join(["{0},".format(c) for c in self._combos])

        #return "< %s ->  %s  %s : %s >" % (self._start_note,self._end_note,self._dist,cstr)
        return "%s -> %s (%s)" % (self._start_note, self._end_note, self._best_combo)

class PhraseNode:

    def __init__(self, fnote, transitions):
        self._fnote = fnote
        all_trans = [Transition(fnote,t) for t in transitions]
        self._transitions = [tr for tr in all_trans if len(tr._combos) > 0]        # clear out any transitions that are impossible
        self._next = []             # a list of PhraseNodes
        self._best_trans = None
        self._finger = None

    def seed(self, finger):
        #print "seeding %s with %s" % (self,finger)
        for tn in self._transitions:
            tn.set_combos_by_finger(finger)

    def set_best_trans(self, best_trans):
        for n in self._next:
            if n._fnote == best_trans._end_note:
                self._best_trans = n
                break

    def __str__(self):
        #trans = "".join(["%s" % t for t in self._transitions])
        #return "%s" % trans
        return "%s" % self._fnote

class PhraseGraph:

    def __init__(self, phrase):
        self._graph = []
        self._note_map = NoteMap()._note_map
        self.build_phrase_graph(phrase)

    def build_phrase_graph(self, phrase):
        prev = []
        cnt = 0

        for n in range(len(phrase) - 1):
            fnotes = self._note_map[phrase[n]]          # the possible FrettedNotes for a given note
            trans = self._note_map[phrase[n+1]]         # the possible FrettedNotes for the next note
            tmp = []

            for fn in fnotes:
                pn = PhraseNode(fn,trans)   # add a new PhraseNode for the FrettedNote for this note, with transitions to the next note
                for i in prev:
                    self._graph[i]._next.append(pn)
                print "i:%s" % pn._next
                self._graph.append(pn)
                tmp.append(cnt)
                cnt += 1

            print "T:%s" % tmp
            prev = tmp




    def find_best_path(self):
        pnode = self._graph[0]

        while pnode:
            #best_trans = min(pnode._transitions, key = lambda trans: trans._dist[1])
            best_trans = min(pnode._transitions, key = lambda trans: min(trans._combos, key = lambda combo: combo[2]))
            best_combo = best_trans.get_best_combo()
            pnode.set_best_trans(best_trans)
            print "B:%s, %s" % (pnode,best_combo)
            pnode = pnode._best_trans
            if pnode: pnode.seed(int(best_combo[1]))


        return


    def __str__(self):
        str = []
        for node in self._graph:
            str.append("{ %s } \n" % node)

        return "".join(str)