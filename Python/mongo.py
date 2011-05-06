""" mongo.py - A simple demonstration of pymongo

AUTHOR

Mark J. Nenadov (2011)
* Essex, Ontario
* Email: <marknenadov@gmail.com> 

LICENSING

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Lesser General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version

This program is distributed in the hope that it will be useful
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program. If not, see <http://www.gnu.org/licenses/>. 

"""

from pymongo import Connection

def get_collection_names(db):
    """ Return a list of mongodb collections in a database
    """
    connection = Connection('localhost')
    db = connection.test
    return db.collection_names()

def insert_document(collection, data):
    """ Insert document into mongodb
    """

    collection.insert(data)
    print("Inserted data to collection")

connection = Connection('localhost')
db = connection.test

collections = get_collection_names(db)

for collection in collections:
    print("Collection found: " + collection)
    if collection == 'widgets':
        post = {"name": "Mark", "tags": ["programmer", "admin"]}
        insert_document(db[collection], post)
        for item in db[collection].find():
            for item_key in item.keys():
                print(str(item_key) + ": " + str(item[item_key]))
         
