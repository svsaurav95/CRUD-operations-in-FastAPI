from fastapi import FastAPI, APIRouter, HTTPException
from configurations import collection
from database.schemas import all_tasks
from database.models import todo
from bson.objectid import ObjectId
from datetime import datetime

app = FastAPI()
router = APIRouter()

@router.get("/")
async def get_all_todos():
    data = collection.find({"is_deleted":False})
    return all_tasks(data)

@router.post("/")
async def create_task(new_task: todo):
    try:
        resp = collection.insert_one(dict(new_task))
        return {"status_code": 200, "id": str(resp.inserted_id)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Some error occurred: {e}")

@router.put("/{task_id}")
async def update_task(task_id: str, updated_task: todo):
    try:
        id = ObjectId(task_id)
        existing_doc = collection.find_one({"_id": id, "is_deleted": False})
        if not existing_doc:
            raise HTTPException(status_code=404, detail="Task does not exist")
        updated_task.updated_at = int(datetime.timestamp(datetime.now()))
        resp = collection.update_one({"_id": id}, {"$set": dict(updated_task)})
        return {"status_code": 200, "message": "Task updated successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Some error occurred: {e}")


@router.delete("/{task_id}")
async def delete_task(task_id: str):
    try:
        id = ObjectId(task_id)
        existing_doc = collection.find_one({"_id": id, "is_deleted": False})
        if not existing_doc:
            raise HTTPException(status_code=404, detail="Task does not exist")
        resp = collection.update_one({"_id": id}, {"$set":{"is_deleted": True}})
        return {"status_code": 200, "message": "Task updated successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Some error occurred: {e}")






app.include_router(router)
