import NoteMap
import xml2abc
import midi2abc

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
        header_i = 0    # an index variable used to determine the end of the header section
        while score[header_i:header_i+2] != "V:":   # V: is presumably the beginning of the last line of the header
            header_i += 1
        header_end = score.find("\n",header_i) + 2  # +2 to include the newline
        self.header_fields = self.tokenize_header(score[0:header_end])
        self.score_tokens = self.tokenize_body(score[header_end:])
        
        return

    def read_and_parse_file(self,filename):
        print "reading %s" % filename
        score_src = xml2abc.xml_to_abc(filename)
        self.tokenize_score(score_src)
        
    def __init__(self):
        print "initializing default Player..."
