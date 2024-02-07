import random
import string


def random_choice(options):
    return random.choice(options)

def random_string(length=6):
    return ''.join([ random_choice(string.ascii_lowercase) for _ in range(length)])

def random_int(a=1, b=10):
    return random.randint(a, b)

def extract_variable(line):
    try:
        if('=' in line):
            return line.replace(' ','').split('=')[0]
        else:
            return None
    except:
        return None
    

# save the output in a file
def save_file(filename, output):
    f = open(f'{filename}.py', 'w')
    f.write(output)
    f.close()