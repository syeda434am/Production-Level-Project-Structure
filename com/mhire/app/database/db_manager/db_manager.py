import time
import logging

from com.mhire.app.database.db_manager.db_connection import DBConnection, logger



class DBManager(DBConnection):
    
    def __init__(self, connection_name):

        super().__init__(connection_name)  # Inherit from DBConnection

    def insert_data(self):
        return self.insert_data_with_ranker()

    def update_entry(self):
        return self.update_entry_with_ranker()

    def delete_entry(self):
        return self.delete_entry_with_ranker()

    def search_and_retrieve(self):
        return self.search_and_retrieve_with_ranker()

