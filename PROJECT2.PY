import json
import os
from datetime import date

DATA_FILE = "habits.json"


def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return {}


def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)


def add_habit(habit_name):
    data = load_data()
    if habit_name not in data:
        data[habit_name] = []
        print(f"✅ Habit '{habit_name}' added!")
    else:
        print(f"⚠ Habit '{habit_name}' already exists.")
    save_data(data)


def mark_done(habit_name):
    data = load_data()
    today = str(date.today())
    if habit_name in data:
        if today not in data[habit_name]:
            data[habit_name].append(today)
            print(f"✔ Marked '{habit_name}' as done for today!")
        else:
            print(f"⚠ '{habit_name}' is already marked for today.")
    else:
        print("❌ Habit not found.")
    save_data(data)


def show_progress():
    data = load_data()
    today = str(date.today())
    if not data:
        print("No habits found. Add one first!")
        return
    print("\n📊 Your Habit Progress:")
    for habit, dates in data.items():
        status = "✅ Done" if today in dates else "❌ Not Done"
        print(f"- {habit}: {status} ({len(dates)} days total)")


def main():
    while True:
        print("\n--- Daily Habit Tracker ---")
        print("1. Add Habit")
        print("2. Mark Habit as Done")
        print("3. Show Progress")
        print("4. Exit")

        choice = input("Enter your choice: ")
        
        if choice == "1":
            habit = input("Enter habit name: ")
            add_habit(habit)
        elif choice == "2":
            habit = input("Enter habit name: ")
            mark_done(habit)
        elif choice == "3":
            show_progress()
        elif choice == "4":
            print("Goodbye! Keep building your habits 🚀")
            break
        else:
            print("Invalid choice, try again.")
if__name__ ="main"
main()