from asyncio import gather
from typing import List
from fastapi import APIRouter, Path, Body
from fastapi import status

from utils.converter import sync_converter
from schemas.converterInput import ConverterInput
from schemas.converterOutput import ConverterOutput


router = APIRouter()


@router.get(
    "/converter/{from_currency}/sync",
    response_model=List[ConverterOutput],
    status_code=status.HTTP_200_OK,
)
def sync_converter_endpoint(
    body: ConverterInput = Body(...),
    from_currency: str = Path(max_length=3, regex="^[A-Z]{3}$"),
):
    to_currencies = body.to_currencies
    price = body.price

    result = []

    for currency in to_currencies:
        response = sync_converter(
            from_currency=from_currency, to_currency=currency, price=price
        )

        result.append(response)

    return result
