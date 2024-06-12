from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import List, Optional
import logging
import os
from dotenv import load_dotenv

app = FastAPI()

# Load environment variables from .env file
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '.env'))

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

class IPConfig(BaseModel):
    primary_address: str
    primary_netmask: str
    primary_gateway: str
    secondary_addresses: Optional[List[str]] = Field(default_factory=list)
    secondary_netmasks: Optional[List[str]] = Field(default_factory=list)
    secondary_gateways: Optional[List[str]] = Field(default_factory=list)

def load_ip_config() -> IPConfig:
    secondary_addresses = []
    secondary_netmasks = []
    secondary_gateways = []

    for key, value in os.environ.items():
        if key.startswith("secondary_address_"):
            secondary_addresses.append(value)
        elif key.startswith("secondary_netmask_"):
            secondary_netmasks.append(value)
        elif key.startswith("secondary_gateway_"):
            secondary_gateways.append(value)

    return IPConfig(
        primary_address=os.getenv("primary_address"),
        primary_netmask=os.getenv("primary_netmask"),
        primary_gateway=os.getenv("primary_gateway"),
        secondary_addresses=secondary_addresses,
        secondary_netmasks=secondary_netmasks,
        secondary_gateways=secondary_gateways
    )

@app.get("/ip-config")
async def read_ip_config():
    logger.debug("Attempting to read IP configuration from environment variables")
    try:
        config = load_ip_config()
        return config.dict()
    except Exception as e:
        logger.error(f"Error reading configuration: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@app.put("/ip-config")
async def update_ip_config(config: IPConfig):
    logger.debug(f"Attempting to update IP configuration with {config}")
    try:
        # Build environment variable data string
        env_data = f"primary_address={config.primary_address}\n"
        env_data += f"primary_netmask={config.primary_netmask}\n"
        env_data += f"primary_gateway={config.primary_gateway}\n"
        
        for i, addr in enumerate(config.secondary_addresses):
            env_data += f"secondary_address_{i+1}={addr}\n"
        
        for i, netmask in enumerate(config.secondary_netmasks):
            env_data += f"secondary_netmask_{i+1}={netmask}\n"
        
        for i, gateway in enumerate(config.secondary_gateways):
            env_data += f"secondary_gateway_{i+1}={gateway}\n"

        logger.debug(f"Writing environment data: {env_data}")
        with open(os.path.join(os.path.dirname(__file__), '.env'), 'w') as file:
            file.write(env_data)
        
        # Reload the .env file
        load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '.env'), override=True)
        
        return {"status": "success"}
    except Exception as e:
        logger.error(f"Error writing to configuration file: {e}")
        raise HTTPException(status_code=500, detail=str(e))