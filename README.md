# Table of Contents
1. Required Python Packages
2. MongoDB Setup
3. Running the Application
4. Accessing the Application:
5. API Endpoints
  - User Routes
  - Admin Routes
6. Postman Setup
7. Adding JWT Token in Postman

# Required Python Packages
To install the required Python packages, run the following:
```
pip install -r requirements.txt

```
# MongoDB Setup
In config.py, change the MongoDB URI to use your credentials:
```
client = MongoClient("mongodb+srv://your_username:your_password@cluster0.ei3xf.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

```
# Running the Application
1. Running the Flask Application:
```
python app.py

```
This will start the Flask development server on http://127.0.0.1:5000/.

# Accessing the Application:

The application exposes two main route groups:

* /user: For user actions (registration, login, assignment upload)
* /admin: For admin actions (registration, login, assignment review and status update)
These routes will be available once the application is running.

# API Endpoints
# User Routes (/user)
1. Register User (POST /user/register):
```
{
  "username": "john_doe",
  "password": "password123"
}

```
2. Login User (POST /user/login):
```
{
  "username": "john_doe",
  "password": "password123"
}

```
3. Upload Assignment (POST /user/upload):
   - Headers: Include the JWT token in the Key(Authorization) Value(Bearer <token>).   
```
{
  "task": "Complete the Flask project",
  "admin": "admin_user"
}

```
4. Get Admins (GET /user/admins):
   - Returns a list of all admin usernames for the user to select from when uploading an assignment.
```
(GET /user/admins):

```

# Admin Routes (/admin)

1. Register Admin (POST /admin/register):
```
{
  "username": "admin_user",
  "password": "admin123"
}

```
2. Login Admin (POST /admin/login):
```
{
  "username": "admin_user",
  "password": "admin123"
}

```

3. Get Assignments (GET /admin/assignments):
   - Headers: Include the JWT token in the Authorization header (Bearer token).
   - Returns: A list of assignments assigned to the admin.
     
4. Update Assignment Status (POST /admin/assignments/<assignment_id>/<status>):
   - Headers: Include the JWT token in the Authorization header (Bearer token).
   - Body: No body required.
   - Path Parameters: assignment_id (ID of the assignment to update), status (new status of the assignment, e.g., accepted or rejected).

# Postman Setup
1. Test Data: Use the provided test_data.json to set up test cases in Postman. You can import this file into Postman for easy testing.
2. User Registration and Login:
   - For registration, send a POST request to http://127.0.0.1:5000/user/register with the necessary username and password.
   - For login, send a POST request to http://127.0.0.1:5000/user/login and get the JWT token.
3. User Upload Assignment:
   - Include the JWT token in the Authorization header as a Bearer token.
   - Send a POST request to http://127.0.0.1:5000/user/upload with the task and admin details in the body.
4. Admin Actions:
   - For admin registration and login, send requests to the /admin/register and /admin/login endpoints.
   - For getting assignments, send a GET request to /admin/assignments with the admin's JWT token.
   - For updating assignment status, send a POST request to /admin/assignments/<assignment_id>/<status> with the appropriate assignment_id and status.
  
# Adding JWT Token in Postman

After logging in either as a user or admin, copy the JWT token from the response and add it as a Bearer token in the Authorization tab of your Postman request.



























