import utils

# the file we will be obsfucating
input_file_path = './input_example.py'

# manging variables
variables_mapping = {} # old variable to new variable
variables = []

# our output result
output = ''

# processing functions


# helper functions

# add the left side 'variable' to the array of variables
def handle_left_side_variable(line):
    variable = utils.extract_variable(line)
    if(variable is not None):
        variables.append(variable) 

        if(variable not in variables_mapping.keys()): # if we didn't see this variable before, assign a random string to it
            new_variable = utils.random_string()
            variables_mapping[variable] = new_variable

# to handle right side variables
def handle_right_side_variables(line):
    for var in variables:
        if(var in line):
            line = line.replace(var, variables_mapping[var]) # replace all variables in the line with the new mapped random variable
    return line

# generate a comment
def generate_comment_line():
    return f'#{utils.random_string(60)}'

# generate assignment line
def generate_assignment_line(selected_option):
    if(selected_option == 'string'):
        return f'{utils.random_string()} = "{utils.random_string(20)}"'
    if(selected_option == 'int'):
        return f'{utils.random_string()} = {utils.random_int(a=1, b=10000)}'
    if(selected_option == 'comb' and len(variables) > 0):
        return f'{utils.random_string()} = {variables_mapping[utils.random_choice(variables)]} + {variables_mapping[utils.random_choice(variables)]}'
    return generate_comment_line()


# main processing functions

def handle_variables(line):
    handle_left_side_variable(line)
    return handle_right_side_variables(line)

def generate_random_line(line, n=0.7):
    # n is the probability of adding a random line
    if(utils.random_int() <= n*10):
        # add a new line
        # options 
        # 1. Comment
        # 2. Variable assignment
            # a. String
            # b. Int
            # c. combination of variables
        options = ['comment', 'string', 'int', 'comb']
        selected_option = utils.random_choice(options)
        if(selected_option == 'comment'):
            new_line = generate_comment_line()
        if(selected_option == 'string' or selected_option == 'int' or selected_option == 'comb'):
            new_line = generate_assignment_line(selected_option)
        
        return line + '\n' + new_line
    
    return line

# reading the input file line by line
with open(input_file_path, 'r') as f:
    for line in f.readlines():
        new_line = generate_random_line(handle_variables(line))
        output += f'{new_line}\n'

# save the output in a file
utils.save_file('obsfucated_output', output)