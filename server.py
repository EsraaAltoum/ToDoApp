import uvicorn
from fastapi import FastAPI

from endpoints.status import router

app = FastAPI(title= 'parkinglotApi')
app.include_router(router)

if __name__ == "__main__":
    uvicorn.run(app, host= "0.0.0.0", port= 9011)





