import os           

def create_file():
            try:
                with open('To_do_list.txt', 'w') as f:
                    f.write("This is a To do list!")
                    print("The To-do-list is created successfully")
            except IOError:
                print("Error occured when creating the list file")

def add_hobbies():
        useradd_choice = input("Add your thing to do!: ")
        hobbie_to_do = useradd_choice.split('\n')
        if useradd_choice.isdigit():
          print("You can't add numbers here")
        try:
               with open('To_do_list.txt', 'a') as f:
                    f.write(useradd_choice+ '\n' )
                    print(f"You have added {hobbie_to_do} to the list")
                
        except FileNotFoundError:
                print("Find has not been created")

def view_hobbies():
        try:
            file_path = os.path.join(os.getcwd(), 'To_do_list.txt')
            with open(file_path, 'r') as f:
              lines = f.readlines()
              for line in lines:
                    print(line.strip())
        except FileNotFoundError:
              print("File has not been found")

def remove_hobbies():
    file_path = os.path.join(os.getcwd(), 'To_do_list.txt')
    hobby_to_remove = input("What hobby would you like to remove: ")
    try:
        with open(file_path, 'r') as f:
            lines = f.readlines()
            update_lines = [line for line in lines if line.strip() != hobby_to_remove]
            with open(file_path, 'w') as f:
                f.writelines(update_lines)
        print(f"You have removed {hobby_to_remove} from the list")
    except FileNotFoundError:
            print("File does not exist")

def markdone_hobbies():
    file_path = os.path.join(os.getcwd(), 'To_do_list.txt')
    try:
        with open(file_path, 'r') as f:
            lines = f.readlines()
            for line in lines:
                print(line.strip())
    except FileNotFoundError:
         print("file does not exist")
    hobby_to_mark = input("What hobby would you mark?: ")
    try:
        hobby_done = False
        with open(file_path, 'w'
        '') as f:
            for line in lines:
             if hobby_to_mark in line and " [Done!] " not in line:
                  f.write(line.strip() + " [Done!] ")
                  hobby_done = True
             else:
                ("not such option exists")
        if hobby_done ==True:
                print(f"You have marked {hobby_to_mark} as Done")
        
    except FileNotFoundError:
        print("file does not exist")
      


def __main__():
    while True:
        print("\n")
        print("Welcome to your to do list")
        print("\n")
        print("You must create a file first and it's easy(select create a file)")
        print("\n")

        print("create file")
        print("Add hobbie")
        print("Remove")
        print("View")
        print("Mark")
        print("exit") 
        print("\n")
        choice = input("Enter your choice between the 5!: ").lower()

        if choice == "create file":
            create_file()

        elif choice == "add hobbie":
            add_hobbies()

        elif choice == "view":
            view_hobbies()
        elif choice == "exit":
            quit()
        elif choice == "remove":
            remove_hobbies()
        elif choice == "mark":
             markdone_hobbies()
        else:
             print("That's not a vaild option")

if __name__ == "__main__":
     __main__()

    
               
     


        

        

        
        
    


