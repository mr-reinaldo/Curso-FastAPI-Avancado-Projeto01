from asyncio import gather
from typing import List
from fastapi import APIRouter, Path, Body
from fastapi import status

from utils.converter import async_converter
from schemas.converterInput import ConverterInput
from schemas.converterOutput import ConverterOutput


router = APIRouter()


@router.get(
    "/converter/{from_currency}/async",
    response_model=List[ConverterOutput],
    status_code=status.HTTP_200_OK,
)
async def async_converter_endpoint(
    body: ConverterInput = Body(...),
    from_currency: str = Path(max_length=3, regex="^[A-Z]{3}$"),
):
    to_currencies = body.to_currencies
    price = body.price

    tasks = [
        async_converter(from_currency, to_currency, price)
        for to_currency in to_currencies
    ]

    return await gather(*tasks)
