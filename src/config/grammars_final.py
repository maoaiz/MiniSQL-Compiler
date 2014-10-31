def p_program(p):
    'program : sql_list'
    pass

def p_sql_list(p):
    '''sql_list : sql SEMICOLON
        | sql_list sql SEMICOLON'''
    pass

def p_sql(p):
    '''sql : sql sql
      | schema
      | manipulative_statement
      | schema_element
      | schema_func'''
    pass

def p_schema_func(p):
    '''schema_func : return_type ID LPAREN parameters RPAREN LBLOCK function_body RBLOCK'''
    pass

def p_function_body(p):
    '''function_body : empty
        | cicles
        | instructions
        | assignment'''
    pass

def p_cicles(p):
    '''cicles : while
        | for'''
    pass

def p_while(p):
    '''while : WHILE LPAREN conditions RPAREN LBLOCK instructions RBLOCK'''
    pass

def p_for(p):
    '''for : empty'''
    pass

def p_conditions(p):
    '''conditions : arg operators arg
        | conditions OR conditions
        | conditions AND conditions
        | LPAREN conditions RPAREN'''
    pass

def p_arg(p):
    '''arg : ID
        | NULL'''
    pass


def p_operators(p):
    '''operators : LESS
        | LESSEQUAL
        | GREATER
        | GREATEREQUAL
        | DEQUAL
        | COMPARISON'''
    pass


def p_instructions(p):
    '''instructions : print'''
    pass

def p_print(p):
    '''print : PRINT LPAREN QUOTE STRING QUOTE RPAREN SEMICOLON
        | PRINT LPAREN  ID  RPAREN SEMICOLON'''
    pass


def p_parameters(p):
    '''parameters : manipulative_statement
        | manipulative_statement SEMICOLON
        | arguments'''
    pass

def p_arguments(p):
    '''arguments : return_type ID
        | return_type ID COMMA arguments'''
    pass


def p_return_type(p):
    '''return_type : CHAR
        | IDENTITY
        | VARCHAR
        | NUMBER
        | INT
        | FLOAT
        | DOUBLE
        | BIT
        | SMALLDATETIME'''
    pass


def p_schema(p):
    'schema : CREATE SCHEMA AUTHORIZATION user opt_schema_element_list'
    pass

def p_user(p):
    'user : ID'
    pass

def p_opt_table_element_list(p):
    '''opt_schema_element_list : empty
        | schema_element_list'''
    pass

def p_schema_element_list(p):
    '''schema_element_list : schema_element
        | schema_element_list schema_element'''
    pass

# Elementos de una tabla
def p_schema_element(p):
    '''schema_element : base_table_def
        | view_def
        | privilege_def'''
    pass


        # | schema_element schema_element
        # | schema_element manipulative_statement
        # | manipulative_statement schema_element
        # | manipulative_statement



#Creacion de una Tabla
def p_base_table_def(p):
    'base_table_def : CREATE TABLE table LPAREN base_table_element_commalist RPAREN'
    pass

def p_base_table_element_commalist(p):
  '''base_table_element_commalist : base_table_element
          | base_table_element_commalist COMMA base_table_element'''
  pass

def p_base_table_element(p):
  '''base_table_element : column_def
        | constraint_def
        | table_constraint_def'''
  pass

# Definicion de las columnas (Nombre, Tipo de dato, definicion opcional)
def p_column_def(p):
  'column_def : column data_type column_def_opt_list'
  pass

# Tipo de dato
def p_data_type(p):
  '''data_type : CHAR
      | INT IDENTITY identity
      | CHAR LPAREN NUMBER RPAREN
      | VARCHAR
      | VARCHAR LPAREN NUMBER RPAREN
      | INT
      | FLOAT
      | DOUBLE
      | BIT
      | SMALLDATETIME''' 
  pass

def p_literal(p):
  '''literal : literal ID
      | ID
      | literal NUMBER
      | NUMBER'''
  pass

def p_identity(p):
  'identity : LPAREN literal COMMA literal RPAREN'
  pass

# Definicion Opcional (NOT NULL, NULL, ....)
def p_column_def_opt_list(p):
  '''column_def_opt_list : column_def_opt_list column_def_opt
        | column_def_opt'''
  pass


def p_column_def_opt(p):
  '''column_def_opt : empty
        | NOT NULL
        | NULL
        | NOT NULL UNIQUE
        | NOT NULL PRIMARY KEY
        | DEFAULT NULL
        | DEFAULT USER
        | CHECK LPAREN search_condition RPAREN
        | REFERENCES table
        | REFERENCES table LPAREN column_commalist RPAREN'''
  pass

#condiciones de busqueda
def p_search_condition(p):
  '''search_condition : search_condition OR search_condition
        | search_condition AND search_condition
        | NOT search_condition
        | LPAREN search_condition RPAREN
        | predicate'''
  pass 

