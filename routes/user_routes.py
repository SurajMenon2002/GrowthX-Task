from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from models.user_model import create_user, authenticate_user, get_all_admins
from models.assignment_model import upload_assignment

user_routes = Blueprint("user_routes", __name__)

@user_routes.route("/register", methods=["POST"])  # User registration route
def register_user():
    data = request.json
    return jsonify(create_user(data["username"], data["password"], "user"))

@user_routes.route("/login", methods=["POST"])  # User login route to authenticate and generate JWT token
def login_user():
    data = request.json
    user = authenticate_user(data["username"], data["password"])
    if user:
        token = create_access_token(identity={"username": user["username"], "role": user["role"]})
        return jsonify({"token": token})
    return jsonify({"error": "Invalid credentials"}), 401

@user_routes.route("/upload", methods=["POST"])  # Route to upload assignment (user can upload tasks)
@jwt_required() 
def upload():
    identity = get_jwt_identity()
    if identity["role"] != "user":
        return jsonify({"error": "Unauthorized"}), 403
    data = request.json
    return jsonify(upload_assignment(identity["username"], data["task"], data["admin"]))

@user_routes.route("/admins", methods=["GET"])
def get_admins():
    return jsonify(get_all_admins())
