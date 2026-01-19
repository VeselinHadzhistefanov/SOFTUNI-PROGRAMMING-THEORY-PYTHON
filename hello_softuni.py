select = 1

recepient_name = "softuni"
this_is_a_random_variable = "Hello "
my_var = this_is_a_random_variable

general_statement = None

if select == 1:
    # Assignment method 1: Ternary conditional expression
    general_statement = "Hello world!" if my_var == None else my_var

elif select == 2:
    # Assignment method 2: Imperative reassignment
    general_statement = "Hello world"
    if my_var != None:
        general_statement = my_var

elif select == 3:
    # Assignment method 3: If-else block
    if my_var == None:
        general_statement = "Hello world!"
    else:
        general_statement = my_var

print(general_statement)