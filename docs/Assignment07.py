# ---------------------------------------------------------------------------- #
# Title: Assignment 07
# Description: Working with pickling and structured error handling.
#               Developing a demo that build on what we know and introduces pickling and error handling concepts.
# ChangeLog (Who,When,What):
# ,Created started script
# ZDevries, 2/28/2023, Created started script
#
# ---------------------------------

# Data ---------------------------------------------------------------------- #
# Declare variables and constants
filename = 'pickledData.dat' # Name of file for saving data
flt_input1 = 1.0  # Capture user input as a float
flt_input2 = 1.0  # Captures user input as a float
str_result = ''  # The string result of the mathematical operation
# Processing  --------------------------------------------------------------- #
class Processor:
    """  Performs Processing tasks """

    @staticmethod
    def perform_addition(p1, p2):
        """  Display a menu of choices to the user
        :param p1: (float) value to be added:
        :param p2: (float) value to be added:
        :return: (float) result of the addition of two numbers
        """
        result = p1 + p2
        return result

    @staticmethod
    def perform_subtraction(p1, p2):
        """  Display a menu of choices to the user
        :param p1: (float) value to be added:
        :param p2: (float) value to be added:
        :return: (float) result of the addition of two numbers
        """
        result = p1 - p2
        return result

    @staticmethod
    def perform_division(p1, p2):
        """  Display a menu of choices to the user
        :param p1: (float) value to be added:
        :param p2: (float) value to be added:
        :return: (float) result of the addition of two numbers
        """
        try:
            result = p1 / p2
        except ZeroDivisionError:  # Provide error handling
            print('\n You cannot divide a number by 0')
        return result

    @staticmethod
    def Write_Data_To_File(str_save_data):
        """ Writes data to a File
        :param str_save_data: (string) you want saved to the file:
        """

        file = open("pickledData.dat", "ab")
        pickle.dump(str_save_data, file)
        file.close()

    @staticmethod
    def read_data_from_file(filename):
        """ Read data from the pickled file

        :param file_name: (string) with name of file:
        """
        with open(filename, "rb") as file:
            while True:
                try:
                    print(pickle.load(file))
                except EOFError:
                    break



# Presentation (Input/Output)  -------------------------------------------- #
class IO:
    """ Performs Input and Output tasks """

    @staticmethod
    def output_menu_tasks():
        """  Display a menu of choices to the user

        :return: nothing
        """

        print('''
        Menu of Options
        1) Add the Values
        2) Subtract the Values
        3) Divide the Values
        4) Review Data Saved to File
        5) Exit the Program
        ''')

        print()  # Add an extra line for looks
    @staticmethod
    def input_menu_choice():
        """ Gets the menu choice from a user

        :return: string
        """

        choice = str(input("Which option would you like to perform? [1 to 5] - ")).strip()
        print()  # Add an extra line for looks
        return choice

    @staticmethod
    def input_values_for_calculation():
        """ Gets a number from the user

        :return: float
        """
        try:
            flt_input = float(input('Enter a Number: ')) # Get user to provide a number
        except ValueError:
            print('That was not a number')  # Provide an error message if the user does not enter a number
        return flt_input

    @staticmethod
    def print_results(result):
        """ Prints the results to the user
        :return: string
        """
        print('\nThe result is: ' + result)  # Print the formatted result

    @staticmethod
    def save_preference():
        """ Prompts user to save results
        :return: string
        """
        # Get user input to determine whether they would like to save the equation
        str_save_pref = input('Would you like to save the formula to a file: y/n ').lower().strip()

        return str_save_pref


# Main Body of Script  ------------------------------------------------------ #

import pickle

# Open and close the file to clear and or populate the .dat file in the working directory
file = open("pickledData.dat", "wb")
file.close()

# Present the menu options to the user
while (True):
    IO.output_menu_tasks()  # Shows menu
    choice_str = IO.input_menu_choice()  # Get menu option

    if choice_str == '1':
        # Perform Addition
        print('Enter the numbers you would like to add \n')
        flt_input1 = IO.input_values_for_calculation() # Get user input
        flt_input2 = IO.input_values_for_calculation()  # Get user input
        str_result = str(Processor.perform_addition(flt_input1, flt_input2)) # Add the numbers
        IO.print_results(str_result)  # Print the result
        if IO.save_preference() == "y":
            str_save_dat = str(flt_input1) + ' + ' + str(flt_input2) + ' = ' + str_result + '\n'
            Processor.Write_Data_To_File(str_save_dat)
            print('Data saved to file')
        else: break

    elif choice_str == '2':
        # Perform Subtraction
        print('Enter the numbers you would like to subtract \n')
        flt_input1 = IO.input_values_for_calculation()  # Get user input
        flt_input2 = IO.input_values_for_calculation()  # Get user input
        str_result = str(Processor.perform_subtraction(flt_input1, flt_input2))  # Subtract the numbers
        IO.print_results(str_result)
        if IO.save_preference() == "y":
            str_save_dat = str(flt_input1) + ' - ' + str(flt_input2) + ' = ' + str_result + '\n'
            Processor.Write_Data_To_File(str_save_dat)
            print('Data saved to file')
        else: break

    elif choice_str == '3':
        # Perform Division
        print('Enter the numbers you would like to divide \n')
        flt_input1 = IO.input_values_for_calculation()  # Get user input
        flt_input2 = IO.input_values_for_calculation()  # Get user input
        str_result = str(Processor.perform_division(flt_input1, flt_input2))  # Subtract the numbers
        IO.print_results(str_result)
        if IO.save_preference() == "y":
            str_save_dat = str(flt_input1) + ' \ ' + str(flt_input2) + ' = ' + str_result + '\n'
            Processor.Write_Data_To_File(str_save_dat)
            print('Data saved to file')
        else: break

    elif choice_str == '4':
        Processor.read_data_from_file(filename)

    elif choice_str == '5':  # Exit Program
        print("Goodbye!")
        break  # by exiting loop
    else:
        print(choice_str + ' is not a number between 1-4')
