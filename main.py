from fastapi import FastAPI, HTTPException, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import sqlite3
import logging
import re

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)
app = FastAPI()

# Set up the template directory for rendering HTML
templates = Jinja2Templates(directory="templates")


def execute_query(sql_query, params=()):
    logger.debug(f"Executing SQL Query: {sql_query} with params: {params}")
    connection = sqlite3.connect("chat_assistant.db")
    cursor = connection.cursor()
    try:
        cursor.execute(sql_query, params)  # Use parameterized queries
        result = cursor.fetchall()
        connection.close()
        return result
    except Exception as e:
        logger.error(f"Error executing query: {e}")
        connection.close()
        return str(e)


@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    """Render the home page with the query input form."""
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/query", response_class=HTMLResponse)
async def handle_query(request: Request, query: str = Form(...)):
    """Handle form submission and display the query results."""
    try:
        sql, params = None, ()
        query_lower = query.lower()

        if "employees in" in query_lower and "department" in query_lower:
            match = re.search(r"in\s+(?:the\s+)?(.*?)\s+department",
                              query_lower)
            if match:
                department = match.group(1).strip().capitalize()
                sql = "SELECT * FROM Employees WHERE LOWER(Department) = LOWER(?)"
                params = (department, )

        elif "manager of" in query_lower and "department" in query_lower:
            match = re.search(r"of\s+(?:the\s+)?(.*?)\s+department",
                              query_lower)
            if match:
                department = match.group(1).strip().capitalize()
                sql = "SELECT Manager FROM Departments WHERE LOWER(Name) = LOWER(?)"
                params = (department, )

        elif "hired after" in query_lower:
            date = query_lower.split("after")[1].strip()
            sql = "SELECT * FROM Employees WHERE Hire_Date > ?"
            params = (date, )

        elif "total salary" in query_lower and "department" in query_lower:
            match = re.search(r"for\s+(?:the\s+)?(.*?)\s+department",
                              query_lower)
            if match:
                department = match.group(1).strip().capitalize()
                sql = "SELECT SUM(Salary) FROM Employees WHERE LOWER(Department) = LOWER(?)"
                params = (department, )

        if sql:
            result = execute_query(sql, params)
            return templates.TemplateResponse("index.html", {
                "request": request,
                "result": result
            })
        else:
            return templates.TemplateResponse(
                "index.html", {
                    "request": request,
                    "error": "Invalid query. Please try again."
                })
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
