from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update

from database.models import User

async def outAllUsers(session: AsyncSession):
    response = select(User)
    res = await session.execute(response)
    
    return res.scalar().id