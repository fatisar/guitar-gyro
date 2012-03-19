__author__ = 'Daniel'

import re

class TokenizeABC:

    def __init__(self,abc):
        self._abc = abc

    def tokenize_header(self,header):
        header = header.split("\n")
        for i,h in enumerate(header):
            header[i] = h[2:]
        return header

    def tokenize_body(self,body):
        return body

    def tokenize(self):
        print "tokenizing score..."
        header_i = 0    # an index to the end of the header

        header_re = re.compile("\d:")
        # iterate through score until we find "V:", the end of the header section
        while header_re.search(self._abc[header_i:header_i+2]) is not None:   # V: is presumably the beginning of the last line of the header
            header_i += 1
        header_end = self._abc.find("\n",header_i) + 2  # +2 to include the newline
        header_fields = self.tokenize_header(self._abc[0:header_end])
        score_tokens = self.tokenize_body(self._abc[header_end:])

        tokens = (header_fields,score_tokens)
        return tokens
        
