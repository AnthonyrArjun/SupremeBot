# SupremeBot
Python web scraper bot that purchases high interest items at a quick execution time


TO USE: 

Must have Selenium Installed: https://pypi.org/project/selenium/ or pip3 install selenium while in working directory in terminal 

Config file MUST be filled out with information in order for code to run. 
Copy and paste the URL of your Supreme product into the 'product_url' key, in between the quotation marks. 
For all numerical values EXCEPT card number, remove the quotations. 
For card number: keep quotations, add spaces between every 4 digits of card number 
See documentation at the top of config.py file for information on card year. 

From your computer's terminal, run the following command: python3 supremebot.py

This script will take you all the way from your specified page, to the captcha image right before the order processes. 
You must still complete the captcha in order to successfully check out. 
