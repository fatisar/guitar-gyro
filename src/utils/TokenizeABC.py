__author__ = 'Daniel'

import re

class TokenizeABC:

    def __init__(self,abc,tokens):
        tokens =  self.tokenize(abc,tokens)

    def tokenize_header(self,header):
        header = header.split("\n")
        for i,h in enumerate(header):
            header[i] = h[2:]
        return header

    def tokenize_body(self,body):
        print body
        return body

    def tokenize(self,score,tokens):
        print "tokenizing score..."
        header_i = 0    # an index to the end of the header

        header_re = re.compile("\d:")
        # iterate through score until we find "V:", the end of the header section
        while header_re.search(score[header_i:header_i+2]) is not None:   # V: is presumably the beginning of the last line of the header
            header_i += 1
        header_end = score.find("\n",header_i) + 2  # +2 to include the newline
        header_fields = self.tokenize_header(score[0:header_end])
        score_tokens = self.tokenize_body(score[header_end:])
        tokens.append((header_fields,score_tokens))
        return
