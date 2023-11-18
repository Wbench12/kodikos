from sqlalchemy import Column, Integer, String
from model.database import Base
class Company(Base):
    __tablename__ = "companies"
    id = Column(Integer, primary_key=True , nullable=False)
    company_name = Column(String, nullable=False)
    login_email = Column(String, nullable=False)
    company_password = Column(String, nullable=False)
    company_service_name = Column(String, nullable=False)
    company_service_description=Column(String, nullable=True)
    company_description=Column(String, nullable=False)
    company_prior_collaborations_and_partnerships=Column(String, nullable=True)
    contact_email=Column(String, nullable=True)
    contact_tel1=Column(String, nullable=True)
    contact_tel2=Column(String, nullable=True)
    website_url=Column(String, nullable=True)
    def __repr__(self):
     return f'Company(id={self.id},company_name={self.company_name},login_email={self.login_email},compoany_description={self.company_description},company_password={self.company_password},company_service_name={self.company_service_name},company_service_description={self.company_service_description},company_prior_collaborations_and_partnership={self.company_prior_collaborations_and_partnerships}, contact_email={self.contact_email},contact_tel1={self.contact_tel1},contact_tel2={self.contact_tel2},website_url={self.website_url})'
      