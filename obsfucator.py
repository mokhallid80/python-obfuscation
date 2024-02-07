import utils

# the file we will be obsfucating
input_file_path = './input_example.py'

# manging variables
variables_mapping = {} # old variable to new variable
variables = []

# our output result
output = ''

# processing functions
def handle_variables(line):
    handle_left_side_variable(line)
    return handle_right_side_variables(line)

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

# reading the input file line by line
with open(input_file_path, 'r') as f:
    for line in f.readlines():
        new_line = handle_variables(line)
        output += f'{new_line}\n'


# save the output in a file
utils.save_file('obsfucated_output', output)