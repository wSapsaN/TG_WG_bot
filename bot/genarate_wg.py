import os
from config import GENERATE_SCRIPT_path

async def create_config(ip: str, user_name: str)-> str:
    os.system(f"{GENERATE_SCRIPT_path} {user_name} {ip} 2>> error.txt")

    return f"{user_name}.conf"