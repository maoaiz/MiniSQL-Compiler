from .reserved_words import reserved_words as reserved
t_ignore = ' \t\r'

# Regular expressions rules for a simple tokens 
t_PLUS   = r'\+'
t_MINUS  = r'-'
t_TIMES  = r'\*'
t_DIVIDE = r'/'
t_EQUAL  = r'='
t_DISTINT = r'!'
t_LESS   = r'<'
t_GREATER = r'>'
t_SEMICOLON = ';'
t_COMMA  = r','
t_LPAREN = r'\('
t_RPAREN  = r'\)'
t_LBRACKET = r'\['
t_RBRACKET = r'\]'
t_LBLOCK   = r'{'
t_RBLOCK   = r'}'
t_COLON   = r':'
t_AMPERSANT = r'\&'
t_HASHTAG = r'\#'
t_DOT = r'\.'


def t_NL(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")


def t_error(t):
    print "Illegal character '%s'" % t.value[0]
    t.lexer.skip(1)


def t_comments(t):
    r'/\*(.|\n)*?\*/'
    t.lexer.lineno += t.value.count('\n')

def t_comments_C99(t):
    r'//(.)*?\n'
    t.lexer.lineno += 1

def t_comments0(t):
    r'--(.)*?\n'
    t.lexer.lineno += 1


def t_comments1(t):
    r'\#(.)*?\n'
    t.lexer.lineno += 1
    

def t_NUMBER(t):
    r'[+|-]?\d+(\.\d+)?(E[+|-]?\d+)?'
    t.value = float(t.value)
    return t


def t_LESSEQUAL(t):
	r'<='
	return t

def t_GREATEREQUAL(t):
	r'>='
	return t

def t_DEQUAL(t):
	r'!='
	return t

def t_ISEQUAL(t):
	r'=='
	return t
    
def t_MINUSMINUS(t):
	r'--'
	return t

def t_PLUSPLUS(t):
	r'\+\+'
	return t

def t_ID(t):
    r'[a-zA-Z_]\w*'
    t.type = reserved.get(t.value,'ID')
    return t