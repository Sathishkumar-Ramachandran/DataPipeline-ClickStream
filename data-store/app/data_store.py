# data-store/app/data_store.py

import psycopg2

class DataStore:
    def __init__(self):
        # Initialize the data store connection
        self.connection = psycopg2.connect(host='localhost', port=5432, database='data_store', user='username', password='password')
        self.cursor = self.connection.cursor()

    def store_clickstream_data(self, data):
        # Assuming data is a dictionary with keys: 'UserID', 'Timestamp', 'URL', 'Country', 'City'
        sql = "INSERT INTO clickstream_table (user_id, timestamp, url, country, city) VALUES (%s, %s, %s, %s, %s)"
        values = (data['UserID'], data['Timestamp'], data['URL'], data['Country'], data['City'])
        self.cursor.execute(sql, values)
        self.connection.commit()