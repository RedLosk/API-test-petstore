from URL import BASE_URL

def pet_endpoint():
    return f"{BASE_URL}/pet"

def pet_by_id(pet_id):
    return f"{BASE_URL}/pet/{pet_id}"

def pets_by_status():
    return f"{BASE_URL}/pet/findByStatus"

def store_inventory():
    return f"{BASE_URL}/store/inventory"

def store_order():
    return f"{BASE_URL}/store/order"

def order_by_id(order_id):
    return f"{BASE_URL}/store/order/{order_id}"

def user_endpoint():
    return f"{BASE_URL}/user"

def user_by_username(username):
    return f"{BASE_URL}/user/{username}"

def user_login():
    return f"{BASE_URL}/user/login"

def user_logout():
    return f"{BASE_URL}/user/logout"

def create_users_list():
    return f"{BASE_URL}/user/createWithList"