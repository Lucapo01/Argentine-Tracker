from motor.motor_asyncio import AsyncIOMotorClient

MONGO_URI = "mongodb+srv://lucigar01:4dRMIzQ3W7f26qFU@fcitrackercluster.hfnbd1z.mongodb.net/?retryWrites=true&w=majority&appName=FciTrackerCluster"
DATABASE = "fcitracker-database"
USERS_COLLECTION = "users"

client = AsyncIOMotorClient(MONGO_URI)
database = client[DATABASE]
collection = database[USERS_COLLECTION]

