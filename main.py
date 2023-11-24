import random
import string

def generate_password():
    characters = string.ascii_letters + string.digits

    password = "".join(random.choice(characters) for _ in range(6))

    return password
password = generate_password()
print(password)



