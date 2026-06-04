import sqlite3

conn = sqlite3.connect("lifeos.db")
cursor = conn.cursor()

def add_habit():
    user_input = input("Enter habit name: ")
    cursor.execute("INSERT INTO habits (name) VALUES (?)", (user_input,))
    conn.commit()
    print("✅ Habit saved to database!")

def show_habits():
    cursor.execute("SELECT * FROM habits")
    habits = cursor.fetchall()
    for habit in habits:
        print("→", habit[1])

def delete_habit():
    user_input = input("Which id would you like to delete? ")
    cursor.execute("DELETE FROM habits WHERE id = ?", (user_input,))
    conn.commit()
    print("✅ Habit deleted!")

add_habit()
add_habit()
show_habits()
delete_habit()
show_habits()