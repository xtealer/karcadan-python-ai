from fastapi import FastAPI,Request
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/ping")
async def ping():
    return "Hello, I am alive" 

# endpoint for exit status model
@app.post("/exit")
async def section(request: Request):

    data = await request.json()
    from exit_status import predict
    result = predict(data)
    return {"prediction": result}


# endpoint for follow on funding model
@app.post("/funding")
async def section(request: Request):

    data = await request.json()

    from funding import make_predictions
    answer = make_predictions(data)

    return {"Answer": answer}



