# Lohgan Joseph
# 2038027

import csv
from datetime import datetime

"""
Part 1: Defining the item classes. 
"""

class Item:
    def item_tab(self, item_id, manufacturer, item_type, price, service_date, damaged):
        self.item_id = item_id
        self.manufacturer = manufacturer
        self.item_type = item_type
        self.price = price
        self.service_date = service_date
        self.damaged = damaged

"""
Part 2: Reading the csv file.
This is where the function for opening the csv files will be
"""

def read_csv(file_name):
    data = {}
    with open(file_name, mode = 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            data[row[0]] = row[1:]
    return data

"""
Part 3: Loading the data from the csv's
This part is giving me trouble because the program won't read the file despite being in the 
right repository and path.


"""

def load_data():
    manufacturer_data = read_csv('ManufacturerList.csv')
    price_data = read_csv('PriceList.csv')
    service_date_data = read_csv('ServiceDatesList.csv')
    return manufacturer_data, price_data, service_date_data

"""
Part 4: Processing the data into a list of items

Here is where the data from the manufacturers, prices, and service dates all combine into a 
list of item objects.
"""

def process_data(manufacturer_data, price_data, service_date_data):
    items = []
    for item_id, (manufacturer, item_type, *damaged) in manufacturer_data.items():
        price = price_data[item_id][0]
        service_date = service_date_data[item_id][0]
        damaged = damaged[0] if damaged else "" # If the item is damaged, it'll be recognized as such, if otherwise there's a blank space
        item = Item(item_id, manufacturer, item_type, float(price), service_date, damaged)
        items.append(item)
    return items

"""
Part 5: Sorting functions

These are functions to sort the list out upon output
"""

def sort_by_manufacturer(item):
    # Used for sorting and returning the item manufacturer
    return item.manufacturer

def sort_by_item_id(item):
    # Used for sorting by and returning the item ID.
    return item.item_id

def sort_by_service_date(item):
    # Used for sorting by and returning the service date. Returned as a datetime object.
    return datetime.strptime(item.service_date, '%m/%d/%Y')

def sort_by_price(item):
    # Used for sorting by and returning the item's price
    return item.price

"""
Part 6: Writing the inventory

Here's the portion that writes the full inventory and outputs it as a csv.
"""


