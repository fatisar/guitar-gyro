from utils import *
from parselib import xml2abc
from parselib import midi2abc

class Player:

    def __init__(self):
        print "initializing default Player..."
        
        self._note_map = NoteMap()._note_map




        

    def generate_tab_for_file(self,filename):
        tokens = self.read_and_tokenize_file(filename)
        phrases = self.parse_phrases(tokens)
        tabs = self.tabulate_phrases(phrases)

        #print tabs


    def tabulate_phrases(self, phrases):
        tabs = []
        
        for pg in phrases:
            tabbed_phrase = pg.find_best_path()
            tabs.append(tabbed_phrase)
        return tabs

    def parse_phrases(self, tokens):
        phrases = []
        phrase = ["C","D","E","F","G","A","B'","C'"]
        phrase = ["G","A","B","C#'","D'","E'","F#'","G"]
        phrase_graph = PhraseGraph(phrase)
        #print phrase_graph
        phrases.append(phrase_graph)
        
        return phrases


    def read_and_tokenize_file(self,filename):
        print "reading %s" % filename
        if filename[-3:] == "xml":
            abc = xml2abc.xml_to_abc(filename)
        elif filename[-3:] == "mid":
            abc = midi2abc.midi_to_abc(filename)
        else:
            print "Error reading %s" % filename
            return
        
        return TokenizeABC(abc).tokenize()

        
