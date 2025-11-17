from fastapi import FastAPI

app = FastAPI()

@app.get("/health")
async def health():
  return {"status": "ok", "app_health": "healthy"}

@app.get("/")
async def route():
  return {"Hello": "World"}

@app.get("/doc")
async def doc():
  return "Hi DOCTOR!"

@app.get("/intro")
async def intro():
   return "Hi Rakshi!"

@app.get("/lap")
async def lap():
   return "laptop!"

@app.get("/add")
async def add(x=10,y=20):
  res=x+y
  return {"result":res}

@app.get("/mul")
async def mul(x=20,y=2):
  res1=x*y
  return {"result":res1}

@app.get("div")
async def div(x=10,y=2):
  ans=x/y
  return {"result":ans}


