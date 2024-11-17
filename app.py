from flask import Flask
from routes.user_routes import user_routes
from routes.admin_routes import admin_routes
from flask_jwt_extended import JWTManager

app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = "supersecretkey"  # Replace with a secure key
jwt = JWTManager(app)

# Register blueprints
app.register_blueprint(user_routes, url_prefix="/user")
app.register_blueprint(admin_routes, url_prefix="/admin")

if __name__ == "__main__":
    app.run(debug=True)
