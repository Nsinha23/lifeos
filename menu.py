import sqlite3
from habits import add_habit, show_habits, delete_habit
from ai import get_motivation

conn = sqlite3.connect("lifeos.db")
cursor = conn.cursor()


print ("Welcome to LifeOS!")
motivation = get_motivation()
print(motivation)


while True: 
    print("Please select 1: Add habit, 2: show habits, 3: Delete habit, 4: EXIST") 
    press_value = input("entervalue here ")

    if press_value == "1": 
        print (" You can add habits") 
        add_habit(cursor, conn)

    elif press_value == "2": 
        print ("Here is the list of your habits") 
        show_habits(cursor)

    elif press_value == "3": 
        print (" Deleting habit") 
        delete_habit(cursor, conn)

    else: 
        print ("BBye") 
        break
