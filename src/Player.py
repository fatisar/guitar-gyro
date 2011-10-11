from utils import *
from parselib import xml2abc
from parselib import midi2abc
import re

class Player:
    def tokenize_header(self,header):
        header = header.split("\n")
        for i,h in enumerate(header):
            header[i] = h[2:]
        return header

    def tokenize_body(self,body):
        print body
        return body

    def tokenize_score(self,score):
        print "tokenizing score..."
        header_i = 0    # an index to the end of the header

        header_re = re.compile("\d:")
        # iterate through score until we find "V:", the end of the header section
        while header_re.search(score[header_i:header_i+2]) != None:   # V: is presumably the beginning of the last line of the header
            header_i += 1
        header_end = score.find("\n",header_i) + 2  # +2 to include the newline
        self.header_fields = self.tokenize_header(score[0:header_end])
        self.score_tokens = self.tokenize_body(score[header_end:])
        
        return

    def read_and_parse_file(self,filename):
        print "reading %s" % filename
        score_src = ""
        if filename[-3:] == "xml":
            score_src = xml2abc.xml_to_abc(filename)
        elif filename[-3:] == "mid":
            score_src = midi2abc.midi_to_abc(filename)
        else:
            print "Error reading %s" % filename
            return

        print score_src
        self.tokenize_score(score_src)
        
    def __init__(self):
        print "initializing default Player..."
        self._note_map = NoteMap()._note_map
        phrase = ["C","E","G","B'","C'"]
        self._phrase_graph = PhraseGraph(phrase)
        print "%s" % self._phrase_graph