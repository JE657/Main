"""
    Full Name: Jordan-Lee Evan
    Course Number: Is115-3001
    Date of Completion: 4/30/2021
    Time to complete: 60 Minutes

    Explanation: "Write Python code that exercise your
    understanding of functions and lists in Python."
"""


# input user choice from a menu of functions provided
def menu_function():
    print("Enter 1 to process Test Scores, 2 to process Products, 3 to process even numbers, or type 4 to exit: ")
    choice = int(input())
    return choice


# Function to return different values based on test scores passed in
def scores_function(_list):
    if len(_list) > 0:
        print("Sum of total test scores: {}".format(sum(_list)))
        print("Lowest test score: {}".format(min(_list)))
        print("Highest test score: {}".format(max(_list)))
        print("Average of test scores: {}".format(sum(_list) / len(_list)))
    else:
        print("Empty list provided for scores function")


def products_function(_number_of_products):
    # Lists to store user input
    product_names = []
    product_prices = []

    for i in range(_number_of_products):

        # Ask user for a name and append to products list
        product_names.append(input('Enter a name for the product: '))

        loop = False
        while not loop:
            # Try catch block for invalid input
            try:
                product_input = float(input('Enter a price for the product: '))
                while product_input <= 0:
                    print('Please enter a positive value for product price.')
                    product_input = float(input('Enter a price for the product: '))
            except ValueError:  # If an invalid price is given (non-number) for the product
                print("Invalid value given for product price")  # Display an error message
            else:
                loop = True
                product_prices.append(product_input)

    # Variable to hold the average of product prices
    price_average = sum(product_prices) / len(product_prices)

    # Loop to display contents of product lists
    print('Purchase Price Values')
    for _name, _price in zip(product_names, product_prices):
        print('{}\t{}'.format(_name, _price))

    # Display Length of list and the average of prices
    print('Total of {} products.'.format(len(product_names)))
    print('Average product price: {}'.format(price_average))

    # Loop to continuously ask user for prices until they enter an exit command
    user_input = ""
    while user_input != "exit":

        user_input = input('Enter a price for an item (type exit to finish):')
        if user_input != "exit":
            if float(user_input) in product_prices:
                # using list.index function take the index of the price found and match it to the product_names[] object
                # at the same index
                print("PRICE FOUND FOR PRODUCT: {}".format(product_names[product_prices.index(float(user_input))]))

            else:
                print("PRICE NOT FOUND")

    # Return -1 if the price average is greater than 10
    if price_average > 10:
        return -1
    else:
        return price_average


# Function to display all even numbers between _min and _max
def display_even(_min, _max):
    total = 0
    if _min > _max:
        print("Minimum value greater than maximum.")
        return -100

    for i in range(_min, _max+1):
        if i % 2 == 0:
            total += i
            print(i)

    return total

# Main Function
def main():
    choice = menu_function()  # provide the menu
    while choice != 4:  # a continuous loop
        if choice == 1:

            # List and Loop to hold test scores input from user
            scores_list = []
            input_scores = ""
            while input_scores != 'exit':
                print(scores_list)

                # If the user does not enter exit, continue to add test scores, otherwise break the loop
                input_scores = input('Enter a test score (type exit to finish): ')
                if input_scores != 'exit':
                    # Validation for positive values
                    while int(input_scores) < 0:
                        print('Enter a positive value for test scores.')
                        input_scores = input('Enter a test score (type exit to finish): ')

                    # Add score to list
                    scores_list.append(int(input_scores))
                else:
                    # After while loop ends, call the scores_function
                    scores_function(scores_list)

        elif choice == 2:
            # Input amount of products from user
            input_products = int(input('Enter the number of products to enter: '))

            # Validation for positive amount of products
            while input_products < 1:
                print('Enter a number of products greater than 0.')
                input_products = int(input('Enter the number of products to enter: '))

            # Call products function
            products_function(input_products)

        elif choice == 3:
            minimum = int(input('Enter a minimum value for the range: '))
            maximum = int(input('Enter a maximum value for the range: '))
            display_even(minimum, maximum)

        else:
            # If an invalid selection is entered, display a message and loop
            print("Invalid choice - try again")

        # display menu after selection is made
        choice = menu_function()


main()
