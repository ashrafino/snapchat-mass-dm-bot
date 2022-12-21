# snapchat-mass-dm-bot
This code is using the Selenium webdriver to automate tasks in the Chrome web browser. The tasks being automated include logging in to the Snapchat website and sending a message to each of the user's chats.

Here's a breakdown of what the code does:

Import the webdriver module from the selenium library.
Initialize the Chrome webdriver and use it to open the Snapchat website.
Read the login information (username and password) from a text file called "login_info.txt".
Find the username and password fields on the Snapchat website and enter the login information in those fields.
Find the login button and click it to log in to the website.
Find all the chat icons on the website and click on each one.
For each chat, find the message field and send a custom message. Then find the send button and click it to send the message.
Go back to the main screen of the website after sending each message.
This code will open the Chrome web browser, navigate to the Snapchat website, log in, and send a message to each of the user's chats. It does this by interacting with the web page using the Chrome webdriver and the elements on the page (such as the login button and the message field) using their HTML attributes (such as their class names).

I recently attempted to use a bot to log in to my account on the website, but the bot was unable to do so because of an issue with verification. Whenever the bot entered my login information and clicked the login button, it was prompted to enter a verification code that was sent to my phone via the app. The bot was unable to retrieve this code, so it was unable to log in to my account. I tried multiple times, but the verification issue persisted. This is a problem because I rely on the bot to access my account and perform certain tasks, and now it is unable to do so due to this verification issue. I hope to find a solution soon so that the bot can log in to my account and resume its duties.
