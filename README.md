# StoreLocator
A demo that enables customers to search the locations of retailers in Google Map. Made for Systems Integration course. 
The idea of this demo is to demonstrate the ideas of application and data integration.

## Three major components in the demo system:
* Data integration demo. 
  * stores.csv and locations.xml, contains the information about location coordinates for each store. 
    * data_merger.py is the script that read these two data files and output the merged result into a csv file, under the name store_locations.csv
* RESTful web service demo returning a JSON object. 
  * This is within the store_locator.py file
* Mashup demo that accepts a postcode as the input. 
  * A very simple HTML file called store_map.html

## Built with

* Python 
* Atom

## Author

* **Paul Jensen** - *Initial work* - [pjj007] https://github.com/pjj007 

## Acknowledgements
* Dr Mingzhong Wang - Course Coordinator
