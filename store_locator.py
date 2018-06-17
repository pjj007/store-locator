from bottle import route, run, request, response
import petl as etl


@route('/getlocation')
# Set headers
# Retrieve data from csv file
def display_store():
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Content-type'] = 'application/json'
    table = (
        etl
        .fromcsv('store_locations.csv')
        .convert('Lat', float)
        .convert('Lon', float)
    )
    store_id = request.query.postcode

    # Select rows
    table1 = etl.select(table, "{Postcode}=='" + store_id + "'")

    # Set default postcode of 2000 
    if etl.nrows(table1) == 0:
        defaultPostCode = "2000"
        table1 = etl.select(table, "{Postcode}=='" + defaultPostCode + "'")

    # Reorder fields
    print(table1)
    table2 = etl.cut(table1, 'Name', 'Lat', 'Lon').dicts()[0]

    print(table2)
    return table2


run(host='localhost', port=8080, debug=False)
