import csv
from datetime import datetime

# Step 1: Define the Item class
class Item:
    def __init__(self, item_id, manufacturer, item_type, price, service_date, damaged):
        self.item_id = item_id
        self.manufacturer = manufacturer
        self.item_type = item_type
        self.price = price
        self.service_date = service_date
        self.damaged = damaged

# Step 2: Function to read data from a CSV file
def read_csv(file_name):
    """
    Reads data from a CSV file and returns a dictionary where the key is the item ID 
    and the value is the rest of the data in the row.
    """
    data = {}
    with open(file_name, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            data[row[0]] = row[1:]
    return data

# Step 3: Load data from all CSV files
def load_data():
    """
    Loads data from ManufacturerList.csv, PriceList.csv, and ServiceDatesList.csv
    and returns them as dictionaries.
    """
    manufacturer_data = read_csv('ManufacturerList.csv')
    price_data = read_csv('PriceList.csv')
    service_dates_data = read_csv('ServiceDatesList.csv')
    return manufacturer_data, price_data, service_dates_data

# Step 4: Process data into a list of Item objects
def process_data(manufacturer_data, price_data, service_dates_data):
    """
    Combines data from the manufacturer, price, and service dates files into
    a list of Item objects.
    """
    items = []
    for item_id, (manufacturer, item_type, *damaged) in manufacturer_data.items():
        price = price_data[item_id][0]
        service_date = service_dates_data[item_id][0]
        damaged = damaged[0] if damaged else ""
        item = Item(item_id, manufacturer, item_type, float(price), service_date, damaged)
        items.append(item)
    return items

# Custom sorting functions
def sort_by_manufacturer(item):
    """
    Returns the manufacturer of the item, used for sorting by manufacturer.
    """
    return item.manufacturer

def sort_by_item_id(item):
    """
    Returns the item ID, used for sorting by item ID.
    """
    return item.item_id

def sort_by_service_date(item):
    """
    Returns the service date of the item as a datetime object, used for sorting by service date.
    """
    return datetime.strptime(item.service_date, '%m/%d/%Y')

def sort_by_price(item):
    """
    Returns the price of the item, used for sorting by price.
    """
    return item.price

# Step 5: Write full inventory to CSV
def write_full_inventory(items):
    """
    Writes the full inventory to FullInventory.csv, sorted alphabetically by manufacturer.
    """
    items.sort(key=sort_by_manufacturer)
    with open('FullInventory.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        for item in items:
            writer.writerow([item.item_id, item.manufacturer, item.item_type, item.price, item.service_date, item.damaged])

# Step 6: Write item type specific inventories to CSV
def write_item_type_inventories(items):
    """
    Writes a separate inventory file for each item type (e.g., LaptopInventory.csv),
    sorted by item ID.
    """
    item_types = {}
    for item in items:
        if item.item_type not in item_types:
            item_types[item.item_type] = []
        item_types[item.item_type].append(item)
    
    for item_type, items in item_types.items():
        items.sort(key=sort_by_item_id)
        with open(f'{item_type}Inventory.csv', mode='w', newline='') as file:
            writer = csv.writer(file)
            for item in items:
                writer.writerow([item.item_id, item.manufacturer, item.price, item.service_date, item.damaged])

# Step 7: Write past service date inventory to CSV
def write_past_service_date_inventory(items):
    """
    Writes items that are past their service date to PastServiceDateInventory.csv,
    sorted by service date from oldest to most recent.
    """
    today = datetime.today().date()
    past_service_items = [item for item in items if datetime.strptime(item.service_date, '%m/%d/%Y').date() < today]
    past_service_items.sort(key=sort_by_service_date)
    with open('PastServiceDateInventory.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        for item in past_service_items:
            writer.writerow([item.item_id, item.manufacturer, item.item_type, item.price, item.service_date, item.damaged])

# Step 8: Write damaged inventory to CSV
def write_damaged_inventory(items):
    """
    Writes all damaged items to DamagedInventory.csv, sorted by price from highest to lowest.
    """
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
    manufacturer_data, price_data, service_dates_data = load_data()
    items = process_data(manufacturer_data, price_data, service_dates_data)
    generate_reports(items)

# Step 11: Execute the main function
if __name__ == '__main__':
    main()
