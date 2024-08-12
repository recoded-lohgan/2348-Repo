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
I'll implement the pandas function
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
    manufacturer_data = read_csv('recoded-lohgan/2348-Repo/Final Project 2024/ManufacturerList.csv')
    price_data = read_csv('recoded-lohgan/2348-Repo/Final Project 2024/PriceList.csv')
    service_date_data = read_csv('recoded-lohgan/2348-Repo/Final Project 2024/ServiceDatesList.csv')
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

# Writing FullInventory
def write_full_inventory(items):
    items.sort(key=sort_by_manufacturer)
    with open('FullInventory.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        for item in items:
            writer.writerow([item.item_id, item.manufacturer, item.item_type, item.price, item.service_date, item.damaged])

# Writing Item Type/LaptopInventory.csv
def write_item_type_inventories(items):
    item_types = {}
    for item in items:
        if item.item_type not in item_types:
            item_types[item.item_type] = []
        item_types[item.item_type].append(item)

    for item_type, items in item_types.items():
        items.sort(key = sort_by_item_id)
        with open(f'{item_type}LaptopInventory.csv', mode = 'w', newline = '') as file:
            writer = csv.writer(file)
            for item in items:
                writer.writerow([item.item_id, item.manufacturer, item.price, item.service_date, item.damaged])

# Writing PastServiceDateInventory.csv
def write_past_service_date_inventory(items):
    today = datetime.today().date()
    past_service_items = [item for item in items if datetime.strptime(item.service_date, '%m/%d/%Y').date() < today]
    past_service_items.sort(key = sort_by_service_date)
    with open('PastServiceDateInventory.csv', mode = 'w', newline = '') as file:
        writer = csv.writer(file)
        for item in past_service_items:
            writer.writerow([item.item_id, item.manufacturer, item.item_type, item.price, item.service_date, item.damaged])

# Writing DamagedInventory.csv
def write_damaged_inventory(items):
    damaged_items = [item for item in items if item.damaged]
    damaged_items.sort(key=sort_by_price, reverse=True)
    with open('DamagedInventory.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        for item in damaged_items:
            writer.writerow([item.item_id, item.manufacturer, item.item_type, item.price, item.service_date])

# Step 9: Generate all required reports
def generate_reports(items):
    """
    Generates all inventory reports: FullInventory, Item Type Inventories, 
    Past Service Date Inventory, and Damaged Inventory.
    """
    write_full_inventory(items)
    write_item_type_inventories(items)
    write_past_service_date_inventory(items)
    write_damaged_inventory(items)

# Step 10: Main function to orchestrate the loading, processing, and report generation
def main():
    """
    Main function to execute the program. It loads data from CSV files,
    processes it, and generates the required inventory reports.
    """
    manufacturer_data, price_data, service_date_data = load_data()
    items = process_data(manufacturer_data, price_data, service_date_data)
    generate_reports(items)

# Step 11: Execute the main function
if __name__ == '__main__':
    main()