# FastAPI MongoDB Todo Application

This repository contains a basic CRUD API application built with FastAPI and MongoDB. The application allows you to create, read, update, and delete todo tasks.

# Features
Create Todo: Add new tasks.
Read Todos: Retrieve all tasks.
Update Todo: Modify existing tasks.
Delete Todo: Soft delete tasks (mark as deleted).

# Copy code
git clone https://github.com/yourusername/fastapi-mongodb-todo.git
cd fastapi-mongodb-todo
Create and activate a virtual environment:
bash
Copy code
```
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`\

```
# Install dependencies:
bash
Copy code
pip install -r requirements.txt
Configure MongoDB:

Update the MongoDB connection URI in the configurations.py file:
Copy code
```
uri = "mongodb+srv://<username>:<password>@cluster0.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
```
Replace <username> and <password> with your MongoDB Atlas credentials.

Running the Application
bash
Copy code
```
uvicorn main:app --reload
```
The application will be available at http://127.0.0.1:8000.

# API Endpoints
Get All Todos
URL: /
Method: GET
Response: List of all todos
Create a Todo
URL: /
Method: POST
Request Body:
json
Copy code
```
{
    "title": "string",
    "description": "string",
    "is_completed": false,
    "is_deleted": false
}
```
Response: Created todo ID
Update a Todo
URL: /{task_id}
Method: PUT
Request Body:
json
Copy code
```
{
    "title": "string",
    "description": "string",
    "is_completed": false,
    "is_deleted": false
}
```
Response: Success message
Directory Structure
bash
Copy code
```
fastapi-mongodb-todo/
├── configurations.py  # MongoDB configuration
├── database/
│   ├── models.py      # Pydantic models
│   ├── schemas.py     # MongoDB document schemas
├── main.py            # Main FastAPI application
└── README.md          # This file
```
License
This project is licensed under the MIT License.

Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Contact
For any questions or issues, please open an issue in the repository.
