
def add_habit(cursor, conn):
    user_input = input("Enter habit name: ")
    cursor.execute("INSERT INTO habits (name) VALUES (?)", (user_input,))
    conn.commit()
    print("✅ Habit saved!")

def show_habits(cursor):
    cursor.execute("SELECT * FROM habits")
    habits = cursor.fetchall()
    for habit in habits:
        print("→", habit[1])

def delete_habit(cursor, conn):
    show_habits(cursor)
    user_input = input("Which id to delete? ")
    cursor.execute("DELETE FROM habits WHERE id = ?", (user_input,))
    conn.commit()
    print("✅ Habit deleted!")




