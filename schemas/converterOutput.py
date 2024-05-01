from pydantic import BaseModel, Field


class ConverterOutput(BaseModel):
    """
    {
        "from_currency": "BRL",
        "to_currency": "USD",
        "price": 100.0,
        "converted_price": 20.0
    }
    """

    from_currency: str = Field(..., max_length=3, pattern="^[A-Z]{3}$")
    to_currency: str = Field(..., max_length=3, pattern="^[A-Z]{3}$")
    price: float = Field(..., gt=0)
    converted_price: float = Field(..., gt=0)
