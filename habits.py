habits = []

def add_habit():
    user_input = input("Enter habit name: ")
    habits.append(user_input)
    print("✅ Habit added! Your habits:", habits)

def show_habits():
    if len(habits) == 0:
        print("no habits yet")
    else:
        for n in habits:
            print(n)

add_habit() 
add_habit()
show_habits()