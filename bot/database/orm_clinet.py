from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update

from database.models import User

async def add_client(*, session: AsyncSession, id_telegram: int, nik_name: str):
    
    if await exist_user__(session=session, id_telegram=id_telegram): return
    
    session.add(User(
        id_telegram=id_telegram,
        nik_name_telegram=nik_name,
        reqests_vpn=True,
    ))

    await session.commit()

async def exist_user__(session: AsyncSession, id_telegram: int)-> bool:
    response = select(User.id_telegram).where(User.id_telegram == id_telegram)
    res = await session.execute(response)
    
    return bool(res.scalar())