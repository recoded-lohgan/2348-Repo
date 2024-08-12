# Lohgan Joseph
# 2038027

import csv
from datetime import datetime

class OutputInventory:
    # This is where the functions to create the outputs lie.

    def __init__(self, item_list):
        # All items must be included to make the full list
        self.item_list = item_list

    # This is the csv output for the full inventory
    def full(self):
        with open("FinalProject_FullInventory.csv", 'w') as file:
            items = self.item_list
            # Get order of keys to write to file based on manufacturer in alphabetical order
            keys = sorted(items.keys(), key = lambda x: items[x]['manufacturer'], reverse=False)
            for item in keys:
                id = item
                man_name = items[item]['manufacturer']
                item_type = items[item]['item_type']
                price = "${:.3f}".format(float(items[item]['price'])) # Ensures the price is in currency format
                service_date = items[item]['service_date']
                damaged = items[item]['damaged']
                file.write('{},{},{},{},{},{}\n'.format(id,man_name,item_type,price,service_date,damaged))


    # csv output for individual item types (Laptop, Phone, and Tower respectively)
    def by_type(self):
        items = self.item_list
        types = []
        keys = sorted(items.keys()) # Sorted by item ID
        for item in items:
            item_type = items[item]['item_type']
            if item_type not in types:
                types.append(item_type)
        for type in types:
            file_name = type.capitalize() + 'Inventory.csv'
            with open('FinalProjectoutput_files' + file_name, 'w') as file:
                for item in keys:
                    id = item
                    man_name = items[item]['manufacturer']
                    price = "${:.3f}".format(float(items[item]['price'])) # Price formatted to look like proper currency
                    service_date = items[item]['service_date']
                    damaged = items[item]['damaged']
                    item_type = items[item]['item_type']
                    if type == item_type:
                        file.write('{},{},{},{},{}\n'.format(id, man_name, price, service_date, damaged))


    # csv output for Past Service Date Inventory (if the item is past the service date)
    def past_service(self):
        items = self.item_list
        keys = sorted(items.keys(), key = lambda x: datetime.strptime(items[x]['service_date'], "%m/%d/%Y"))
        # Sorted by service date oldest to recent
        with open("FinalProject_PastServiceDateInventory.csv", 'w') as file:
            for item in keys:
                id = item
                man_name = items[item]['manufacturer']
                item_type = items[item]['item_type']
                price = "${:.3f}".format(float(items[item]['price']))  # Format price as currency
                service_date = items[item]['service_date']
                damaged = items[item]['damaged']
                today = datetime.now().date()
                service_expiration = datetime.strptime(service_date, "%m/%d/%Y").date()
                expired = service_expiration < today
                if expired:
                    file.write('{},{},{},{},{},{}\n'.format(id, man_name, item_type, price, service_date, damaged))


    # csv output for Damaged Inventory. We need an order of keys to write to the file based on the prices
    def damaged(self):
        items = self.item_list
        keys = sorted(items.keys(), key = lambda x: float(items[x]['price']), reverse=True) 
        # Sorted by lowest to highest price
        with open("FinalProject_DamagedInventory.csv", 'w') as file:
            for item in keys:
                id = item
                manu_name = items[item]['manufacturer']
                item_type = items[item]['item_type']
                price = "${:.3f}".format(float(items[item]['price']))  # Format price as currency
                service_date = items[item]['service_date']
                damaged = items[item]['damaged']
                if damaged:
                    file.write('{},{},{},{},{}\n'.format(id, manu_name, item_type, price, service_date))


if __name__ == '__main__':
    items = {}
    files = ['FinalProject_ManufacturerList.csv', 'FinalProject_PriceList.csv', 'FinalProject_ServiceDatesList.csv']
    for file in files:
        with open(file, 'r') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for line in csv_reader:
                item_id = line[0]
                if file == files[0]:
                    items[item_id] = {}
                    manu_name = line[1]
                    item_type = line[2]
                    damaged = line[3] if len(line) > 3 else ""  # In case the damaged status doesn't appear
                    items[item_id]['manufacturer'] = manu_name.strip()
                    items[item_id]['item_type'] = item_type.strip()
                    items[item_id]['damaged'] = damaged
                elif file == files[1]:
                    price = line[1]
                    items[item_id]['price'] = price
                elif file == files[2]:
                    service_date = line[1]
                    items[item_id]['service_date'] = service_date

    inventory = OutputInventory(items)
    # Make all the output files
    inventory.full()
    inventory.by_type()
    inventory.past_service()
    inventory.damaged()

    # Placing the manufacturers and types in a list
    types = []
    manufacturers = []
    for item in items:
        checked_manufacturer = items[item]['manufacturer']
        checked_type = items[item]['item_type']
        if checked_manufacturer not in types:
            manufacturers.append(checked_manufacturer)
        if checked_type not in types:
            types.append(checked_type)
