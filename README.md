#  HNG Stage 0 Backend Task – Dynamic Profile Endpoint

This is my submission for the **HNG Backend Track – Stage 0 Task**.  
The task is to build a simple RESTful API endpoint (`/me`) that returns my profile information along with a **dynamic cat fact** fetched from an external API.

---

##  Features
- Returns a JSON response at `/me`
- Fetches a random cat fact dynamically from [Cat Fact Ninja API](https://catfact.ninja/fact)
- Includes current UTC timestamp in ISO 8601 format
- Handles API errors gracefully
- Clean FastAPI project structure
- Configurable via environment variables

---

##  Tech Stack
- **Language:** Python
- **Framework:** FastAPI
- **HTTP Client:** HTTPX
- **Server:** Uvicorn
- **Environment Config:** python-dotenv

---

##  Setup Instructions

### **1. Clone the repository**
```bash
git clone https://github.com/haneefojay/hng-stage0-backend.git
cd hng-stage0-backend
```
---

## 2. Create and activate a virtual environment

python -m venv venv

venv\Scripts\activate    # for Windows
or
source venv/bin/activate # for Mac/Linux

---

## 3. Install dependencies
pip install -r requirements.txt

---

## 4. Set environment variables

Create a .env file in the project root and add:

EMAIL=youremail@example.com

FULL_NAME=Your_Full_Name_Here

STACK=Your_Stack_Here

---

## 5. Run the server
uvicorn app.main:app --reload

Visit: http://127.0.0.1:8000/me

Example Response
{
  "status": "success",
  "user": {
    "email": "johndoe@gmail.com",
    "name": "John Doe",
    "stack": "Python/FastAPI"
  },
  "timestamp": "2025-10-17T08:34:59.296557+00:00",
  "fact": "Cats can rotate their ears 180 degrees."
}

---

## Project Structure

hng-stage0-backend/

│

├── app/

│   ├── main.py

│   ├── routes/

│   │   └── profile.py

│   ├── core/

│   │   ├── config.py

│   │   └── utils.py

│   └── __init__.py

│
├── .env.example

├── requirements.txt

├── .gitignore

└── README.md


---

## 🪄 Author

Name: Haneef Ojuatalyo
Email: haneefojutalayo@gmail.com

Stack: Python/FastAPI
Track: HNG Backend
