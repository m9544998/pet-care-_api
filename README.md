# pet-care_api
 # Pet Care Management API

A RESTful API built using **Flask** and **SQLite** to manage pet records.

This project allows users to add pets, view all pets, get pet details by ID, and delete pet records. It is a beginner-friendly backend project for learning Flask REST APIs and SQLite.

---

#  Project Overview

The Pet Care Management API helps store and manage pet information in a database. It demonstrates CRUD operations, input validation, reusable database connections, and error handling using Flask and SQLite.

---

# Features

* Add Pet
* View All Pets
* Get Pet By ID
* Delete Pet
* Input Validation
* Error Handling
* JSON Responses
* SQLite Database

---

#  Technologies Used

* Python 3
* Flask
* SQLite3
* REST API
* JSON

---

# Project Structure

```text
pet-care-management-api/
│
├── app.py
├── pets.db
├── README.md
└── requirements.txt
```

---

# Installation

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/pet-care-management-api.git
```

### 2. Open the Project Folder

```bash
cd pet-care-management-api
```

### 3. Install Flask

```bash
pip install flask
```

### 4. Run the Project

```bash
python app.py
```

Server will start at:

```text
http://127.0.0.1:5000
```

---

#  Database Schema

```sql
CREATE TABLE pets(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    pet_name TEXT NOT NULL,
    pet_type TEXT NOT NULL
);
```

---

# API Endpoints

| Method | Endpoint   | Description   |
| ------ | ---------- | ------------- |
| POST   | /pets      | Add Pet       |
| GET    | /pets      | View All Pets |
| GET    | /pets/<id> | Get Pet By ID |
| DELETE | /pets/<id> | Delete Pet    |

---

# Add Pet

### Request

```json
{
    "pet_name": "Tom",
    "pet_type": "Cat"
}
```

### Response

```json
{
    "message": "Pet added successfully",
    "pet_id": 1
}
```

---

# View All Pets

### Request

```http
GET /pets
```

### Response

```json
[
    {
        "id": 1,
        "pet_name": "Tom",
        "pet_type": "Cat"
    }
]
```

---

# Get Pet By ID

### Request

```http
GET /pets/1
```

### Response

```json
{
    "id": 1,
    "pet_name": "Tom",
    "pet_type": "Cat"
}
```

---

# Delete Pet

### Request

```http
DELETE /pets/1
```

### Response

```json
{
    "message": "Pet deleted successfully"
}
---

#  Learning Outcomes

By completing this project, you will learn:

* Flask Routing
* CRUD Operations
* SQLite Database Integration
* REST API Development
* JSON Request & Response
* Backend Project Structure

---

# Future Improvements

* Update Pet Information
* Owner Name
* Pet Age
* Vaccination Status
* Search Pet by Name
* Pet Breed
* Pet Gender
* Appointment History

---

# Author

**Maheen Asad**

Learning Flask • SQLite • REST API Development

---

 If you like this project, give it a on GitHub and continue building more Flask + SQLite projects!




       
