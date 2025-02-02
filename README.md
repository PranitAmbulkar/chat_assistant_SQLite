# **Company Chat Assistant**

A FastAPI-based application that interacts with an SQLite database to provide answers to employee- and department-related queries. This project demonstrates the ability to design, implement, and deploy a chat assistant with a clean and dynamic user interface.

## **Features**
- Query employee and department details using natural language.
- Supports SQL-powered dynamic responses.
- Provides a user-friendly web interface for submitting queries.
- Preloaded SQLite database with sample data.

## **Project Structure**

```
chat_assistant_SQLite/
├── Query_Results_Screenshots/    # Contains screenshots of query results
├── README.md                     # Project description and setup instructions
├── UI_chat_assistant.png         # Screenshot of the UI for reference
├── chat_assistant.db             # SQLite database file with preloaded data
├── index.html                    # HTML template for the chat interface
├── main.py                       # Main FastAPI application file
├── replit                        # Replit configuration file
├── requirements.txt              # Python dependencies required for the project
├── setup_db.py                   # Script to set up and populate the SQLite database
└── templates/                    # Directory for HTML templates (if applicable)
    └── index.html                # HTML file for the user interface
```

---

## **Setup Instructions**

### **1. Clone the Repository**
```bash
git clone https://github.com/PranitAmbulkar/chat_assistant_SQLite.git
cd chat_assistant_SQLite
```

### **2. Install Dependencies**
Make sure you have Python 3.10+ installed. Install the required Python packages:
```bash
pip install -r requirements.txt
```

### **3. Set Up the Database**
Run the `setup_db.py` file to create and populate the SQLite database:
```bash
python setup_db.py
```

### **4. Run the Application**
Start the FastAPI server:
```bash
uvicorn main:app --reload
```
The application will be available at: [http://127.0.0.1:8000](http://127.0.0.1:8000)

### **5. Access the Web Interface**
- Navigate to the `/` route (homepage) in your browser.
- Enter your query in the input box and submit.

---

## **Example Queries**
1. Show me all employees in the Sales department.
2. Who is the manager of the Marketing department?
3. Show employees hired after 2022-01-01.
4. What is the total salary expense for Engineering?

---

## **Known Limitations**
- SQL injection prevention is handled minimally.
- Error handling for database connection issues can be improved.

---

## **Demo**
### **Live Hosted Link**
[Live Demo on Replit](https://c98c246d-3758-4572-acd1-a48edcb7b3fc-00-1feochlksyh8g.sisko.replit.dev/)

---

## **Screenshots**
### **1. User Interface**
![UI](UI_chat_assistant.png)

### **2. Example Query Results**
Check the `Query_Results_Screenshots/` folder for more examples.

---

## **Contributing**
Feel free to fork this repository, make your changes, and submit a pull request. Any suggestions for improvement are welcome.

---

## **License**
This project is licensed under the MIT License.
