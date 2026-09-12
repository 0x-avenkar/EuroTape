import asyncio

import httpx


async def main():

    params = {
        "geo": "EA",
        # "geo": "INVALID_GEO",
        "coicop": "CP00",
        "unit": "RCH_A",
        "format": "JSON",
        "lang": "en",
    }

    async with httpx.AsyncClient() as client:
        response = await client.get(
            "https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/prc_hicp_manr?",
            params=params,
        )

        data = response.json()
        print(data.keys())


asyncio.run(main())
