from fastapi import FastAPI

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def home():
    return {"message": "Hello World"}



"""l = {
    "1": "Apple",
    "2": "Banana",
    "3": "Mango",  
    "4" : "Grapes",            
     "5" : "Orange" }

@app.get("/getList/")
def home():
    return l """

"""
@app.post("/postList/")
async def home(request: Request):
    body = await request.json()
    print("Method:", request.method)
    print("URL:", request.url)
    print("Headers:",dict(request.headers))
    print("Body:", body.decode('utf-8'))
    return {"message": "GMR Luxury Properties"} """
