import mysql.connector
from contextlib import contextmanager

@contextmanager
def get_db_cursor(commit=False):
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="12345678",
        database="expense_manager"
    )

    cursor = connection.cursor()
    yield cursor

    if commit:
        connection.commit()

    cursor.close()
    connection.close()

def fetch_all_expenses():
    with get_db_cursor() as cursor:
        cursor.execute("SELECT * FROM expenses")
        expenses = cursor.fetchall()

        for expense in expenses:
            print(expense)

def fetch_expense_by_date(date):
    with get_db_cursor() as cursor:
        cursor.execute("SELECT * from expenses WHERE expense_date=%s", (date,))
        expenses = cursor.fetchall()

        for expense in expenses:
            print(expense)

def insert_expense(expense_date, amount, category, notes):
    with get_db_cursor(commit=True) as cursor:
        cursor.execute("INSERT INTO expenses(expense_date, amount, category, notes) VALUES (%s,%s,%s,%s)",
        (expense_date, amount, category, notes))

def delete_expense_by_date(date):
    with get_db_cursor(commit=True) as cursor:
        cursor.execute("DELETE FROM expenses WHERE expense_date=%s",(date,))

if __name__ == "__main__":
    #fetch_all_expenses()
    #fetch_expense_date("2024-08-01")

    insert_expense("2024-12-22", 120, "Food", "Nila")

    print("Before deleting")
    fetch_expense_by_date("2024-12-22")

    delete_expense_by_date("2024-12-22")

    print("After deleting:")
    fetch_expense_by_date("2024-12-22")
