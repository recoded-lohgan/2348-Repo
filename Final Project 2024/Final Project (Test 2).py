import pandas as pd
from datetime import datetime

# File paths
manufacturer_file = 'recoded-lohgan/2348-Repo/Final Project 2024/ManufacturerList.csv'
price_file = 'recoded-lohgan/2348-Repo/Final Project 2024/PriceList.csv'
service_date_file = 'recoded-lohgan/2348-Repo/Final Project 2024/ServiceDatesList.csv'

# Read the CSV files into DataFrames
manufacturer_df = pd.read_csv(manufacturer_file)
price_df = pd.read_csv(price_file)
service_date_df = pd.read_csv(service_date_file)

# Merge the DataFrames on 'item_id'
inventory_df = pd.merge(manufacturer_df, price_df, on='item_id')
inventory_df = pd.merge(inventory_df, service_date_df, on='item_id')

# Convert 'service_date' to datetime
inventory_df['service_date'] = pd.to_datetime(inventory_df['service_date'], format='%m/%d/%Y')

# Sort by manufacturer for full inventory
full_inventory_df = inventory_df.sort_values('manufacturer')

# Write full inventory to CSV
full_inventory_df.to_csv('recoded-lohgan/2348-Repo/Final Project 2024/FullInventory.csv', index=False)

# Write item-type specific inventory files
for item_type in inventory_df['item_type'].unique():
    item_type_df = inventory_df[inventory_df['item_type'] == item_type]
    item_type_df = item_type_df.sort_values('item_id')
    item_type_df.to_csv(f'recoded-lohgan/2348-Repo/Final Project 2024/{item_type}Inventory.csv', index=False)

# Filter and sort for past service date inventory
today = pd.to_datetime(datetime.today().strftime('%Y-%m-%d'))
past_service_date_df = inventory_df[inventory_df['service_date'] < today]
past_service_date_df = past_service_date_df.sort_values('service_date')
past_service_date_df.to_csv('recoded-lohgan/2348-Repo/Final Project 2024/PastServiceDateInventory.csv', index=False)

# Filter and sort for damaged inventory
damaged_df = inventory_df[inventory_df['damaged'] == 'damaged']
damaged_df = damaged_df.sort_values('price', ascending=False)
damaged_df.to_csv('recoded-lohgan/2348-Repo/Final Project 2024/DamagedInventory.csv', index=False)