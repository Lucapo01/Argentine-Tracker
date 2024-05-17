from motor.motor_asyncio import AsyncIOMotorClient
from ....settings import MONGO_URI

DATABASE = "fcitracker-database"

class NotFoundException(Exception):
    def __init__(self, item_name: str):
        self.item_name = item_name
        super().__init__(f"{item_name} not found")

class AlreadyExistsException(Exception):
    def __init__(self, item_name: str):
        self.item_name = item_name
        super().__init__(f"{item_name} already exists")

class Database:
    def __init__(self, collection):
        self.client = AsyncIOMotorClient(MONGO_URI)
        self.database = self.client[DATABASE]
        self.collection = self.database[collection]

    def __del__(self):
        if self.client is not None:
            self.client.close()
            self.client = None
            self.database = None
