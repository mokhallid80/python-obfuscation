import random
import string


def random_string(length=6):
    return ''.join([random.choice(string.ascii_lowercase) for _ in range(length)])


def extract_variable(line):
    try:
        if('=' in line):
            return line.replace(' ','').split('=')[0]
        else:
            return None
    except:
        return None