from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update

from database.models import User

async def outAllUsers(session: AsyncSession):
    response = select(User)
    res = await session.execute(response)
    
    return res.scalar().id

async def get_nameClinet(session: AsyncSession, id_telegram: int)-> str:
    response = select(User.nik_name_telegram).where(User.id_telegram == id_telegram)
    res = await session.execute(response)
    
    return str(res.scalar())

async def get_lastIPClinet(session: AsyncSession, id_telegram: int)-> int:
    last_id = await get_userIDinDB__(session=session, id_telegram=id_telegram)

    response = select(User.ip_client).where(User.id == last_id)
    res = await session.execute(response)
    
    return int(res.scalar().split('.')[-1])

async def get_userIDinDB__(session: AsyncSession, id_telegram: int)-> int:
    response = select(User.id).where(User.id_telegram == id_telegram)
    res = await session.execute(response)

    return int(res.scalar())-1