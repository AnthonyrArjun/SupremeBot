from selenium import webdriver 
from config import keys 
import time 


#All buttons/forms to interact with on supreme.com 
def order(k):
        #Specify which URL to open in Chrome
    driver.get(k['product_url'])

        #Select Size
    driver.find_element_by_xpath('//*[@id="size"]/option[2]').click()

        #Add Product to cart
    driver.find_element_by_xpath('//*[@id="add-remove-buttons"]/input').click()

        #Short rest to ensure Checkout Now button appears 
    time.sleep(0.5)

        #Checkout Now 
    driver.find_element_by_xpath('//*[@id="cart"]/a[2]').click()

        #Checkout page: name
    driver.find_element_by_xpath('//*[@id="order_billing_name"]').send_keys(k['name'])

        #Checkout page: email
    driver.find_element_by_xpath('//*[@id="order_email"]').send_keys(k['email'])

        #Checkout page: phone number
    driver.find_element_by_xpath('//*[@id="order_tel"]').send_keys(k['phone'])

        #Checkout page: address
    driver.find_element_by_xpath('//*[@id="order_billing_address"]').send_keys(k['address'])

        #Checkout page: zip code 
    driver.find_element_by_xpath('//*[@id="order_billing_zip"]').send_keys(k['zip'])

        #Checkout page: card number 
    driver.find_element_by_xpath('//*[@id="credit_card_number"]').send_keys(k['card'])

        #Checkout page: card month 
    driver.find_element_by_xpath('//*[@id="credit_card_month"]/option[{}]'.format(k['card_month'])).click()    


        #Checkout page: card year
    driver.find_element_by_xpath('//*[@id="credit_card_year"]/option[{}]'.format(k['card_year'])).click()  

        #Checkout page: CVV 
    driver.find_element_by_xpath('//*[@id="credit_card_verification_value"]').send_keys(k['cvv'])

           #Checkout page: terms and conditions
    driver.find_element_by_xpath('//*[@id="terms-checkbox"]/label/div/ins').click()

        #Checkout page: process payment 
    driver.find_element_by_xpath('//*[@id="pay"]/input').click()



if __name__ == '__main__':
     #Specify webdriver (Chrome, don't touch)
    driver = webdriver.Chrome('./chromedriver')
    order(keys)