from .reserved_words import reserved_words as reserved
t_PLUS   = r'\+'
t_MINUS  = r'-'
t_TIMES  = r'\*'
t_DIVIDE = r'/'
t_EQUAL  = r'='
t_DISTINCT = r'!'
t_LESS   = r'<'
t_LESSEQUAL = r'<='
t_GREATER = r'>'
t_GREATEREQUAL = r'>='
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
t_DEQUAL = r'!='
# t_ISEQUAL = r'=='  
t_COMPARISON = r'=='  
t_MINUSMINUS = r'--'
t_PLUSPLUS = r'\+\+'
t_QUOTE = r'\'|\"'
t_ignore = '\t\r'

def t_STRING(t):
    # r'(.)*?(\ )(.)*'
    # r'\'([^"]|\\")*\''
    r'\'[\w\ +-/\*]+\''
    return t


def t_DATE2(t):
    r'date|DATE'
    return t

def t_DATE1(t):
    r'\d*-([0]?[1-9]|[1][0-2])-([3][0-1]|[2][0-9]|[1][0-9]|[0]?[1-9])'
    return t

def t_NL(t):
    r'\n+'
    # t.lexer.lineno += t.value.count("\n")
    t.lexer.lineno += 1

def t_error(t):
    print "Lexical error: Illegal character '%s'" % t.value[0]
    t.lexer.skip(1)

def t_WHITESPACE(t):
    r'\ '

def t_COMMENT(t):
    r'--(.)*?(\ )(.)*\n'
    # print "Se ignoro el comentario: '%s'" % t.value[:-2]
    t.lexer.lineno += 1

def t_COMMENT_OFFICIAL(t):
    r'/\*(.|\n)*?\*/'
    # print "Se ignoro el comentario: '%s'" %t.value
    t.lexer.lineno += t.value.count('\n')
    # return t

def t_comments(t):
    r'/\*(.|\n)*?\*/'
    t.lexer.lineno += t.value.count('\n')

def t_comments_C99(t):
    r'//(.)*?\n'
    t.lexer.lineno += 1

def t_NUMBER(t):
    r'[+|-]?\d+(\.\d+)?(E[+|-]?\d+)?'
    t.value = float(t.value)
    return t

def t_ID(t):
    r'[a-zA-Z_]\w*'
    # r'\$[^aeiou][.]?\#(\w)*'
    t.value= t.value.lower()
    t.type = reserved.get(t.value,'ID')
    return t

