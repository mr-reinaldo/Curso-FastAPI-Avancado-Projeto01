from pydantic import BaseModel, Field, field_validator
from typing import List
from re import match


class ConverterInput(BaseModel):
    """
    {
        "price": 100.0,
        "to_currencies": ["USD", "EUR"]
    }
    """

    price: float = Field(..., gt=0)
    to_currencies: List[str]

    @field_validator("to_currencies")
    def validate_to_currency(cls, value):
        for currency in value:
            if not match("^[A-Z]{3}$", currency):
                raise ValueError("Moeda inválida")

        return value
