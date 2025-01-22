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
    last_ip = "0"
    
    count = 1
    while last_ip == "0":
        last_id = await get_userIDinDB__(session=session, id_telegram=id_telegram, travl=count)
        print(str(last_id) + f"\n\n{id_telegram}\n\n")
        
        response = select(User.ip_client).where(User.id == last_id)
        res = await session.execute(response)
        
        last_ip = res.scalar()

        count += 1
        if count > 15: return 1

    return int(last_ip.split('.')[-1])
        
async def get_userIDinDB__(session: AsyncSession, id_telegram: int, travl: int)-> int:
    response = select(User.id).where(User.id_telegram == id_telegram)
    res = await session.execute(response)

    return int(res.scalar())-travl