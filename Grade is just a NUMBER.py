def assign_grade(score):
    if score < 0 or score > 100:
        print("Invalid Score!! Please Enter a value between 0 and 100.")
    elif score <= 60:
        print("Grade: F")
    elif score <= 69:
        print("Grade D")
    elif score <= 79:
        print("Grade C")
    elif score <= 89:
        print("Grade B")
    else:
        print("Grade A")
    
while True:
    score_input = input("Enter your score: ")
    if not score_input.isdigit():
         print("Invalid input. Please enter a valid number.")
         continue
    
    score = int(score_input)
    assign_grade(score)
    
    babyko123 = input("Do you want to enter another score? (yes/no): ")
    if babyko123 != 'yes':
        print("Exiting the Program.")
        break

    