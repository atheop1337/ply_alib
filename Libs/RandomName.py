import random

def generate_random_name():
    vowels = 'aeiou'
    consonants = 'bcdfghjklmnpqrstvwxyz'
    name_length = random.randint(3, 8)
    name = ''
    for i in range(name_length):
        if i % 2 == 0:
            name += random.choice(consonants)
        else:
            name += random.choice(vowels)
    return name.capitalize()

random_name = generate_random_name()
