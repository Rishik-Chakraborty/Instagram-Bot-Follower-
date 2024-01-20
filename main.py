

import time  # using time library to delay certain actions to avoid bot detection
from selenium import webdriver  # using webdriver to access the google.com page
from selenium.webdriver.chrome.options import Options  # options is used with webdriver to securely connect to browser
from selenium.webdriver.common.by import By  # By is used to sort through HTML tags, and select a box/button
from selenium.webdriver.common.keys import Keys  # allows me to press keys on my keyboard to send as data

# Configuring Chrome options
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

# Constants for Instagram account
USERNAME = "YOUR PERSONAL USERNAME"
PASSWORD = "YOUR ACCOUNT'S PASSWORD"

# Asking user which public account they want to follow the followers of

SIMILAR_ACCOUNT = str(input("Which account do you want to follow? It must be public, and please do not include the @:"))

if SIMILAR_ACCOUNT[0] == "@":
    SIMILAR_ACCOUNT = SIMILAR_ACCOUNT[1:len(SIMILAR_ACCOUNT) - 1]

# Create a class for Instagram Follower Bot
class InstaFollower:
    def __init__(self):
        # Initializing WebDriver to establish the environment connection for subsequent methods to function.

        self.driver = webdriver.Chrome(options=chrome_options)

    # Method to print characters slowly
    def print_slow(self, element, text):
        for char in text:
            element.send_keys(char)
            time.sleep(0.5)  # printing 2 characters per second

    # Method to log in to Instagram
    def login(self):
        self.driver.get("https://www.instagram.com/accounts/login/")  # Open Instagram login page
        time.sleep(5)  # Wait for the page to load, and used this time to avoid Instagram Bot detection

        # Find username field by finding class name "_aa4b"
        username_field = self.driver.find_element(By.CLASS_NAME, "_aa4b")

        # Printing username in username box. Printing slowly to avoid bot detection
        self.print_slow(username_field, USERNAME)

        # Find password field
        password_field = self.driver.find_element(By.NAME, "password")

        # Printing password slowly
        self.print_slow(password_field, PASSWORD)

        # Pressing Enter to log in
        password_field.send_keys(Keys.ENTER)

        time.sleep(3)

    # Method to find followers of a specific account
    def find_followers(self):
        time.sleep(3)
        # Navigate to the followers page of the specified account
        followers_url = f"https://www.instagram.com/{SIMILAR_ACCOUNT}/followers"
        self.driver.get(followers_url)
        time.sleep(2)

        # Finding HTML class name which opens the followers page
        followers_container = self.driver.find_element(By.CLASS_NAME, "_acan")
        time.sleep(4)

        # Scroll through the followers list 5 times (doing more would result in suspicious behavior)
        for _ in range(5):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", followers_container)
            time.sleep(3)

    # Method to follow accounts in the followers list
    def follow(self):
        # Find all 'Follow' buttons
        follow_buttons = self.driver.find_elements(By.CLASS_NAME, '_acan._acap._acas._aj1-')
        # Click on each 'Follow' button
        for button in follow_buttons:
            button.click()
            time.sleep(1)


# Instantiate the Instagram Follower Bot
try:
    verifying_intent = input(
        f"\nAre you ok with following the followers of {SIMILAR_ACCOUNT}'s Instagram account? Yes or No: ").upper()

    if verifying_intent in ["YES", "Y", "YA"]:
        value = 1
        print("\nThe program will run in 3 seconds. There will be several 5 second delays to avoid Instagram Bot "
              "detection, so please do not close the program prematurely.")
        time.sleep(3)
        bot = InstaFollower()
        # Execute bot actions
        bot.login()  # Login to Instagram
        bot.find_followers()  # Find followers of a specific account
        bot.follow()  # Follow accounts

    elif verifying_intent in ["NO", "N", "NA", "NAH"]:
        value = 0
        print("It seems like there's an issue with following the account's followers.")

    else:
        print("Looks like you didn't tell me yes or no. Please try again!")

except Exception as e:
    # Print only the first line of the error message
    print(f"\n\nError {str(e).splitlines()[0]}")
