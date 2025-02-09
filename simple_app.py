from fastapi import FastAPI, Depends, Request, Query, Body

app = FastAPI(title="Task Manager API")


def get_data_dict(id: int, request: Request):
    print(request)
    return {"data": "Hello, World!", "id": id}


def default_pagination(
    skip: int | None = Query(default=0, description="Pagination offset"),
    limit: int | None = Query(default=100, description="Number of items per page"),
):
    return {"skip": skip, "limit": limit}



@app.get("/{id}")
async def get(
    data=Depends(get_data_dict),
    data1=Depends(get_data_dict),
    pagination=Depends(default_pagination),
    q=Query(str, description="Query parameter"),
):
    print(data1)
    return data


def get_data_dict(data: dict = Body(...), query: str = Query(None)):
    return data, query


@app.post("/")
async def post(data=Depends(get_data_dict)):
    return data


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
