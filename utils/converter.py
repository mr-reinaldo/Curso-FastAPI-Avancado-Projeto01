from requests import get
from fastapi import HTTPException, status
from aiohttp import ClientSession


# Função que converte uma moeda para outra (síncrona)
def sync_converter(from_currency: str, to_currency: str, price: float):
    url = f"http://economia.awesomeapi.com.br/json/last/{from_currency}-{to_currency}"

    try:
        response = get(url=url)
        data = response.json()
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Erro ao acessar API: {e}",
        )

    if not data:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Dados não encontrados",
        )

    ask_bid = float(
        data.get(f"{from_currency}{to_currency}").get("bid")
    )  # bid é o valor de compra

    return {
        "from_currency": from_currency,
        "to_currency": to_currency,
        "price": price,
        "converted_price": price * ask_bid,
    }


# Função que converte uma moeda para outra (assíncrona)
async def async_converter(from_currency: str, to_currency: str, price: float):
    url = f"http://economia.awesomeapi.com.br/json/last/{from_currency}-{to_currency}"

    async with ClientSession() as session:
        async with session.get(url) as response:
            data = await response.json()

    if not data:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Dados não encontrados",
        )

    ask_bid = float(
        data.get(f"{from_currency}{to_currency}").get("bid")
    )  # bid é o valor de compra

    print(ask_bid)

    return {
        "from_currency": from_currency,
        "to_currency": to_currency,
        "price": price,
        "converted_price": price * ask_bid,
    }
