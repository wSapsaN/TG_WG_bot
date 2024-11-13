import os

async def create_config(ip: str, user_name: str)-> None:
    # os.system(f"sudo ../wireguard_setup/creat_client.sh {user_name} {ip} 2>> error.txt")
    os.system(f"sudo ../wireguard_setup/test_up.sh {user_name} {ip} 2>> error.txt")