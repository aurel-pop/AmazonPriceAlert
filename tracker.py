import requests
import time
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
from win10toast import ToastNotifier

toaster = ToastNotifier()
search = input("Enter Product Name: ")
store = {}
search_lists = search.split()
amazon_link = "https://amazon.de"

url = amazon_link+'/s?k='+'+'.join(search_lists)+'aurel0ec-21'

def tracker(random_header):
    # Make a GET request to the Amazon URL using the "requests" library
    # The "headers" parameter is set to the value of "random_header"
    url_open = requests.get(url,headers = random_header)

    # Use BeautifulSoup to parse the HTML content of the page
    soup = BeautifulSoup(url_open.content,'html.parser')

    # Find the first "span" tag with the specified class attribute
    tag = soup('span',{'class':'a-size-medium a-color-base a-text-normal'})

    # Find the first "span" tag with the specified class attribute
    tag_2 = soup('span',{'class':'a-price-whole'})

    # Use "zip" to iterate over both "tag" and "tag_2" in parallel
    for i,j in zip(tag,tag_2):
        # Check if the "search" term appears in the text of the first "span" tag
        if search.lower() in (i.text).lower():
            # If it does, print the item name and price
            print("{} || price: {} Rs".format(i.text,j.text))

            # Store the item name and price in a dictionary called "store"
            store[str(i.text)]=j.text

            # Check if the current item name already exists in the "store" dictionary
            for a,b in store.items():
                if str(i.text)==a:
                    # If it does, compare the current price to the previous price
                    if j.text<b:
                        # If the current price is lower, show a toast notification using the "toaster" library
                        toaster.show_toast("Amazon Deal",i.text+" || Price"+j.text)


while True:
    user = UserAgent()
    randomHeader = {'User-Agent':str(user.random)}
    print('Tracking.....',time.asctime(time.localtime(time.time())))
    tracker(randomHeader)
    time.sleep(60*5)