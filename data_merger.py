import petl as etl

# Open CSV file
stores = etl.fromcsv('stores.csv')

# Open XML document
locations = etl.fromxml('locations.xml', 'store', {'Name': 'Name', 'Lat': 'Lat', 'Lon': 'Lon'})
print(locations)

# Set output
output_table = [["ID", "Name", "Suburb", "State", "Postcode"]]

store_id = 1

# Read through the store.csv to generate output_table
store = etl.cut(stores, 'Name', 'Suburb', 'State', 'Postcode').distinct()
print(store)
for s in etl.values(store, 'Name', 'Suburb', 'State', 'Postcode'):
    output_table.append([store_id, s])
    store_id += 1
print (output_table)

# Merge and join XML and CSV together
merge_output = etl.join(stores, locations, key="Name")
print(merge_output)

store_table = etl.cut(merge_output, 'ID', 'Name', 'Suburb', 'State', 'Postcode', 'Lat', 'Lon')
print(etl.head(store_table, 5))

# Export to CSV file
etl.tocsv(merge_output, 'store_locations.csv')


