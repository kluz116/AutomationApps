from ninja import NinjaAPI

api = NinjaAPI()


@api.get("/add")
def add(request, a: int, b: int):
    return {"result": a + b}
@api.get("/cap/cap_id")
def cap_id(request):
    return request
