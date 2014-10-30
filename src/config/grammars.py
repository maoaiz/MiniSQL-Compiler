
def p_program(p):
  'program : sql_list'
  pass

def p_sql_list(p):
  '''sql_list : sql SEMICOLON
        | sql_list sql SEMICOLON'''
  pass

# SCHEME: Define las Tablas
def p_sql(p):
  '''sql : schema
      | manipulative_statement
      | schema_element'''
  pass

def p_schema(p):
  'schema : CREATE SCHEMA AUTHORIZATION user opt_schema_element_list'
  pass

def p_user(p):
  'user : ID'
  pass

def p_opt_schema_element_list_1(p):
  'opt_schema_element_list : ' #vacio
  pass

def p_opt_table_element_list_2(p):
  'opt_schema_element_list : schema_element_list'
  pass

def p_schema_element_list_1(p):
  '''schema_element_list : schema_element
        | schema_element_list schema_element'''
  pass

# Elementos de una tabla
def p_schema_element_1(p):
  '''schema_element : base_table_def
        | view_def
        | privilege_def'''
  pass

#Creacion de una Tabla
def p_base_table_def(p):
  'base_table_def : CREATE TABLE table LPAREN base_table_element_commalist RPAREN'
  pass

def p_constraint_def(p):
  'constraint_def : CONSTRAINT ID table_constraint_def'
  pass

def p_base_table_element_commalist_1(p):
  '''base_table_element_commalist : base_table_element
          | base_table_element_commalist COMMA base_table_element'''
  pass

def p_base_table_element_1(p):
  '''base_table_element : column_def
        | constraint_def
        | table_constraint_def'''
  pass

def p_literal_1(p):
  '''literal : literal NAME2 
      | NAME2
      | ID'''
  pass

def p_literal_2(p):
  '''literal : literal NUMBER
      | NUMBER'''
  pass

# Definicion de las columnas (Nombre, Tipo de dato, definicion opcional)
def p_column_def(p):
  'column_def : column data_type column_def_opt_list'
  pass

