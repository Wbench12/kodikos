from fastapi import FastAPI, Depends
from pydantic import BaseModel
from model.database import DBSession, engine
from model import models
from fastapi import FastAPI
from schemas import CompanyInput
from fastapi.exceptions import HTTPException
from sqlalchemy.orm import Session
import requests
models.Base.metadata.create_all(bind=engine)
###
app=FastAPI()
###
def get_db():
    try:
        db = DBSession()
        yield db
    finally:
        db.close()

@app.get("/companies")
def read_companies(db: Session = Depends(get_db)):
    companies = db.query(models.Company).all()
    return companies
@app.post("/signup")
def add_company(company:CompanyInput, db: Session = Depends(get_db)):
        if len(company.company_name) == 0 or len(company.company_password) == 0 or len(company.login_email) == 0:
            raise HTTPException(
                status_code=400, detail={
                    "status": "Error 400 - Bad Request",
                    "message": "email and password and name fields are all required"
                })
        new_company = models.Company(
            company_name=company.company_name, login_email=company.login_email,company_password=company.company_password, company_description=company.company_description, company_prior_collaborations_and_partnerships=company.company_prior_collaborations_and_partnerships, company_service_name= company.company_service_name, company_service_description= company.company_service_description,contact_tel1=company.contact_tel1 ,contact_tel2=company.contact_tel2, website_url=company.website_url,contact_email=company.contact_email)
        db.add(new_company)
        db.commit()
        db.refresh(new_company)
        return new_company
@app.get("/services/{company_service_name}")
def get_company_list(company_service_name:str, db: Session = Depends(get_db)):
    companies=db.query(models.Company).filter(models.Company.company_service_name==company_service_name).all()
    return companies
