# Vending Machine Project

# Libraries Used
import pandas as pd # To convert product dictionary to table

# Functions
# The mon_link function connects the product code to amount and declares how much should be deducted for each purchase.
# A function was used here because we will be needing this operation more than once across the programme
# The global method is used here so we can modify it outside of current use.
# This is important because the value of change and vat will differ at every point.

def mon_link():
    global change
    global vat

    if productID == "SB":
        change = change - 5
    elif productID == "FB":
        change = change - 10
    elif productID == "MB":
        change = change - 20
    elif productID == "TB":
        change = change - 50

        # Created a list of acceptable prices so the programme can loop through to check the correctness of user input.
prices = [5, 10, 20, 50]

# A dictionary was used to leverage on it's associative array structure to connect product name, price and product code together.
prod = {"product_name": ["Slim bar", "Far bar", "Mar bar", "Twin bar"],
        "price": ["5p", "10p", "20p", "50p"],
        "product_code": ["SB", "FB", "MB", "TB"]}

# The dictionary above is then converted to a data frame for its table-like structure so users can easily read through.
# The dataframe was called later in the programme.
product_table = pd.DataFrame.from_dict(prod)

# Created a list of product code so the programme can loop through to check correctness user input.
product_code = ["SB", "FB", "MB", "TB"]

# Building the vending machine in a function comes in handy when the hardware does more than vending.
def vending_machine():
    # The print functions gives the user a clear understanding of what the machine does and what criteria it takes to work.
    print(
        "Welcome to Fi's Vending Machine.\n  \n Note: The coin denomination this machine can take are 5, 10, 20 and 50.\n")

    # This dataframe ensures the user knows what product is available and at what price.
    print(product_table)

    # The global method is used here so we can modify variable value outside of current use.
    global change
    global money
    global productID
    global vat

    # The try and except method is used here to control and check that the value of coin (money) entered is...
    # ... an acceptable coin and is not a string.
    # The embedded while loops ensures the user enters the right value before moving to the next process.
    while True:
        try:
            money = int(input("Enter your coin here: "))
            while money not in [5, 10, 20, 50]:
                money = int(input("Please enter a correct coin here: "))
            break
        except ValueError:
            print('Please insert a valid coin')
            continue

    # ProductID takes in input from the user and the while loop checks if the input entered is in the acceptable...
    # ... product code list. If it's not, the user is prompted to enter the code again.
    productID = input("please enter a product code:").upper()
    while productID not in product_code:
        productID = input("please enter a valid product code:").upper()

    change = money

    mon_link()

    # The while loop here deals with the change, ensuring the user does not buy more than the coin inputed.
    # A while loop is embedded within to check that users enter the right ID on the next try after they have tried...
    # ...to buy more the the amount they have.

    while change < 0:
        print('Oppss! You have selected a product above your balance ')
        productID = input("Please enter a product code in accordance with your balance:").upper()
        change = money
        while productID not in product_code:
            productID = input("Please enter a valid product code:").upper()

        mon_link()
        # In the case where the user has more coin than their purchase, the while loop below controls their
        # second (or multiple) purchase or gives them change if they choose not to make a second purchase.
    while change > 0:

        multiple_purchase = input(
            f"You have {change}p left, will you like to purchase other product? Enter Yes or No: ").upper()

        # This is conform the user's second purchase request to yes or no string format
        while multiple_purchase not in ["YES", "NO"]:
            multiple_purchase = input(f"You have {change}p left,please enter either Yes or No: ").upper()
        if multiple_purchase == "YES":
            productID = input("please enter a product code:").upper()
            while productID not in product_code:
                productID = input("please enter a valid product code:").upper()
            vat = change
            mon_link()
            while change < 0:
                print('Oppss! You have selected a product above your balance ')
                productID = input("Please enter a product code in accordance with your coin:").upper()
                change = vat
                while productID not in product_code:
                    productID = input("please enter a valid product code:").upper()
                mon_link()

                # In a case when the coin has now reached zero, either from the first, second or multiple purchase,...
                # ...the code below prints the thank you message and ends the programme.
            print(change)
            if change == 0:
                print("Thank you for shopping at Fi's vending machine")

                # In a case where the user still has change but is ot willing to make another purchase, the elif...
                # ... statement prints the user's change and breaks the programme.
        elif multiple_purchase == "NO":
            print(f'you have {change}p')
            break


# Initiating the vending machine programme.
# Until the programme is done running, the print statement below it will not run.

vending_machine()

print('You are all done! Please take your product(s)')


#Another Project

#Smarter way to quickly visualise data. Follow the steps below:

# 1. Install package - Search for "pivottablejs" and install
# 2. Import dataset - Find the "FAO.csv" dataset attached to this submission or simply download if from the link below-
#  https://drive.google.com/drive/folders/13mozd1nXsbXKM3pRidwlQoQX0gA_-ktz?usp=sharing
# 3. Ensure the file path of the FAO.CSV file is consistent with your default python path

# Read in the data set
df = pd.read_csv("FAO.csv")

# See first 5 rows of the data to understand its structure
df.head(2)

# import package for visualisation
from pivottablejs import pivot_ui

# Display pop out with data set
pivot_ui(df)

# Display the relationship between any two columns and switch chart types with ease
