import utils

input_file_path = './input_example.py'

variables_mapping = {} # old variable to new variable
variables = []

output = ''
with open(input_file_path, 'r') as f:
    for line in f.readlines():
        new_line = line
        variable = utils.extract_variable(line)

        if(variable is not None):
            variables.append(variable)

            if(variable not in variables_mapping.keys()):
                new_variable = utils.random_string()
                variables_mapping[variable] = new_variable
            new_line = new_line.replace(variable, variables_mapping[variable])

        for var in variables:
            if(var in new_line):
                new_line = new_line.replace(var, variables_mapping[var])
        output += f'{new_line}\n'



f = open('output.py', 'w')
f.write(output)
f.close()