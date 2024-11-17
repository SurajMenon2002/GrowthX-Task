from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from models.user_model import create_user, authenticate_user
from models.assignment_model import get_assignments_for_admin, update_assignment_status

admin_routes = Blueprint("admin_routes", __name__)

# Admin registration route (to create a new admin)
@admin_routes.route("/register", methods=["POST"])
def register_admin():
    data = request.json
    return jsonify(create_user(data["username"], data["password"], "admin"))

# Admin login route to authenticate and generate JWT token
@admin_routes.route("/login", methods=["POST"])
def login_admin():
    data = request.json
    admin = authenticate_user(data["username"], data["password"])
    if admin:
        token = create_access_token(identity={"username": admin["username"], "role": admin["role"]})
        return jsonify({"token": token})
    return jsonify({"error": "Invalid credentials"}), 401


@admin_routes.route("/assignments", methods=["GET"])  # Route to get all assignments for admin
@jwt_required()
def get_assignments():
    identity = get_jwt_identity()
    if identity["role"] != "admin":
        return jsonify({"error": "Unauthorized"}), 403
    return jsonify(get_assignments_for_admin(identity["username"]))

@admin_routes.route("/assignments/<assignment_id>/<status>", methods=["POST"])   # Route to update assignment status (accept/reject) by admin 
@jwt_required()
def update_status(assignment_id, status):
    identity = get_jwt_identity()
    if identity["role"] != "admin":
        return jsonify({"error": "Unauthorized"}), 403
    return jsonify(update_assignment_status(assignment_id, status))
