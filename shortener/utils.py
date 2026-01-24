import random
import string

def generate_short_code(length=6):
    """Generates a random string of fixed length"""
    chars = string.ascii_letters + string.digits  # a-z, A-Z, 0-9
    return ''.join(random.choice(chars) for _ in range(length))