def p_predicate(p):
    '''predicate : comparison_predicate
            | assignment_predicate
            | between_predicate
            | like_predicate
            | test_for_null
            | in_predicate
            | all_cr_any_predicate
            | existence_test'''
    pass 

def p_comparison_predicate(p):
    '''comparison_predicate : scalar_exp COMPARISON scalar_exp
                | scalar_exp COMPARISON subquery'''
    pass 

def p_assignment_predicate(p):
    '''assignment_predicate : assignment'''
    pass 

def p_subquery(p):
    'subquery : LPAREN SELECT opt_all_distinct selection table_exp RPAREN'
    pass


def p_between_predicate(p):
    '''between_predicate : scalar_exp NOT BETWEEN scalar_exp AND scalar_exp
                | scalar_exp BETWEEN scalar_exp AND scalar_exp'''
    pass 

def p_like_predicate(p):
    '''like_predicate : scalar_exp NOT LIKE atom empty
                | scalar_exp LIKE atom empty'''
    pass

def p_test_for_null(p):
    '''test_for_null : column_ref IS NOT NULL
                | column_ref IS NULL'''
    pass 

def p_in_predicate(p):
    '''in_predicate : scalar_exp NOT IN LPAREN subquery RPAREN
            | scalar_exp IN LPAREN subquery RPAREN
            | scalar_exp NOT IN LPAREN atom_commalist RPAREN
            | scalar_exp IN LPAREN atom_commalist RPAREN'''
    pass 

def p_atom_commalist(p):
    '''atom_commalist : atom
                | atom_commalist COMMA atom'''
    pass 

def p_all_cr_any_predicate(p):
    'all_cr_any_predicate : scalar_exp COMPARISON any_all_some subquery'
    pass

def p_any_all_some(p):
    '''any_all_some : ANY
            | ALL
            | SOME'''
    pass

def p_existence_test(p):
    'existence_test : EXISTS subquery'
    pass


def p_column_commalist(p):
  '''column_commalist : empty
        | column
        | column_commalist COMMA column
        | LPAREN column_commalist RPAREN''' 
  pass

def p_constraint_def(p):
  'constraint_def : CONSTRAINT ID table_constraint_def'
  pass

def p_table_constraint_def(p):
  '''table_constraint_def : UNIQUE LPAREN column_commalist RPAREN
        | PRIMARY KEY LPAREN column_commalist RPAREN
        | FOREIGN KEY LPAREN column_commalist RPAREN REFERENCES table
        | FOREIGN KEY LPAREN column_commalist RPAREN REFERENCES table LPAREN column_commalist RPAREN
        | CHECK LPAREN search_condition RPAREN''' 
  pass

#vista de tablas
def p_view_def(p):
  'view_def : CREATE VIEW table opt_column_commalist AS query_spec opt_with_check_option'
  pass

def p_opt_column_commalist(p):
  '''opt_column_commalist : empty
        | LPAREN column_commalist RPAREN'''
  pass

def p_query_spec(p):
  'query_spec : SELECT opt_all_distinct FROM selection table_exp'
  pass

def p_opt_with_check_option(p):
  '''opt_with_check_option : empty 
    | WITH CHECK OPTION'''
  pass


def p_opt_all_distinct(p):
  '''opt_all_distinct : empty
        | ALL
        | DISTINCT'''
  pass 

def p_selection(p):
  '''selection : scalar_exp_commalist
      | TIMES'''
  pass

def p_scalar_exp_commalist(p):
  '''scalar_exp_commalist : scalar_exp
        | scalar_exp_commalist COMMA scalar_exp'''
  pass

def p_table_exp(p):
  '''table_exp : from_clause
      | opt_where_clause
      | opt_group_by_clause'''
  pass 

def p_from_clause(p):
  'from_clause : FROM table_ref_commalist'
  pass

def p_table_ref_commalist(p):
  '''table_ref_commalist : table_ref
        | table_ref_commalist COMMA table_ref'''
  pass

def p_table_ref(p):
  '''table_ref : table
      | table range_variable'''
  pass

def p_range_variable(p):
  'range_variable : ID'
  pass

def p_opt_where_clause(p):
  '''opt_where_clause : empty 
        | where_clause'''
  pass

def p_where_clause(p):
  'where_clause : search_condition'
  pass

def p_opt_group_by_clause(p):
  '''opt_group_by_clause : empty
    | GROUP BY column_ref_commalist'''
  pass

def p_column_ref_commalist(p):
  '''column_ref_commalist : column_ref
        | column_ref_commalist COMMA column_ref'''
  pass


#esclares
def p_scalar_exp(p):
  '''scalar_exp : scalar_exp PLUS scalar_exp
      | scalar_exp MINUS scalar_exp
      | scalar_exp EQUAL scalar_exp
      | scalar_exp TIMES scalar_exp
      | scalar_exp DIVIDE scalar_exp
      | atom
      | column_ref
      | function_ref
      | LPAREN scalar_exp RPAREN'''
  pass 

