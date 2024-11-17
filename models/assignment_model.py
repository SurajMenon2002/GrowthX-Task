from config import assignments_collection
from datetime import datetime
from bson import ObjectId

# Function to upload an assignment
def upload_assignment(user_id, task, admin):
    try:
        assignment = {
            "userId": user_id,
            "task": task,
            "admin": admin,
            "status": "pending",
            "timestamp": datetime.utcnow()  
        }
        assignments_collection.insert_one(assignment)
        return {"message": "Assignment uploaded successfully"}
    except Exception as e:
        return {"error": f"Error uploading assignment: {str(e)}"}

# Function to get all assignments for a specific admin
def get_assignments_for_admin(admin):
    try:
        assignments = assignments_collection.find({"admin": admin})
        return [
            {"id": str(a["_id"]), "userId": a["userId"], "task": a["task"], "status": a["status"], "timestamp": a["timestamp"]}
            for a in assignments
        ]
    except Exception as e:
        return {"error": f"Error fetching assignments: {str(e)}"}

# Function to update the status of an assignment (accept or reject)
def update_assignment_status(assignment_id, status):
    try:
        # Convert assignment_id to ObjectId if it's a string
        if isinstance(assignment_id, str):
            assignment_id = ObjectId(assignment_id)
        
        assignment = assignments_collection.find_one({"_id": assignment_id})
        
        if not assignment:
            return {"error": "Assignment not found"}
        
        if assignment["status"] != "pending":
            return {"error": "Assignment already processed"}
        
        # Update the status of the assignment
        result = assignments_collection.update_one({"_id": assignment_id}, {"$set": {"status": status}})
        
        if result.modified_count == 1:
            return {"message": f"Assignment {status} successfully"}
        return {"error": "Assignment not found or already updated"}
    except Exception as e:
        return {"error": f"Error updating assignment status: {str(e)}"}
