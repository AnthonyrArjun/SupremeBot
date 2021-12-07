"""
As of 12/07/2021, Supreme.com allows for 2021-2031 as card expiration years.
These years are 1-10 in xpath selector in element inspector. 
The key 'card_year' must match the corresponding 1-10 number for the script to function.
Ex. if exp year is 2023, set card_year to 3.

"""




keys ={
    'product_url': 'https://www.supremenewyork.com/shop/accessories/kd9n3yxwh/t0snob67u',
    'name':'Anthony Arjun',
    'email': 'anthonyrarjun@gmail.com',
    'phone': 6787071416,
    'address': '104 Hampshire Trace',
    'zip' : 30290,
    'city': 'Tyrone',
    'card': '4011 7100 1770 1668',
    'card_month': 12,
    'card_year': 3,         # See above documentation. It's literally 4 lines
    'cvv': 219
}