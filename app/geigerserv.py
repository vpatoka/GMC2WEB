"""
A webserver which receives and processes GMC Counter POST requests
and save it to flat CSV file.
"""
import os
import csv
import socket
import logging
import datetime
import asyncio
import aiohttp
from fastapi import FastAPI, Request, HTTPException, Query, Depends
from fastapi.responses import StreamingResponse, HTMLResponse, RedirectResponse

HOME = os.environ["HOME_HOSTNAME"]
FORWARD_TO_GMC = os.environ.get("FORWARD_TO_GMC", False)
logger = logging.getLogger(__name__)
app = FastAPI()

@app.get("/upload")
async def upload_data(
    request: Request,
    AID: str    = Query(..., description="User ID"),
    GID: str    = Query(..., description="Geiger Counter ID"),
    CPM: int    = Query(..., description="Counts per Minute"),
    ACPM: float = Query(..., description="Average counts per minute"),
    uSV: float  = Query(..., description="Value in Micro sieverts."),
):
    """
    Stores the datapoint defined by the request Query arguments.
    """
    if FORWARD_TO_GMC:
        # we forward the data to geiger map website
        try:
            async with aiohttp.ClientSession() as session:
                params = {"AID": AID, "GID": GID, "CPM": CPM, "ACPM": ACPM, "uSV": uSV}
                async with session.get(
                    "http://www.gmcmap.com/log2.asp", params=params, timeout=1.0
                ) as response:
                    logger.debug(f"Response from gmcmap: {response.status}")
        except Exception:
            logger.warning("Error forwarding request to geigermap", exc_info=True)

    with open('app/app_data/GMC.csv', 'a') as csvFile:
      csv_file = csv.writer(csvFile, delimiter = '|')
      csv_file.writerow([AID, GID, CPM, ACPM, uSV])

      csvFile.close()
      return HTMLResponse("OK.ERR0")

    return HTMLResponse("OK.ERR0")


@app.get("/")
async def home():
    url_list = [{"path": route.path, "name": route.name} for route in app.routes]
    return url_list
