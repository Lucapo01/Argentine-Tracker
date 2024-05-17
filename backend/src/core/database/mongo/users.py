from . import NotFoundException, Database
from ...schemas.schemas import User
from typing import List

USERS_COLLECTION = "users"

class UsersDatabase(Database):
    def __init__(self):
        super().__init__(USERS_COLLECTION)
    
    async def get_by_ip(self, ip: str) -> User:
        user = await self.collection.find_one({"ip": ip})
        if not user:
            raise NotFoundException(f"User with ip {ip}")
        return User(**user)
    
    async def upsert(self, user: User):
        await self.collection.update_one({"ip": user.ip}, {"$set": user.model_dump()}, upsert=True)

    async def get_all(self) -> List[User]:
        users = []
        async for user in self.collection.find():
            users.append(User(**user))
        return users