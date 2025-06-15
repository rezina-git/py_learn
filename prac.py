def user_choice():
    
    choice = 'WRONG'
    within_range = False
    
    while choice.isdigit() == False or within_range == False :
        
        choice = input ("Please enter a number (0-10)")
        
        if choice.isdigit() == False :
            print("Sorry that is not a digit")
            
        if choice.isdigit() == True:
            if int(choice) in range(0,10):
                within_range = True
            else:
                within_range = False
    return int(choice)

user_choice()