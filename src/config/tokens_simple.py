
# reserved = {""}

# LISTA DE TOKENS
tokens = (
    # PALABRAS RESERVADAS
    'SELECT', 'ID', 'FROM', 'WHITESPACE', 'PLUS','PYC'
)
t_ignore = '\t\r'
t_PLUS   = r'\+'
t_PYC   = r';'

def t_WHITESPACE(t):
    r'\ '

def t_SELECT(t):
    r'select | SELECT'
    return t

def t_FROM(t):
    r'from | FROM'
    return t

def t_ID(t):
    r'\$[a-zA-Z_]\w*'
    # r'\$[^aeiou][.]?\#(\w)*'
    # t.type = reserved.get(t.value,'ID')
    t.value= t.value.lower()
    return t

def t_error(t):
    print t
    print "Error lexico:" + str(t.value[0])
    t.lexer.skip(1)
    