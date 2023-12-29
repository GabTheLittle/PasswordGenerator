import random
from random import randint
import string

def pw_generator():
    specialCharacter = ["~","@","#","_","^","*","%","/",".","+",":",";","="]
    password = []
    for i in range (16):
        test = randint(1,3)
        if test == 1 :
            password.append(random.choice(string.ascii_letters))
        elif test == 2 :
            password.append(str(randint(0,9)))
        elif test == 3 :
            password.append(random.choice(specialCharacter))
    password = "".join(password)
    return password

print("Mot de passe généré :",pw_generator())