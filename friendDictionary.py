friends = {
    "Natalie": [16, "Blonde", "Dungeons and Dragons", "RWBY", "Hufflepuff"], 
    "Syris": [17, "black", "Watching TikTok", "Grey's Anatomy", "Good at making Mac'n'Cheese"],
    "Mr.Neeno": [40, "grey", "Traveling", "Star Trek", "drawing"]
    }

#This just prints out what the users options are
def option_msg():

    print("What would you like to do?")
    print("1. Add a friend")
    print("2. Delete a friend")
    print("3. Modify a friend")
    print("4. Print a friend")
    print("5. Print ALL friends")
    print("-1. Quit the program")

#This is what runs at the start of the program
def startup():
    print("Welcome to your dictionary of friends!")
    print("This is what your dictionary looks like!")
    print_dictionary()
    while True:
        option_msg()

        choice = int(input("Enter your choice here: "))
        
        if choice == 1:
            add()
        elif choice == 2:
            delete()
        elif choice == 3:
            modify()
        elif choice == 4:
            friend = input("Which friend would you like to print?: ")
            print_friend(friend)
        elif choice == 5:
            print_dictionary()
        elif choice == -1:
            print ("You have lots of friends!")
            print ("Have a nice day! :)")
            break 
        else:
            ("That is not a valid option!")

#This is what adds a new friend to the friends dictionary       
def add():
    new_list= []
    friend_name = input ("What friend would you like to add?: ")
    friend_age = int(input("What is your friends age?: "))
    friend_hair = input ("what is your friends hair colour?: ")
    friend_hobby= input ("What is your friends hobby?: ")
    friend_show = input ("Wwhat is your friends favorite TV show?: ")
    friend_quality = input("What is your friends best quality?: ")
    
    new_list.append(friend_age)
    new_list.append(friend_hair)
    new_list.append(friend_hobby)
    new_list.append(friend_show)
    new_list.append(friend_quality)
    
    friends[friend_name] = new_list
    
    print_dictionary()

#This deletes a friend from the dictionary
def delete():
    print ("____________________________________________________________")

    delete_friend = input ("which friend would you like to delete?: ")
    if delete_friend in friends: 
        del friends [delete_friend]
        print ("____________________________________________________________")
        print ("Here is your new friend list: ")
        print_dictionary()

        
    else:
        print ("You don't have that friend in your list!")
        print ("This is your current friend list")
        print_dictionary()


#This gives the user the option to chabge something in the dictionary about one of their friends 
def modify():
    print ("____________________________________________________________")
    friend_modify = input("Which friend do you want to modify?: ")
    print("     1. Age")
    print("     2. Hair Color")
    print("     3. Hobby")
    print("     4. Favorite show")
    print("     5. Best quality")
    modify_choice= int(input("What do you want modify?: "))
    if modify_choice == 1:
        new_age = int(input("What is their new age?: "))
        friends [friend_modify][0] = new_age
        print_friend(friend_modify)
    elif modify_choice == 2:
        new_hair= input("What is their new hair color?: ")
        friends [friend_modify][1] = new_hair
        print_friend(friend_modify)
    elif modify_choice == 3:
        new_hobby = input("What is their new hobby?: ")
        friends [friend_modify][2] = new_hobby
        print_friend(friend_modify)
    elif modify_choice == 4:
        new_show = input("What is their new favorite show?: ")
        friends [friend_modify][3] = new_show
        print_friend(friend_modify)
    elif modify_choice ==5:
        new_quality = int(input("What is their new best quality?: "))
        friends [friend_modify][0] = new_quality
        print_friend(friend_modify)
    else: 
        print ("That is not a valid option!")
    

#This prints the entire dictionary
def print_dictionary():
    print("Here are your friends!")
    print ("____________________________________________________________")
    for item in friends.keys():
        print("Friend: " + item)
        print ("    Age is " + str(friends[item][0]))
        print ("    Hair color is " +friends[item][1])
        print ("    Hobby is " + friends [item][2])
        print ("    Favorite show is " + friends [item][3])
        print ("    Best quality is " + friends[item][4])
        print ("____________________________________________________________")

#This prints only one friend of the users choice
def print_friend(friend):
    print ("____________________________________________________________")
    print("Friend: " + friend)
    print ("    Age is " + str(friends[friend][0]))
    print ("    Hair color is " +friends[friend][1])
    print ("    Hobby is " + friends [friend][2])
    print ("    Favorite show is " + friends [friend][3])
    print ("    Best quality is " + friends[friend][4])
    print ("____________________________________________________________")

startup()