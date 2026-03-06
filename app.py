from supabase import create_client
from dotenv import load_dotenv
import os

load_dotenv()

url = os.getenv("URL")
key = os.getenv("KEY")

supabase = create_client(url, key)

name = input("Enter name: ")
message = input("Enter message: ")

supabase.table("feedback").insert({
    "name": name,
    "message": message
}).execute()

print("Data inserted successfully")