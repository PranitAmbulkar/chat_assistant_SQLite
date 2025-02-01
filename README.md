# 📝 Chat Assistant API (FastAPI + SQLite)
A chatbot assistant that interacts with an SQLite database to retrieve employee details, department managers, and salary-related queries.

---

## 🚀 **Live Demo**
🔗 **Hosted API**: [Replit URL](https://c98c246d-3758-4572-acd1-a48edcb7b3fc-00-1feochlksyh8g.sisko.replit.dev/)  
📄 **Swagger UI Docs**: [API Docs](https://c98c246d-3758-4572-acd1-a48edcb7b3fc-00-1feochlksyh8g.sisko.replit.dev/docs)  

---

## 📌 **Features**
✅ Fetch employees by department  
✅ Get the manager of a department  
✅ List employees hired after a given date  
✅ Calculate total salary expenses for a department  
✅ FastAPI interactive Swagger UI  

---

## 🏗 **Project Structure**
```
/chat-assistant
│── main.py              # FastAPI application
│── setup_db.py          # Database setup script
│── chat_assistant.db    # SQLite database file
│── requirements.txt     # Python dependencies
│── README.md            # Project documentation
│── .replit              # Replit configuration (if hosted on Replit)
```

---

## 📦 **Installation & Setup**
### **1️⃣ Clone the Repository**
```bash
git clone https://github.com/your-username/chat-assistant.git
cd chat-assistant
```

### **2️⃣ Install Dependencies**
```bash
pip install -r requirements.txt
```

### **3️⃣ Initialize the Database**
```bash
python setup_db.py
```
This will create an SQLite database (`chat_assistant.db`) and populate it with sample employee and department data.

### **4️⃣ Run the FastAPI Server**
```bash
uvicorn main:app --host=0.0.0.0 --port=8000
```

### **5️⃣ Access API Documentation**
Open your browser and visit:
```
http://127.0.0.1:8000/docs
```

---

## 🛠 **API Endpoints**

### **1️⃣ Root Endpoint (`/`)**
🔹 **Method**: `GET`  
🔹 **Response**: Welcome message  

📌 **Example Request**
```bash
curl http://127.0.0.1:8000/
```
📌 **Response**
```json
{
  "message": "Welcome to the SQLite Chat Assistant"
}
```

---

### **2️⃣ Query Endpoint (`/query`)**
🔹 **Method**: `POST`  
🔹 **Request Body**: `{ "query": "<your-query>" }`  
🔹 **Response**: Query results  

📌 **Supported Queries**
- `"Show me all employees in the Sales department."`
- `"Who is the manager of the Engineering department?"`
- `"List all employees hired after 2021-01-01."`
- `"What is the total salary expense for the Marketing department?"`

📌 **Example Request**
```bash
curl -X POST "http://127.0.0.1:8000/query" -H "Content-Type: application/json" -d '{"query": "Show me all employees in the Sales department."}'
```
📌 **Response**
```json
{
  "result": [
    [1, "Alice", "Sales", 50000, "2021-01-15"],
    [5, "Eve", "Sales", 55000, "2021-07-01"],
    [8, "Hank", "Sales", 52000, "2022-11-10"],
    [10, "Jack", "Sales", 57000, "2023-05-18"]
  ]
}
```

---

## 📂 **Database Schema**
The database contains two tables:

### **1️⃣ Employees Table**
| ID  | Name     | Department   | Salary | Hire_Date   |
|------|----------|--------------|--------|-------------|
| 1    | Alice    | Sales        | 50000  | 2021-01-15  |
| 2    | Bob      | Engineering  | 70000  | 2020-06-10  |
| 3    | Charlie  | Marketing    | 60000  | 2022-03-20  |

📌 **Create Table SQL**
```sql
CREATE TABLE Employees (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Name TEXT NOT NULL,
    Department TEXT NOT NULL,
    Salary INTEGER NOT NULL,
    Hire_Date DATE NOT NULL
);
```

---

### **2️⃣ Departments Table**
| ID  | Name         | Manager   |
|------|--------------|-----------|
| 1    | Sales        | Alice     |
| 2    | Engineering  | Bob       |

📌 **Create Table SQL**
```sql
CREATE TABLE Departments (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Name TEXT NOT NULL,
    Manager TEXT NOT NULL
);
```

---

## 🌍 **Hosting the API Online**
### **🚀 Deployment on Replit**
1. **Upload all files (`main.py`, `setup_db.py`, `chat_assistant.db`, etc.).**
2. **Modify `.replit` File:**
   ```ini
   run = "uvicorn main:app --host=0.0.0.0 --port=8000"
   ```
3. **Click "Run" and Copy the Public URL.**
4. **Keep Your API Running Longer:**  
   - Use [UptimeRobot](https://uptimerobot.com/) to ping your URL every 5 minutes

## ⚠️ **Known Limitations & Future Improvements**
### **🚨 Current Limitations**
- Database is limited to **predefined queries** (e.g., no free-text AI processing).
- The API does **not handle real-time updates** (requires manual DB refresh).

### **🔮 Future Enhancements**
✅ Integrate with **LLMs (like OpenAI GPT-4)** for natural language understanding.  
✅ Move from **SQLite → PostgreSQL** for scalability.  
✅ Add **authentication (JWT tokens)** to restrict acce
For support, feel free to raise an issue in the **GitHub repository** or reach out to me. 🚀
