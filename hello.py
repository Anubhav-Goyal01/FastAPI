from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/hi/{who}")
def greet(who: str):
    return f"Hello? {who}"


if __name__ == "__main__":
 uvicorn.run("hello:app", reload=True)