def p_select_statement(p):
    '''select_statement : SELECT ID PLUS ID PYC'''
    pass

def p_error(p):
    print p
    if p:
        print("Syntax error at '%s'" % p.value)
    else:
        print("Syntax error at EOF")
