from fastapi import FastAPI
from app.models.Polls import Poll, PollCreate

app = FastAPI()


@app.get("/test")
def test():
    return {"message": "Hello World"}


@app.post("/polls/create")
def create_poll(poll: PollCreate) -> Poll:
    return Poll(
        title="some placeholder title",
        options=["yes", "no", "maybe"],
    )
