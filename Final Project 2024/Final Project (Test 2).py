import csv
from datetime import datetime

# File paths
manufacturer_file = 'ManufacturerList.csv'
price_file = 'PriceList.csv'
service_date_file = 'ServiceDatesList.csv'

# Dictionaries to store the data
manufacturer_data = {}
price_data = {}
service_date_data = {}

# Reading ManufacturerList.csv
with open(manufacturer_file, 'r') as file:
    reader = csv.reader(file)
    next(reader)  # Skip header
    for row in reader:
        item_id = row[0]
        manufacturer_data[item_id] = {
            'manufacturer': row[1],
            'item_type': row[2],
            'damaged': row[3] if len(row) > 3 else ''
        }

# Reading PriceList.csv
with open(price_file, 'r') as file:
    reader = csv.reader(file)
    next(reader)  # Skip header
    for row in reader:
        item_id = row[0]
        price_data[item_id] = row[1]

# Reading ServiceDatesList.csv
with open(service_date_file, 'r') as file:
    reader = csv.reader(file)
    next(reader)  # Skip header
    for row in reader:
        item_id = row[0]
        service_date_data[item_id] = row[1]

# Processing and creating the output files
full_inventory = []
laptop_inventory = []
phone_inventory = []
tv_inventory = []
past_service_date_inventory = []
damaged_inventory = []

# Current date for past service date comparison
today = datetime.today()

# Default service date
default_service_date = '01/01/1900'

# Combining the data
for item_id, details in manufacturer_data.items():
    manufacturer = details['manufacturer']
    item_type = details['item_type']
    damaged = details['damaged']
    price = price_data.get(item_id, '0')
    service_date = service_date_data.get(item_id, default_service_date)

    # Full Inventory
    full_inventory.append([item_id, manufacturer, item_type, price, service_date, damaged])

    # Item Type Inventory
    if item_type.lower() == 'laptop':
        laptop_inventory.append([item_id, manufacturer, price, service_date, damaged])
    elif item_type.lower() == 'phone':
        phone_inventory.append([item_id, manufacturer, price, service_date, damaged])
    elif item_type.lower() == 'tv':
        tv_inventory.append([item_id, manufacturer, price, service_date, damaged])

    # Past Service Date Inventory
    service_date_obj = datetime.strptime(service_date, '%m/%d/%Y')
    if service_date_obj < today:
        past_service_date_inventory.append([item_id, manufacturer, item_type, price, service_date, damaged])

    # Damaged Inventory
    if damaged.lower() == 'damaged':
        damaged_inventory.append([item_id, manufacturer, item_type, price, service_date, damaged])

# Sorting the lists as required

# Sort full inventory by manufacturer name
def sort_by_manufacturer(item):
    return item[1]
full_inventory.sort(key=sort_by_manufacturer)

# Sort laptop inventory by item ID
def sort_by_item_id(item):
    return int(item[0])
laptop_inventory.sort(key=sort_by_item_id)

phone_inventory.sort(key=sort_by_item_id)

tv_inventory.sort(key=sort_by_item_id)

# Sort past service date inventory by service date (oldest to most recent)
def sort_by_service_date(item):
    return datetime.strptime(item[4], '%m/%d/%Y')
past_service_date_inventory.sort(key=sort_by_service_date)

# Sort damaged inventory by price (most expensive to least expensive)
def sort_by_price(item):
    return int(item[3])
damaged_inventory.sort(key=sort_by_price, reverse=True)

# Output file names and their corresponding data
output_files = {
    'FullInventory.csv': full_inventory,
    'LaptopInventory.csv': laptop_inventory,
    'PhoneInventory.csv': phone_inventory,
    'TVInventory.csv': tv_inventory,
    'PastServiceDateInventory.csv': past_service_date_inventory,
    'DamagedInventory.csv': damaged_inventory
}

# Writing output files
for file_name, data in output_files.items():
    with open(file_name, 'w', newline='') as file:
        writer = csv.writer(file)
        if 'FullInventory' in file_name:
            writer.writerow(['item_id', 'manufacturer', 'item_type', 'price', 'service_date', 'damaged'])
        elif 'PastServiceDateInventory' in file_name:
            writer.writerow(['item_id', 'manufacturer', 'item_type', 'price', 'service_date', 'damaged'])
        elif 'DamagedInventory' in file_name:
            writer.writerow(['item_id', 'manufacturer', 'item_type', 'price', 'service_date', 'damaged'])
        else:
            writer.writerow(['item_id', 'manufacturer', 'price', 'service_date', 'damaged'])
        writer.writerows(data)
