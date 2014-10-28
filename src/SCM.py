import os
from libs.ply import lex
from libs.ply import yacc

Lexical = None
from config.reserved_words import reserved_words as reserved
from config.tokens_final import *
# from config.tokens_simple import *
from config.tokens_re_final import *
from config.grammars import * 
# from config.grammars_simple import * 

class SCMCompiler:
    data = None
    lexer = None

    def __init__(self, src=None, print_tokens=False):
        self.src = src
        self.print_tokens = print_tokens

    def compile(self):
        if not self.lexer():
            print "\n[ERROR]Lexical analysis with finished with ERROR"
        else:
            print "\nLexical analysis finished"
        if not self.parser():
            print "Esto se jodio"
        else:
            print "\nSintax analysis finished"

    def parser(self):
        if self.data:
            try:
                parser = yacc.yacc()
                parser.parse(self.data, tracking=True)
                return True
            except Exception, e:
                print "[ERROR]", e
                return False

    def lexer(self):
        if not self.src:
            self.printer("No code file")
            return False
        if not os.path.isfile(self.src):
            print "IOError: No such file: '{}'".format(self.src)
            return False
        f = open(self.src, 'r')
        self.data = f.read()
        f.close()
        self.lexer = lex.lex()
        # print "'{}'".format(self.data[:10])
        self.lexer.input(self.data)
        while True:
            try:
                t = self.lexer.token()
                # print t
                if not t:
                    self.printer("\n\tFinished. No more tokens")
                    break
                self.printer("\tType: {}\t\ttoken: {}\tline {}\tpos {}".format(t.type, t.value, t.lineno, t.lexpos))
                # self.printer(t)
            except Exception, e:
                print "[ERROR]:", e
                return False
        # print "Retornando"
        global Lexical
        Lexical = self.lexer
        return True

    def printer(self, text):
        if self.print_tokens:
            print text
