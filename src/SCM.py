import os
from libs.ply import lex
from config.reserved_words import reserved_words as reserved
from config.tokens import tokens
from config.tokens_re import *


class SCMCompiler:

    def __init__(self, src=None, print_tokens=False):
        self.src = src
        self.print_tokens = print_tokens

    def compile(self):
        if self.lexer():
            print "\nLexical analysis with success"
        else:
            print "\n[ERROR]Lexical analysis with finished with ERROR"

    def lexer(self):
        if not self.src:
            self.printer("No code file")
            return False
        if not os.path.isfile(self.src):
            print "IOError: No such file: '{}'".format(self.src)
            return False
        f = open(self.src, 'r')
        data = f.read()
        f.close()
        lexer = lex.lex()
        lexer.input(data)
        while True:
            try:
                t = lexer.token()
                if not t:
                    self.printer("\n\tFinished. No more tokens")
                    break
                self.printer("\tType: {}\t\ttoken: {}\tline {}\tpos {}".format(t.type, t.value, t.lineno, t.lexpos))
                # self.printer(t)
            except Exception, e:
                print e
                return False
        return True

    def printer(self, text):
        if self.print_tokens:
            print text
