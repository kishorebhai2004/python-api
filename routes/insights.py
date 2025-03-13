from fastapi import APIRouter, HTTPException
from services.scraper import scrape_linkedin_page
from services.database import save_page, get_page
from models.page import PageCreate, Page

router = APIRouter()

@router.get("/pages/{page_id}", response_model=Page)
async def get_page_details(page_id: str):
    # Check if page exists in DB
    page = get_page(page_id)
    if page:
        return page

    # Scrape LinkedIn page if not in DB
    scraped_data = scrape_linkedin_page(page_id)
    if not scraped_data:
        raise HTTPException(status_code=404, detail="Page not found")

    # Save scraped data to DB
    page_create = PageCreate(**scraped_data)
    save_page(page_create)

    # Fetch the saved page from DB and return it
    saved_page = get_page(page_id)
    return saved_page