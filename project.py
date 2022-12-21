from selenium import webdriver

# Open the web browser and go to the Snapchat website
driver = webdriver.Chrome()
driver.get("https://www.snapchat.com/")

# Read the login information from a text file
with open("login_info.txt", "r") as login_file:
  username = login_file.readline().strip()
  password = login_file.readline().strip()

# Find the username and password fields on the website
username_field = driver.find_element_by_id("username")
password_field = driver.find_element_by_id("password")

# Enter the login information in the fields
username_field.send_keys(username)
password_field.send_keys(password)

# Find the login button and click it
login_button = driver.find_element_by_class_name("login-button")
login_button.click()





# Find the chat icons on the website
chats = driver.find_elements_by_class_name("chat-icon")

# Click on each chat icon
for chat in chats:
  chat.click()
  
  # Send the custom message
  message_field = driver.find_element_by_class_name("message-box-input")
  message_field.send_keys("Hello, this is a custom message")
  send_button = driver.find_element_by_class_name("send-button")
  send_button.click()
  
  # Go back to the main screen
  driver.back()
