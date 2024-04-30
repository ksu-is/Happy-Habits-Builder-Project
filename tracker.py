#this code is in progress. 
#this program is intended to track and view habit progress for users

def track_habits():
    habits = {}
    habit_history = {}

    print("\nWelcome to Happy Habits Builder!\nLet's get back to tracking. Select from the choices below.")
    
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
            frequency = input("Enter how often you'd like to complete this habit (e.g., daily, weekly, monthly): ")
            habits[habit] = {'completed': False, 'frequency': frequency, 'progress': []}
            print(f"\n'{habit}' added to your habits with a frequency of {frequency}.")
            
        elif choice == '2':
            if not habits:
                print("You have no habits to remove.")
            else:
                print("\nYour habits:")
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
                habits[habit_to_mark]['completed'] = True
                habits[habit_to_mark]['progress'].append(True)
                print(f"'{habit_to_mark}' marked as completed. Way to go!")

        elif choice == '4':
            if not habits:
                print("\nYou have no habits to mark as missed.")
            else:
                print("\nYour habits:")
                for i, habit in enumerate(habits.keys(), start=1):
                    print(f"{i}. {habit}")
                index = int(input("Enter the index of the habit you want to mark as missed: "))
                habit_to_mark = list(habits.keys())[index - 1]
                habits[habit_to_mark]['completed'] = False
                habits[habit_to_mark]['progress'].append(False)
                print(f"'{habit_to_mark}' marked as missed. Don't give up!")
                
        elif choice == '5':
            if not habits:
                print("You have no habits to view.")
            else:
                print("\nYour habits:")
                for habit_name, habit_info in habits.items():
                    status = "completed" if habit_info['completed'] else "not completed"
                    print(f"- '{habit_name}': {status}, Frequency: {habit_info['frequency']}")

        elif choice == '6':
            if not habits:
                print("\nYou have no habits to track progress for.")
            else:
                habit_name = input("Enter the habit you want to see your progress for: ")
                if habit_name in habits:
                    frequency = habits[habit_name]['frequency']
                    progress = habits[habit_name]['progress']
                    completed_count = sum(progress)
                    total_count = len(progress)
                    if total_count == 0:
                        consistency = 0
                    else:
                        consistency = (completed_count / total_count) * 100
                    print(f"You completed '{habit_name}' {completed_count} times out of {total_count} attempts ({consistency:.2f}% consistency). Frequency: {frequency}")
                else:
                    print("Habit not found. Please enter a valid habit.")
                
        elif choice == '7':
            print("Exiting program. Keep up the good work!")
            break
            
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    track_habits()