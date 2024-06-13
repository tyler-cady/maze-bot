from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from dotenv import load_dotenv, set_key, dotenv_values
import os

app = FastAPI()

class IPConfig(BaseModel):
    ETHERNET_ADDRESS: str
    IP_ADDRESS: str
    IP_ADDRESS_NETMASK: str
    GATEWAY: str
    SECONDARY_IP_ADDRESS: str
    SECONDARY_IP_ADDRESS_NETMASK: str
    SECONDARY_GATEWAY: str

USER_ENV_FILE = "user.env"

# Load the .env file
def load_config():
    if not os.path.exists(USER_ENV_FILE):
        print(f"File {USER_ENV_FILE} not found")
        raise HTTPException(status_code=404, detail="Config file not found")
    load_dotenv(USER_ENV_FILE)

# Read the .env file into a dictionary
def read_env_file():
    if not os.path.exists(USER_ENV_FILE):
        print(f"File {USER_ENV_FILE} not found")
        raise HTTPException(status_code=404, detail="Config file not found")
    return dotenv_values(USER_ENV_FILE)

# Write the .env file from a dictionary
def write_env_file(config):
    if not os.path.exists(USER_ENV_FILE):
        print(f"File {USER_ENV_FILE} not found")
        raise HTTPException(status_code=404, detail="Config file not found")
    for key, value in config.items():
        set_key(USER_ENV_FILE, key, value)
    print(f"Config written to file: {config}")

@app.get("/config", response_model=IPConfig)
async def get_config():
    config = read_env_file()
    return IPConfig(**config)

@app.put("/config")
async def update_config(new_config: IPConfig):
    config = new_config.dict()
    write_env_file(config)
    return {"message": "Config updated successfully"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001, log_level="debug")


'''
To test:

curl -X GET "http://127.0.0.1:8000/config"

curl -X PUT "http://127.0.0.1:8000/config" -H "Content-Type: application/json" -d '{
    "ETHERNET_ADDRESS": "00:0A:35:00:22:22",
    "IP_ADDRESS": "192.168.0.124",
    "IP_ADDRESS_NETMASK": "255.255.255.0",
    "GATEWAY": "192.168.0.1",
    "SECONDARY_IP_ADDRESS": "192.168.0.255",
    "SECONDARY_IP_ADDRESS_NETMASK": "255.255.255.0",
    "SECONDARY_GATEWAY": "192.168.0.1"
}'

'''
