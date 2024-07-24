import sqlite3
import pandas as pd

# Connect to the database
conn = sqlite3.connect('assignment.db')
cursor = conn.cursor()

# #function to print the databse
# def print_database():
#     cursor.execute("SELECT name, marks FROM students")
#     rows = cursor.fetchall()

#     if rows:
#         print("Database Contents:")
#         for row in rows:
#             name, marks = row
#             print(f"Name: {name}, Marks: {marks}")
#     else:
#         print("The database is empty.")


# Function to print all records in the database as a DataFrame USING PANDAS 
def print_database():
    cursor.execute("SELECT name, marks FROM students")
    rows = cursor.fetchall()

    if rows:
        df = pd.DataFrame(rows, columns=['Name', 'Marks'])
        print("\nDatabase Contents:")
        print(df.to_string(index=False))
    else:
        print("The database is empty.")


# Function to perform the search and display results
def search_students(search_str):
    # Perform case-insensitive search
    cursor.execute("SELECT name, marks FROM students WHERE name LIKE ?", ('%' + search_str + '%',))
    rows = cursor.fetchall()

    if rows:
        total_marks = 0
        print("\nSearch Results:")
        for row in rows:
            name, marks = row
            total_marks += marks
            print(f"Name: {name}, Marks: {marks}")

        average_marks = total_marks / len(rows)
        print(f"\nTotal Marks: {total_marks}")
        print(f"Average Marks: {average_marks:.2f}")
    else:
        print("No results found.")


search_str = input("Enter search string: ").strip()
print_database()
if not search_str:
    print("Please enter a search string")
else:
    search_students(search_str)


# Close the connection
conn.close()