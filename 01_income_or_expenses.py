# Component 01 - Ask user if they want to enter an income or expenses


# Not Blank function goes here
def not_blank(question, error_msg, ):
    error = error_msg

    valid = False
    while not valid:
        response = input(question)

        # If response is blank, question is repeated (loop starts over)
        if response == "":
            print(error)
            continue

        # if response is not blank, program continues
        else:
            return response


# Ask user if they want to enter income or expenses
def which_way():
    valid_input = False
    while not valid_input:
        income_expenses = not_blank("Would you like to enter an income or an expense? ",
                                    "Please input either <income> or <expense>").lower()

        if income_expenses == "income":
            print("You chose {}.".format(income_expenses))
            break

        elif income_expenses == "expense":
            print("You chose {}.".format(income_expenses))
            break

        else:
            print("Please enter <income> or <expense>")

    return income_expenses

# main routine
what_income_expenses = which_way()
