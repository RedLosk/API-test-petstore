import random
import string

def random_string(length=10):
    #Generates a random string
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(length))

def random_number(min_val=1, max_val=999999):
    #Generates a random number
    return random.randint(min_val, max_val)

def random_email():
    #Generates a random email
    username = random_string(8)
    domain = random_string(5)
    return f"{username}@{domain}.com"

def generate_pet():
    #Generates pet data
    return {
        "id": random_number(),
        "name": f"Pet_{random_string(5)}",
        "photoUrls": [f"https://example.com/photo_{random_number(1, 5)}.jpg"],
        "status": random.choice(["available", "pending", "sold"])
    }

def generate_order(pet_id=None):
    #Generates order data
    return {
        "id": random_number(),
        "petId": pet_id or random_number(),
        "quantity": random_number(1, 10),
        "status": "placed",
        "complete": False
    }

def generate_user():
    #Generates user data
    username = f"user_{random_string(6)}"
    return {
        "id": random_number(),
        "username": username,
        "firstName": f"First_{random_string(4)}",
        "lastName": f"Last_{random_string(4)}",
        "email": random_email(),
        "password": random_string(8),
        "phone": f"+1{random.randint(1000000000, 9999999999)}",
        "userStatus": 0
    }