import logging
from py import connections # Assuming you have a database module named py with connections
from com.mhire.app.config.config import Config

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[logging.StreamHandler()]  # Ensures console output
)
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

class DBConnection:

    def __init__(self, connection_name):
        config = Config()
        self.connection_name = connection_name
        self.uri = config.uri
        self.token = config.token
        self.is_connected = False
        
        self.initiate_connection()


    def initiate_connection(self):
        
        if not self.is_connected:
            connections.connect(alias=self.connection_name,
                                uri=self.uri,
                                token=self.token)
            self.is_connected = True
            logger.info(f"Connecting . . . ")
            logger.info(f"Connected to DB: {self.uri}")
        logger.info(self.check_connection())

    def check_connection(self):

        state = connections.has_connection(alias=self.connection_name)
        if state:
            return f"{self.connection_name} connected and running"
        else:
            return f"{self.connection_name} not connected"

    def end_connection(self):
        
        if self.is_connected:
            connections.disconnect(alias=self.connection_name)
            self.is_connected = False
            logger.info(f"Disconnecting . . . ")
            logger.info(f"Connection {self.connection_name} Ended, Disconnected from DB:{self.uri}")

    def __enter__(self):
        """
        Context manager entry point.
        """
        self.connect()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        """
        Context manager exit point.
        """
        self.disconnect()

