from pymongo import MongoClient

client = MongoClient("mongodb+srv://jrmenon31:Suraj@cluster0.ei3xf.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0") # MongoDB connection string, ensure it is updated with correct credentials (Use or Input your DB string).
db = client["cluster0"] #DB name
users_collection = db["users"]  #collection for users
assignments_collection = db["assignments"]   #collection for assignments
