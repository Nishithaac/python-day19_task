

from selenium import webdriver  # Import the Selenium WebDriver module
from selenium.webdriver.chrome.service import Service  # Import the Service class for ChromeDriver
from webdriver_manager.chrome import ChromeDriverManager  # Import ChromeDriverManager for automatic installation
from selenium.webdriver.common.by import By  # Import By class for locating elements

class Webpage:
    filename = "Webpage_task_11.txt"  # Class variable to store the filename

    def __init__(self, url):
        self.url = url  # Initialize with the URL of the webpage
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))  # Initialize Chrome WebDriver

    def start(self):
        self.driver.maximize_window()  # Maximize the browser window
        self.driver.get(self.url)  # Open the provided URL in the browser

    # Logging into the page with username and password
    def login(self): # Defining a function to login into the page
        # Locate username field and enter username
        self.driver.find_element(by=By.ID, value="user-name").send_keys("standard_user")
        # Locate password field and enter password
        self.driver.find_element(by=By.ID, value="password").send_keys("secret_sauce")
        # Locate login button and click it
        self.driver.find_element(by=By.ID, value="login-button").click()

    # 1) Title of the webpage
    def title(self): # Defining a method to fetch the title of the web page
        print("Title of the webpage is :", self.driver.title)  # Print and display the title of the webpage

    # 2) Current URL of the webpage
    def current_url(self):# Defining a method to fetch the current url
        # Print and display the current URL of the webpage
        print("Current URL of the webpage is : ", self.driver.current_url)

    # 3) Extract the entire contents of the webpage and save it in a Text file whose name will be "Webpage_task_11.txt"
    def contents(self):
        with open(self.filename, "w", encoding="utf-8") as file:  # Open the file for writing
            file.write(self.driver.page_source)  # Write the entire HTML source of the webpage to the file

    def shutdown(self):
        self.driver.close()  # Close the WebDriver instance

if __name__ == "__main__":
    url = "https://www.saucedemo.com/"  # Define the URL of the webpage
    webpage = Webpage(url)  # Create an instance of Webpage class
    webpage.start()  # Open the webpage in the browser
    webpage.login()  # Login to the webpage
    webpage.title()  # Print the title of the webpage
    webpage.current_url()  # Print the current URL of the webpage
    webpage.contents()  # Save the contents of the webpage to a file
    webpage.shutdown()  # Close the browser session


