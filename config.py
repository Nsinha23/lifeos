from dotenv import load_dotenv  #bring me load dotenv tool
import os                       # bring me mac OS tool  

load_dotenv()

CLAUDE_API_KEY = os.getenv("CLAUDE_API_KEY")    # constant name set to call the call claude api from envrionment on the project
APP_NAME = os.getenv("APP_NAME")                # constant name set to call app name from the environment


print(APP_NAME, "is starting up!")              # print the project name and statement