def p_column_ref(p):
  '''column_ref : ID
      | ID DOT ID
      | ID DOT ID DOT ID'''
  pass 


def p_function_ref(p):
  '''function_ref : AMMSC LPAREN TIMES RPAREN
      | AMMSC LPAREN DISTINCT column_ref RPAREN
      | AMMSC LPAREN ALL scalar_exp RPAREN
      | AMMSC LPAREN scalar_exp RPAREN'''
  pass 


def p_privilege_def(p):
  'privilege_def : GRANT privileges ON table TO grantee_commalist opt_with_grant_option'
  pass


def p_opt_with_grant_option(p):
  '''opt_with_grant_option : empty 
    | WITH GRANT OPTION'''
  pass

def p_privileges(p):
  '''privileges : ALL PRIVILEGES
      | ALL 
      | operation_commalist'''
  pass

def p_operation_commalist(p):
  '''operation_commalist : operation
        | operation_commalist COMMA operation'''
  pass

# Opereaciones 
def p_operation(p):
  '''operation : SELECT
      | INSERT
      | DELETE
      | UPDATE opt_column_commalist
      | REFERENCES opt_column_commalist'''
  pass


def p_grantee_commalist(p):
  '''grantee_commalist : grantee
        | grantee_commalist COMMA grantee'''
  pass

def p_grantee(p):
  '''grantee : PUBLIC
      | user'''
  pass

def p_atom(p):
  '''atom : STRING
      | QUOTE parameter_ref QUOTE
      | NUMBER
      | QUOTE DATE1 QUOTE
      | QUOTE USER QUOTE'''
  pass 

def p_parameter_ref(p):
  '''parameter_ref : parameter
        | parameter_ref parameter 
        | parameter INDICATOR parameter'''
  pass 

def p_parameter(p):
  'parameter : ID'
  pass


# Manipulacion de sentencias 
def p_manipulative_statement_1(p):
  '''manipulative_statement : 
          | delete_statement
          | insert_statement
          | select_statement
          | update_statement
          | drop_table'''
  pass 

#update
def p_update_statement(p):
  '''update_statement : UPDATE table SET assignment_commalist WHERE where_conditions'''
  pass

def p_where_conditios(p):
    '''where_conditions : assignment
        | assignment OR where_conditions
        | assignment AND where_conditions
        | LPAREN where_conditions RPAREN
        | where_conditions
        '''
    pass


#drop
def p_drop_table(p):
    'drop_table : DROP TABLE table'
    pass


#delete
def p_delete_statement(p):
  'delete_statement : DELETE FROM table opt_where_clause'
  pass

#sentencia insert
def p_insert_statement(p):
  'insert_statement : INSERT INTO table opt_column_commalist values_or_query_spec'
  pass

def p_values_or_query_spec(p):
  '''values_or_query_spec : VALUES LPAREN insert_atom_commalist RPAREN
          | query_spec'''
  pass

def p_insert_atom_commalist(p):
  '''insert_atom_commalist : insert_atom
          | insert_atom_commalist COMMA insert_atom'''
  pass

def p_insert_atom(p):
  '''insert_atom : atom 
      | NULL'''
  pass


#SELECT
def p_select_statement(p):
  '''select_statement : SELECT opt_all_distinct selection INTO target_commalist table_exp
    | SELECT selection FROM table WHERE assignment_commalist assign_cond
    | SELECT selection FROM table'''
  pass


def p_target_commalist(p):
  '''target_commalist : target
        | target_commalist COMMA target'''
  pass

def p_target(p):
  'target : parameter_ref'
  pass

def p_assignment_commalist(p):
  '''assignment_commalist : assignment
        | assignment_commalist COMMA assignment'''
  pass

def p_assignment(p):
  '''assignment : column EQUAL scalar_exp
      | LPAREN assignment_commalist AMPERSANT AMPERSANT assignment_commalist RPAREN
      | column LESS scalar_exp
      | column GREATER scalar_exp
      | column EQUAL NULL'''
  pass

def p_assign_cond(p):
  '''assign_cond : assign_cond cond  assignment_commalist
      | cond  assignment_commalist'''
  pass

def p_cond(p):
  '''cond : cond OR
    | cond AND
    | cond AMPERSANT AMPERSANT
    | AND
    | OR
    | AMPERSANT AMPERSANT'''
  pass


def p_column(p):
  'column : ID'
  pass


def p_table(p):
    '''table : ID
      | ID DOT ID'''
    pass


def p_empty(p):
    'empty : '
    pass

def p_error(p):
    if p:
        print ("[Sintax Error] No se esperaba el simbolo '{}' en la linea {}".format(p.value, p.lineno))
    else:
        from src.SCM import Lexical, Parser, yacc
        while 1:
            tok = yacc.token()             # Get the next token
            if not tok or tok.type == 'RBRACE':
                break
        yacc.restart()