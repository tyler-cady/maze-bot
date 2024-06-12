from fastapi import FastAPI, HTTPException, Request
from pydantic import BaseModel
import os

app = FastAPI()

# Define the path to the IP configuration file
IP_CONFIG_FILE_PATH = "/path/to/ip/config/file"

class IPConfig(BaseModel):
    address: str
    netmask: str
    gateway: str

@app.get("/ip-config")
async def read_ip_config():
    try:
        with open(IP_CONFIG_FILE_PATH, 'r') as file:
            data = file.read()
        return {"config": data}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.put("/ip-config")
async def update_ip_config(config: IPConfig):
    try:
        config_data = f"address={config.address}\nnetmask={config.netmask}\ngateway={config.gateway}\n"
        with open(IP_CONFIG_FILE_PATH, 'w') as file:
            file.write(config_data)
        return {"status": "success"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))