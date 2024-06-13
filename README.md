IP Configuration Management API DocumentationOverviewThis FastAPI application provides an API for managing IP configuration settings stored in a .env file. The application allows users to retrieve and update the IP configuration through HTTP requests.EndpointsGet ConfigurationGET /configRetrieves the current IP configuration.Response Model:IPConfigETHERNET_ADDRESS (str): The Ethernet address.IP_ADDRESS (str): The primary IP address.IP_ADDRESS_NETMASK (str): The netmask for the primary IP address.GATEWAY (str): The gateway for the primary IP address.SECONDARY_IP_ADDRESS (str): The secondary IP address.SECONDARY_IP_ADDRESS_NETMASK (str): The netmask for the secondary IP address.SECONDARY_GATEWAY (str): The gateway for the secondary IP address.Responses:200 OK: Returns the current configuration.404 Not Found: If the configuration file does not exist.Example Request:curl -X GET "http://localhost:8000/config" -H "accept: application/json"Example Response:{
    "ETHERNET_ADDRESS": "00:1B:44:11:3A:B7",
    "IP_ADDRESS": "192.168.1.10",
    "IP_ADDRESS_NETMASK": "255.255.255.0",
    "GATEWAY": "192.168.1.1",
    "SECONDARY_IP_ADDRESS": "192.168.1.11",
    "SECONDARY_IP_ADDRESS_NETMASK": "255.255.255.0",
    "SECONDARY_GATEWAY": "192.168.1.1"
}Update ConfigurationPUT /configUpdates the IP configuration.Request Body:IPConfigETHERNET_ADDRESS (str): The Ethernet address.IP_ADDRESS (str): The primary IP address.IP_ADDRESS_NETMASK (str): The netmask for the primary IP address.GATEWAY (str): The gateway for the primary IP address.SECONDARY_IP_ADDRESS (str): The secondary IP address.SECONDARY_IP_ADDRESS_NETMASK (str): The netmask for the secondary IP address.SECONDARY_GATEWAY (str): The gateway for the secondary IP address.Responses:200 OK: If the configuration was updated successfully.404 Not Found: If the configuration file does not exist.Example Request:curl -X PUT "http://localhost:8000/config" -H "accept: application/json" -H "Content-Type: application/json" -d '{
    "ETHERNET_ADDRESS": "00:1B:44:11:3A:B8",
    "IP_ADDRESS": "192.168.1.20",
    "IP_ADDRESS_NETMASK": "255.255.255.0",
    "GATEWAY": "192.168.1.1",
    "SECONDARY_IP_ADDRESS": "192.168.1.21",
    "SECONDARY_IP_ADDRESS_NETMASK": "255.255.255.0",
    "SECONDARY_GATEWAY": "192.168.1.1"
}'Example Response:{
    "message": "Config updated successfully"
}Error HandlingCommon Errors404 Not Found: Returned if the configuration file (user.env) is not found.Example Error Response:{
    "detail": "Config file not found"
}Utility Functionsload_config()Loads the environment variables from the user.env file. Raises an HTTPException with status code 404 if the file is not found.read_env_file()Reads the environment variables from the user.env file and returns them as a dictionary. Raises an HTTPException with status code 404 if the file is not found.write_env_file(config)Writes the provided configuration dictionary to the user.env file. Raises an HTTPException with status code 404 if the file is not found.Running the ApplicationTo run the FastAPI application, execute the following command:uvicorn main:app --host 0.0.0.0 --port 8000 --log-level debugThis will start the application on http://0.0.0.0:8000.NotesEnsure that the user.env file exists in the same directory as the application.The application uses the python-dotenv library to manage environment variables in the .env file.