def handle_user_input():
    '''
    This function is responsible for handling the user input.
    The height, when entered, is converted to meters (from centimeters)

    INPUT: {
        NONE
    }
    OUTPUT: {
        returns a tuple where tuple[0] is user weight (type float)
        and tuple[1] is user height (type float)
    }
    '''
    weight_input = float(input('Please enter your weight (in Kgs): \n'))
    height_input = float(input('Please enter your height (in cms): \n'))/100

    return weight_input, height_input

def bmi_calculate(height, weight):
    '''
    This function calculates the bmi given the user supplied values. The
    formula used in this function is BMI = weight / height ** 2.

    INPUT: {
        height = the height (type float) as suppled by the user.
        weight = the weight (type float) as supplied by the user.
    }
    OUTPUT: {
        returns a variable which contains the resulting BMI.
    }
    '''

    return weight / (height ** 2)

def main():
    '''
    This function is to run the code on top.
    '''

    print('''
    *********************** B M I   C A L C U L A T O R *********************
    Welcome to the BMI Calculator.
    To calculate your BMI type in you weight (in Kgs)
    and your height (in cm).
    Thanks.
    ''')

    user_weight, user_height = handle_user_input()
    user_bmi = bmi_calculate(user_height, user_weight)
    print('\nyour BMI is...')
    print(round(user_bmi, 2))

# run the function.
main()
