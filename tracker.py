def track_habits():
    habits = {}
    
    while True:
        print("\n1. Add habit")
        print("2. Remove habit")
        print("3. Mark habit as completed")
        print("4. Mark habit as missed.")
        print("5. View habits")
        print("6. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            habit = input("Enter the habit you want to add: ")
            habits[habit] = False
            print(f"{habit} added to your habits.")
            
        elif choice == '2':
            if not habits:
                print("You have no habits to remove.")
            else:
                print("Your habits:")
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
                print("Your habits:")
                for i, habit in enumerate(habits.keys(), start=1):
                    print(f"{i}. {habit}")
                index = int(input("Enter the index of the habit you want to mark as completed: "))
                habit_to_mark = list(habits.keys())[index - 1]
                habits[habit_to_mark] = True
                print(f"{habit_to_mark} marked as completed. Way to go!")
                
        elif choice == '5':
            if not habits:
                print("You have no habits to view.")
            else:
                print("Your habits:")
                for habit, completed in habits.items():
                    status = "completed" if completed else "not completed"
                    print(f"- {habit}: {status}")
                
        elif choice == '6':
            print("Exiting. Keep up the good work!")
            break
            
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    track_habits()