def p_identity(p):
  'identity : LPAREN literal COMMA literal RPAREN'
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
      | DOUBLE''' 
  pass

# Definicion Opcional (NOT NULL, NULL, ....)
def p_column_def_opt_list_2(p):
  '''column_def_opt_list : column_def_opt_list column_def_opt
        | column_def_opt'''
  pass

def p_column_def_opt_0(p):
  'column_def_opt : '
  pass

def p_column_def_opt_1(p):
  '''column_def_opt : NOT NULL
        | NULL
        | NOT NULL UNIQUE
        | NOT NULL PRIMARY KEY
        | DEFAULT literal
        | DEFAULT NULL
        | DEFAULT USER
        | CHECK LPAREN search_condition RPAREN
        | REFERENCES table
        | REFERENCES table LPAREN column_commalist RPAREN'''
  pass

def p_table_constraint_def_1(p):
  '''table_constraint_def : UNIQUE LPAREN column_commalist RPAREN
        | PRIMARY KEY LPAREN column_commalist RPAREN
        | FOREIGN KEY LPAREN column_commalist RPAREN REFERENCES table
        | FOREIGN KEY LPAREN column_commalist RPAREN REFERENCES table LPAREN column_commalist RPAREN
        | CHECK LPAREN search_condition RPAREN''' 
  pass

def p_column_commalist_1(p):
  '''column_commalist : column
        | column_commalist COMMA column''' 
  pass

def p_column(p):
  'column : ID'
  pass

#vista de tablas
def p_view_def(p):
  'view_def : CREATE VIEW table opt_column_commalist AS query_spec opt_with_check_option'
  pass

def p_opt_with_check_option_1(p):
  'opt_with_check_option : '
  pass

def p_opt_with_check_option_2(p):
  'opt_with_check_option : WITH CHECK OPTION'
  pass

def p_opt_column_commalist_1(p):
  'opt_column_commalist : '
  pass

def p_opt_column_commalist_2(p):
  'opt_column_commalist : LPAREN column_commalist RPAREN'
  pass

#definicion de privilegios

def p_privilege_def(p):
  'privilege_def : GRANT privileges ON table TO grantee_commalist opt_with_grant_option'
  pass

def p_opt_with_grant_option_1(p):
  'opt_with_grant_option : '
  pass

def p_opt_with_grant_option_2(p):
  'opt_with_grant_option : WITH GRANT OPTION'
  pass

def p_privileges_1(p):
  '''privileges : ALL PRIVILEGES
      | ALL 
      | operation_commalist'''
  pass

def p_operation_commalist_1(p):
  '''operation_commalist : operation
        | operation_commalist COMMA operation'''
  pass

# Opereaciones 
def p_operation_1(p):
  '''operation : SELECT
      | INSERT
      | DELETE
      | UPDATE opt_column_commalist
      | REFERENCES opt_column_commalist'''
  pass

def p_grantee_commalist_1(p):
  '''grantee_commalist : grantee
        | grantee_commalist COMMA grantee'''
  pass

def p_grantee_1(p):
  '''grantee : PUBLIC
      | user'''
  pass


# def p_cursor_def(p):
#   'cursor_def : DECLARE cursor CURSOR FOR query_exp opt_order_by_clause'
#   pass

# def p_opt_order_by_clause_1(p):
#   'opt_order_by_clause : '
#   pass

# def p_opt_order_by_clause_2(p):
#   'opt_order_by_clause : ORDER BY ordering_spec_commalist'
#   pass

def p_ordering_spec_commalist_1(p):
  '''ordering_spec_commalist : ordering_spec
          | ordering_spec_commalist COMMA ordering_spec'''
  pass

def p_ordering_spec_1(p):
  '''ordering_spec : NUMBER opt_asc_desc
        | column_ref opt_asc_desc'''
  pass 

def p_opt_asc_desc_1(p):
  'opt_asc_desc : '
  pass 

def p_opt_asc_desc_2(p):
  '''opt_asc_desc : ASC
        | DESC'''
  pass 

def p_cursor(p):
  'cursor : ID'
  pass

def p_column_ref_1(p):
  '''column_ref : ID
      | ID DOT ID
      | ID DOT ID DOT ID'''
  pass 

# Manipulacion de sentencias 
def p_manipulative_statement_1(p):
  '''manipulative_statement : close_statement
          | commit_statement
          | delete_statement_positioned
          | delete_statement_searched
          | fetch_statement
          | insert_statement
          | open_statement
          | rollback_statement
          | select_statement
          | select_statement_1
          | select_statement_2
          | select_statement_3
          | update_statement_1
          | update_statement_positioned
          | update_statement_searched
          | drop_table'''
  pass 


def p_table(p):
    '''table : ID
      | ID DOT ID'''
    pass

#sentencias simples
def p_drop_table(p):
  'drop_table : DROP TABLE table'
  pass

def p_open_statement(p):
  'open_statement : OPEN cursor'
  pass

def p_close_statement(p):
  'close_statement : CLOSE cursor'
  pass

def p_commit_statement(p):
  'commit_statement : COMMIT WORK'
  pass

def p_rollback_statement(p):
  'rollback_statement : ROLLBACK WORK'
  pass

def p_delete_statement_positioned(p):
  'delete_statement_positioned : DELETE FROM table WHERE CURRENT OF cursor'
  pass

#sentencias fetch
def p_fetch_statement(p):
  'fetch_statement : FETCH cursor INTO target_commalist'
  pass

def p_target_commalist_1(p):
  '''target_commalist : target
        | target_commalist COMMA target'''
  pass

def p_target(p):
  'target : parameter_ref'
  pass

def p_parameter_ref_1(p):
  '''parameter_ref : parameter
        | parameter_ref parameter 
        | parameter INDICATOR parameter'''
  pass 

def p_parameter(p):
  'parameter : ID'
  pass

#sentencia insert
def p_insert_statement(p):
  'insert_statement : INSERT INTO table opt_column_commalist values_or_query_spec'
  pass

def p_values_or_query_spec_1(p):
  '''values_or_query_spec : VALUES LPAREN insert_atom_commalist RPAREN
          | query_spec'''
  pass

def p_insert_atom_commalist_1(p):
  '''insert_atom_commalist : insert_atom
          | insert_atom_commalist COMMA insert_atom'''
  pass

def p_insert_atom_1(p):
  '''insert_atom : atom 
      | NULL'''
  pass

def p_atom_1(p):
  '''atom : QUOTE parameter_ref QUOTE
      | QUOTE literal QUOTE
      | NUMBER
      | QUOTE DATE1 QUOTE
      | QUOTE USER QUOTE'''
  pass 

#sentencia delete
def p_delete_statement_searched(p):
  'delete_statement_searched : DELETE FROM table opt_where_clause'
  pass

def p_opt_where_clause_1(p):
  'opt_where_clause : '
  pass

def p_opt_where_clause_2(p):
  'opt_where_clause : where_clause'
  pass

def p_where_clause(p):
  'where_clause : search_condition'
  pass
#SENTENCIA SELECT *

def p_select_statement_1(p):
  'select_statement_1 : SELECT TIMES FROM table WHERE assignment_commalist assign_cond' 
  pass

def p_select_statement_2(p):
  'select_statement_2 : SELECT TIMES FROM table SEMICOLON' 
  pass

def p_select_statement_3(p):
  'select_statement_3 : SELECT TIMES FROM table PLUSPLUS' 
  pass


#sentencia update
def p_assign_cond(p):
  '''assign_cond : assign_cond cond  assignment_commalist
      | cond  assignment_commalist'''
  pass
def p_update_statement_positioned(p):
  '''update_statement_positioned : UPDATE table SET assignment_commalist WHERE assignment_commalist assign_cond SEMICOLON
      | UPDATE table SET assignment_commalist WHERE assignment_commalist assign_cond'''
  pass
def p_cond(p):
  '''cond : cond OR
    | cond AND
    | cond AMPERSANT AMPERSANT
    | AND
    | OR
    | AMPERSANT AMPERSANT'''
  pass
def p_assignment_commalist_1(p):
  '''assignment_commalist : assignment
        | assignment_commalist COMMA assignment'''
  pass

def p_assignment_1(p):
  '''assignment : column EQUAL scalar_exp
      | LPAREN assignment_commalist AMPERSANT AMPERSANT assignment_commalist RPAREN
      | column LESS scalar_exp
      | column GREATER scalar_exp
      | column EQUAL NULL'''
  pass

def p_update_statement_searched(p):
  '''update_statement_searched : UPDATE table SET assignment_commalist opt_where_clause SEMICOLON
      | UPDATE table SET assignment_commalist opt_where_clause'''
  pass

def p_update_statement_1(p):
  '''update_statement_1 : UPDATE table SET assignment_commalist WHERE search_condition SEMICOLON
      | UPDATE SEMICOLON'''
  pass


#esclares
def p_scalar_exp_1(p):
  '''scalar_exp : scalar_exp PLUS scalar_exp
      | scalar_exp EQUAL scalar_exp
      | scalar_exp TIMES scalar_exp
      | scalar_exp DIVIDE scalar_exp
      | atom
      | column_ref
      | function_ref
      | LPAREN scalar_exp RPAREN'''
  pass 

def p_scalar_exp_commalist_1(p):
  '''scalar_exp_commalist : scalar_exp
        | scalar_exp_commalist COMMA scalar_exp'''
  pass

def p_function_ref_1(p):
  '''function_ref : AMMSC LPAREN TIMES RPAREN
      | AMMSC LPAREN DISTINCT column_ref RPAREN
      | AMMSC LPAREN ALL scalar_exp RPAREN
      | AMMSC LPAREN scalar_exp RPAREN'''
  pass 

#sentencia select
def p_select_statement(p):
  'select_statement : SELECT opt_all_distinct selection INTO target_commalist table_exp'
  pass

def p_opt_all_distinct_1(p):
  'opt_all_distinct : '
  pass 

def p_opt_all_distinct_2(p):
  '''opt_all_distinct : ALL
        | DISTINCT'''
  pass 

def p_selection_1(p):
  '''selection : scalar_exp_commalist
      | TIMES'''
  pass

def p_query_exp_1(p):
  '''query_exp : query_term
      | query_exp UNION query_term
      | query_exp UNION ALL query_term'''
  pass 

def p_query_term_1(p):
  '''query_term : query_spec
      | LPAREN query_exp RPAREN'''
  pass 

def p_query_spec(p):
  'query_spec : SELECT opt_all_distinct FROM selection table_exp'
  pass

def p_table_exp_1(p):
  '''table_exp : from_clause
      | opt_where_clause
      | opt_group_by_clause'''
  pass 

"""
def p_table_exp_4(p):
  'table_exp : opt_having_clause'
  pass 
"""
def p_from_clause(p):
  'from_clause : FROM table_ref_commalist'
  pass

def p_table_ref_commalist_1(p):
  '''table_ref_commalist : table_ref
        | table_ref_commalist COMMA table_ref'''
  pass

def p_table_ref_1(p):
  '''table_ref : table
      | table range_variable'''
  pass

def p_range_variable(p):
  'range_variable : ID'
  pass

def p_opt_group_by_clause_1(p):
  'opt_group_by_clause : '
  pass

def p_opt_group_by_clause_2(p):
  'opt_group_by_clause : GROUP BY column_ref_commalist'
  pass

def p_column_ref_commalist_1(p):
  '''column_ref_commalist : column_ref
        | column_ref_commalist COMMA column_ref'''
  pass

"""
def p_opt_having_clause_1(p):
  'opt_having_clause : '
  pass

def p_opt_having_clause_2(p):
  'opt_having_clause : HAVING search_condition'
  pass
"""
#condiciones de busqueda
def p_search_condition_1(p):
  '''search_condition : search_condition OR search_condition
        | search_condition AND search_condition
        | NOT search_condition
        | LPAREN search_condition RPAREN
        | predicate'''
  pass 

def p_predicate_1(p):
  '''predicate : comparison_predicate
      | between_predicate
      | like_predicate
      | test_for_null
      | in_predicate
      | all_cr_any_predicate
      | existence_test'''
  pass 

def p_comparison_predicate_1(p):
  '''comparison_predicate : scalar_exp COMPARISON scalar_exp
        | scalar_exp COMPARISON subquery'''
  pass 

def p_between_predicate_1(p):
  '''between_predicate : scalar_exp NOT BETWEEN scalar_exp AND scalar_exp
        | scalar_exp BETWEEN scalar_exp AND scalar_exp'''
  pass 

def p_like_predicate_1(p):
  '''like_predicate : scalar_exp NOT LIKE atom opt_escape
        | scalar_exp LIKE atom opt_escape'''
  pass

def p_opt_escape_1(p):
  'opt_escape : '
  pass 
"""
def p_opt_escape_2(p):
  'opt_escape : escape_atom'
  pass
"""
def p_test_for_null_1(p):
  '''test_for_null : column_ref IS NOT NULL
        | column_ref IS NULL'''
  pass 

def p_in_predicate_1(p):
  '''in_predicate : scalar_exp NOT IN LPAREN subquery RPAREN
      | scalar_exp IN LPAREN subquery RPAREN
      | scalar_exp NOT IN LPAREN atom_commalist RPAREN
      | scalar_exp IN LPAREN atom_commalist RPAREN'''
  pass 

def p_atom_commalist_1(p):
  '''atom_commalist : atom
        | atom_commalist COMMA atom'''
  pass 

def p_all_cr_any_predicate(p):
  'all_cr_any_predicate : scalar_exp COMPARISON any_all_some subquery'
  pass

def p_any_all_some_1(p):
  '''any_all_some : ANY
      | ALL
      | SOME'''
  pass

def p_existence_test(p):
  'existence_test : EXISTS subquery'
  pass

def p_subquery(p):
  'subquery : LPAREN SELECT opt_all_distinct selection table_exp RPAREN'
  pass

def p_error(p):
    if 1:
        if p is not None:
            print ("\nERROR SINTACTICO EN LA LINEA " + str(p.lineno) + " NO SE ESPERABA EL TOKEN  '" + str(p.value)) + "'"
        else:
            from src.SCM import Lexical, Parser, yacc
            while 1:
              tok = yacc.token()             # Get the next token
              if not tok or tok.type == 'RBRACE': break
            yacc.restart()
            print ("\nERROR SINTACTICO EN LA LINEA: " + str(Lexical.lineno))
    else:
        raise Exception('syntax', 'error')
