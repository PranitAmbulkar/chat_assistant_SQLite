from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import sqlite3
import logging
import re

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

app = FastAPI()


class Query(BaseModel):
    query: str


def execute_query(sql_query, params=()):
    import logging
    logging.basicConfig(level=logging.DEBUG)
    logger = logging.getLogger(__name__)

    logger.debug(f"Executing SQL Query: {sql_query} with params: {params}")
    connection = sqlite3.connect("chat_assistant.db")
    cursor = connection.cursor()
    try:
        cursor.execute(sql_query,
                       params)  # Use params for parameterized queries
        result = cursor.fetchall()
        connection.close()
        return result
    except Exception as e:
        logger.error(f"Error executing query: {e}")
        connection.close()
        return str(e)


@app.get("/")
def read_root():
    return {"message": "Welcome to the SQLite Chat Assistant"}


@app.post("/query")
def handle_query(query: Query):
    try:
        # Handle "Show me all employees in [the] [department] department."
        if "employees in" in query.query.lower(
        ) and "department" in query.query.lower():
            # Regex to extract the department name, handling optional "the"
            match = re.search(r"in\s+(?:the\s+)?(.*?)\s+department",
                              query.query.lower())
            if match:
                department = match.group(1).strip().capitalize(
                )  # Extract and capitalize department name
                sql = "SELECT * FROM Employees WHERE LOWER(Department) = LOWER(?)"
                params = (department, )
            else:
                return {
                    "error": "Invalid query format. Please check your input."
                }

        # Handle "Who is the manager of [the] [department] department?"
        elif "manager of" in query.query.lower(
        ) and "department" in query.query.lower():
            match = re.search(r"of\s+(?:the\s+)?(.*?)\s+department",
                              query.query.lower())
            if match:
                department = match.group(1).strip().capitalize()
                sql = "SELECT Manager FROM Departments WHERE LOWER(Name) = LOWER(?)"
                params = (department, )
            else:
                return {
                    "error": "Invalid query format. Please check your input."
                }

        # Handle "List all employees hired after [date]."
        elif "hired after" in query.query.lower():
            date = query.query.lower().split("after")[1].strip()
            sql = "SELECT * FROM Employees WHERE Hire_Date > ?"
            params = (date, )

        # Handle "What is the total salary expense for [the] [department] department?"
        elif "total salary" in query.query.lower(
        ) and "department" in query.query.lower():
            match = re.search(r"for\s+(?:the\s+)?(.*?)\s+department",
                              query.query.lower())
            if match:
                department = match.group(1).strip().capitalize()
                sql = "SELECT SUM(Salary) FROM Employees WHERE LOWER(Department) = LOWER(?)"
                params = (department, )
            else:
                return {
                    "error": "Invalid query format. Please check your input."
                }

        else:
            return {"error": "Invalid query. Please try again."}

        # Execute the SQL query
        result = execute_query(sql, params)
        if not result:
            return {"message": "No results found."}
        return {"result": result}

    except Exception as e:
        return {"error": str(e)}
