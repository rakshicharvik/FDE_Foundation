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