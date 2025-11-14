# Database operations handler for loan management system
# This module contains functions to interact with the loan database maintained on mongodb

from pymongo import MongoClient
from typing import Optional, Dict, Any
from .schemas import InterestRates

client = MongoClient("mongodb://localhost:27017/")
db = client["loan_management"]
loans_collection = db["loans"]

# Fetch interest rates based on loan type from the database
def get_interest_rates_by_loan_type(loan_type: str) -> list[InterestRates]:
    resultset = loans_collection.find({"loan_type": loan_type}, {"_id": 0, "interest_rate": 1, "bank_name": 1})

    interest_data = []
    for result in resultset:
        interest_data.append(InterestRates(result))

    return interest_data