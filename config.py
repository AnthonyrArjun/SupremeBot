"""
As of 12/07/2021, Supreme.com allows for 2021-2031 as card expiration years.
These years are 1-10 in xpath selector in element inspector. 
The key 'card_year' must match the corresponding 1-10 number for the script to function.
Ex. if exp year is 2023, set card_year to 3.

"""




keys ={
    'product_url': 'https://www.supremenewyork.com/shop/accessories/kd9n3yxwh/t0snob67u',
    'name':'',
    'email': '',
    'phone':'' ,
    'address': '',
    'zip' : '',
    'city': '',
    'card': '',
    'card_month': '',
    'card_year': '',         # See above documentation. It's literally 4 lines
    'cvv': ''
}