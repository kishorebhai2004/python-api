from pydantic import BaseModel, Field  # Add Field here
from typing import List, Optional

class PageBase(BaseModel):
    page_id: str
    name: str
    url: str
    profile_picture: str
    description: str
    website: Optional[str] = None
    industry: str
    followers: int
    headcount: int
    specialities: List[str]

class PageCreate(PageBase):
    pass

class Page(PageBase):
    id: str = Field(alias="_id")  # Use Field here

    class Config:
        from_attributes = True
        populate_by_name = True  # Allow aliasing