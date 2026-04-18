import os
from dotenv import load_dotenv

# Load variables from .env file (only for local/dev)
load_dotenv()

name = os.getenv("NAME", "Guest")
city = os.getenv("CITY", "Unknown")

print(f"Hello {name} from {city}!")
