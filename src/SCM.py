from libs.ply import lex
from config.reserved_words import reserved_words as reserved
from config.tokens import tokens
from config.tokens_re import *


class SCMCompiler(object):
    src = ""

    def __init__(self, src=None):
        self.src = src

    def compile(self):
        if self.lexer():
            print "Lexical analysis with success"
        else:
            print "Lexical analysis with ERROR"

    def lexer(self):
        lexer = lex.lex()
        f = open(self.src, 'r')
        data = f.read()
        lexer.input(data)
        while True:
            try:
                tok = lexer.token()
                if not tok:
                    print "not token"
                    break  # No more input
                print "Type: %s\ttoken: %s\tline %s" % (tok.type, tok.value, tok.lineno)
            except Exception, e:
                tok = "ERROR:", e
