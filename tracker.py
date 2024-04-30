#this code is in progress. 
#this program is intended to track and view habit progress for users

def track_habits():
    habits = {}
    habit_history = {}

    print("\nWelcome to Happy Habits Builder!")
    
    while True:
        print("\n1. Add new habit")
        print("2. Remove old habit")
        print("3. Mark habit as completed")
        print("4. Mark habit as missed.")
        print("5. View habits tracking.")
        print("6. View Habit Progress.")
        print("7. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            habit = input("Enter the habit you want to add: ")
            habits[habit] = False
            print(f"\n{habit} added to your habits.")
            
        elif choice == '2':
            if not habits:
                print("You have no habits to remove.")
            else:
                print("/nYour habits:")
                for i, habit in enumerate(habits.keys(), start=1):
                    print(f"{i}. {habit}")
                index = int(input("Enter the index of the habit you want to remove: "))
                habit_to_remove = list(habits.keys())[index - 1]
                del habits[habit_to_remove]
                print(f"{habit_to_remove} removed from your habits.")

        elif choice == '3':
            if not habits:
                print("You have no habits to mark as completed.")
            else:
                print("\nYour habits:")
                for i, habit in enumerate(habits.keys(), start=1):
                    print(f"{i}. {habit}")
                index = int(input("Enter the index of the habit you want to mark as completed: "))
                habit_to_mark = list(habits.keys())[index - 1]
                habits[habit_to_mark] = True
                print(f"{habit_to_mark} marked as completed. Way to go!")

        elif choice == '4':
            if not habits:
                print("\nYou have no habits to mark as missed.")
            else:
                print("\nYour habits:")
                for i, habit in enumerate(habits.keys(), start=1):
                    print(f"{i}. {habit}")
                index = int(input("Enter the index of the habit you want to mark as missed: "))
                habit_to_mark = list(habits.keys())[index - 1]
                habits[habit_to_mark] = False
                print(f"{habit_to_mark} marked as missed. Don't give up!")
                
        elif choice == '5':
            if not habits:
                print("You have no habits to view.")
            else:
                print("\nYour habits:")
                for habit, completed in habits.items():
                    status = "completed" if completed else "not completed"
                    print(f"- {habit}: {status}")

        elif choice == '6':
            if not habit_history:
                print("\nNo habits tracked yet.")
            else:
                habit = input("Enter the habit you want to see your progress for: ")
                if habit in habit_history:
                    consistency = sum(habit_history[habit]) / len(habit_history[habit]) * 100
                    print(f"Consistency for '{habit}': {consistency:.2f}%")
                else:
                    print("Habit not found. Please enter a valid habit.")
                
        elif choice == '7':
            print("Exiting program. Keep up the good work!")
            break
            
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    track_habits()