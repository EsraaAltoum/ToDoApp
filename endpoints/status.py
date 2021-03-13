from fastapi import APIRouter
import requests
router = APIRouter()
authToken= "Bearer mi5qSSqdhmrNXBjLq5MBMwuqcS0q8aE4u52fwqrG8CkrBjjksgdV8ZblHdh4ThtDqQVFapfOwrCqadcTH4sJIMhQgEcWpc0bK_9ms_rJ1H-xMT1Amp4tmH_PhAg3X3Yx"

#make get endpoint and specify path
@router.get("/parkinglots/{location}")
def get_parking_lots(location: str):
    headers = {
        'Authorization': authToken
    }
    #making request to yelp api from our api and storing result
    result= requests.get("https://api.yelp.com/v3/businesses/search?location="+location+"&term=parking", headers= headers)
    print(result)
    return result





