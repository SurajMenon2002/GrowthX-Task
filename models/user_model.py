from config import users_collection
from flask_bcrypt import generate_password_hash, check_password_hash

def create_user(username, password, role):
    if users_collection.find_one({"username": username}):
        return {"error": "Username already exists"}
    hashed_pw = generate_password_hash(password).decode('utf-8')
    users_collection.insert_one({"username": username, "password": hashed_pw, "role": role})
    return {"message": f"{role.capitalize()} registered successfully"}

def authenticate_user(username, password):
    user = users_collection.find_one({"username": username})
    if user and check_password_hash(user["password"], password):
        return {"id": str(user["_id"]), "username": user["username"], "role": user["role"]}
    return None

def get_all_admins():
    admins = users_collection.find({"role": "admin"})
    return [{"username": admin["username"]} for admin in admins]
