from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update

from database.models import User

async def add_client(*, session: AsyncSession, id_telegram: int, nik_name: str):
    
    if await exist_user__(session=session, id_telegram=id_telegram): return
    
    session.add(User(
        id_telegram=id_telegram,
        nik_name_telegram=nik_name,
    ))

    await session.commit()

async def exist_user__(session: AsyncSession, id_telegram: int)-> bool:
    response = select(User.id_telegram).where(User.id_telegram == id_telegram)
    res = await session.execute(response)
    
    return bool(res.scalar())

async def update_ip(
        session: AsyncSession, 
        id_telegram: int, 
        address: str
    )-> None:
    
    up_clinet = update(User).where(User.id_telegram == id_telegram).values(ip_client=address)
    up_runtime = update(User).where(User.id_telegram == id_telegram).values(use_runtime=True)

    await session.execute(up_clinet)
    await session.execute(up_runtime)

    await session.commit()

async def status_useVPN(session: AsyncSession, id_telegram: int)-> int:

    response = select(User.reqests_vpn).where(User.id_telegram == id_telegram)

    result = await session.execute(response)

    return int(result.scalar())

async def up_request(session: AsyncSession, id_telegram: int)-> None:
    response = update(User).where(User.id_telegram == id_telegram).values(reqests_vpn=1)

    await session.execute(response)
    await session.commit()