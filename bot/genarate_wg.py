import os

async def create_config(ip: str, user_name: str)-> None:
    os.system(f"sudo ../wireguard_setup/creat_client.sh {user_name} {ip}")