import requests
from bs4 import BeautifulSoup

def scrape_linkedin_page(page_id: str):
    url = f"https://www.linkedin.com/company/{page_id}/"
    headers = {"User-Agent": "Mozilla/5.0"}
    
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        return None

    soup = BeautifulSoup(response.text, "html.parser")

    # Extract Page Name
    page_name = soup.find("title").text.strip() if soup.find("title") else "Unknown"

    # Extract Description
    description = soup.find("meta", {"name": "description"})["content"] if soup.find("meta", {"name": "description"}) else "No description"

    # Extract Industry (example selector, may need adjustment)
    industry = "Unknown"
    industry_tag = soup.find("dd", {"class": "org-page-details__definition-text"})
    if industry_tag:
        industry = industry_tag.text.strip()

    # Extract Followers (example selector, may need adjustment)
    followers = 0
    followers_tag = soup.find("div", {"class": "org-top-card-summary-info-list__info-item"})
    if followers_tag:
        followers_text = followers_tag.text.strip()
        if "followers" in followers_text:
            followers = int(followers_text.replace("followers", "").replace(",", "").strip())

    # Extract Headcount (example selector, may need adjustment)
    headcount = 0
    headcount_tag = soup.find("dd", {"class": "org-about-company-module__company-size-definition-text"})
    if headcount_tag:
        headcount_text = headcount_tag.text.strip()
        if "employees" in headcount_text:
            headcount = int(headcount_text.replace("employees", "").replace(",", "").strip())

    # Extract Specialities (example selector, may need adjustment)
    specialities = []
    specialities_tag = soup.find("dd", {"class": "org-page-details__definition-text"})
    if specialities_tag:
        specialities = [s.strip() for s in specialities_tag.text.split(",")]

    return {
        "page_id": page_id,
        "name": page_name,
        "url": url,
        "profile_picture": "https://via.placeholder.com/150",  # Placeholder
        "description": description,
        "website": "https://example.com",  # Placeholder
        "industry": industry,
        "followers": followers,
        "headcount": headcount,
        "specialities": specialities
    }