from pymongo import MongoClient
from models.page import PageCreate

client = MongoClient("mongodb://localhost:27017/")
db = client["linkedin_insights"]
pages_collection = db["pages"]

def save_page(page: PageCreate):
    page_dict = page.dict()
    result = pages_collection.insert_one(page_dict)
    return str(result.inserted_id)

from bson import ObjectId
from models.page import Page

def get_page(page_id: str):
    page = pages_collection.find_one({"page_id": page_id})
    if page:
        page["_id"] = str(page["_id"])  # Convert ObjectId to string
        return Page(**page)  # Transform to Pydantic model
    return None