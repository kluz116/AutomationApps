from django.shortcuts import get_object_or_404
from ninja import NinjaAPI
from innovations.models import Innovations
from datetime import date
from ninja import Schema
from typing import List

api = NinjaAPI()


class InnovationIn(Schema):
    name: str
    email: str
    description: str


class InnovationOut(Schema):
    id: int
    name: str
    email: str
    description: str


@api.post("/innovation")
def create_innovation(request, payload: InnovationIn):
    obj = Innovations.objects.create(**payload.dict())
    # return {"id": obj.id}
    return {"response": "Successfully created"}


@api.put("/innovations/{innovation_id}")
def update_employee(request, innovation_id: int, payload: InnovationIn):
    employee = get_object_or_404(Innovations, id=innovation_id)
    for attr, value in payload.dict().items():
        setattr(employee, attr, value)
    employee.save()
    return {"success": True}


@api.get("/innovations", response=List[InnovationOut])
def list_innovations(request):
    qs = Innovations.objects.all()
    return qs
