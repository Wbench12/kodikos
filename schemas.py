from pydantic import BaseModel
from typing import Optional

class CompanyInput(BaseModel):
    company_name : str
    login_email : str
    company_password : str
    company_service_name  :str
    company_service_description:Optional[str]
    company_description:str
    company_prior_collaborations_and_partnerships:Optional[str]
    contact_email:Optional[str]
    contact_tel1:Optional[str]
    contact_tel2:Optional[str]
    website_url:Optional[str]