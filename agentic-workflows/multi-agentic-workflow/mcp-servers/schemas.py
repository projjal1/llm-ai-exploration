from pydantic import BaseModel

# Interest rate model class
class InterestRates(BaseModel):
    interest_rate: float
    bank_name: str