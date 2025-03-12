print("This is your meal plan")
print("Explaination: For me i have three seperate meals over a day. So, I thought most of you guys are like that as well")

print("create meal file")
print("manage meal")
print("delete file")
print("view meals")

user_choice = input("Enter choices between those(create/manage/delete?view): ").lower()

def create_meal():
    try:
        with open("meal_plan.txt", 'w') as f:
            f.write("This is a Meal plan for everyday" + "\n" + 
                    "breakfast: " +"\n" + "Lunch: " + "\n" + "Dinner: " + "\n"
                    )
            print("Your meal plan has been created successfully")
    except:
        print("something has occured while creating")

def manage_meal():
    try:
        # Open the file in read mode to display the current meal plan
        with open("meal_plan.txt", 'r') as f:
            lines = f.readlines()
            print("Current Meal Plan:")
            for line in lines:
                print(line.strip())
        
        # Take user input for the meal type and details
        meal_type = input("What meal would you like to manage? (breakfast, lunch, dinner): ").lower()
        meal_detail = input(f"What details would you like to add for {meal_type}?: ")

        # Validate the meal type and update the file
        if meal_type in ["breakfast", "lunch", "dinner"]:
            with open("meal_plan.txt", "a") as f:
                f.write(f"{meal_type.capitalize()}: {meal_detail}\n")
                print(f"{meal_type.capitalize()} has been updated successfully!")
        else:
            print("Invalid meal type. Please choose from breakfast, lunch, or dinner.")

    except FileNotFoundError:
        print("The file 'meal_plan.txt' does not exist. Please create it first.")
    except Exception as e:
        print(f"An error occurred: {e}")


if user_choice == "create":
    create_meal()

if user_choice == "manage":
    manage_meal()


