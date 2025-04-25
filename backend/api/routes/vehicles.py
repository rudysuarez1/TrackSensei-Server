from fastapi import APIRouter, HTTPException
from typing import List
from .schemas.vehicles import Vehicle, VehicleCreate  # Import the updated schemas

router = APIRouter()

# In-memory storage for demonstration purposes
vehicles_db = {}


@router.post("/vehicles/", response_model=Vehicle)
async def create_vehicle(vehicle: VehicleCreate):  # Use VehicleCreate for input
    vehicle_id = len(vehicles_db) + 1  # Simple ID generation for demonstration
    new_vehicle = Vehicle(id=vehicle_id, **vehicle.dict())  # Create a Vehicle instance
    vehicles_db[vehicle_id] = new_vehicle
    return new_vehicle


@router.get("/vehicles/{vehicle_id}", response_model=Vehicle)
async def get_vehicle(vehicle_id: int):
    vehicle = vehicles_db.get(vehicle_id)
    if not vehicle:
        raise HTTPException(status_code=404, detail="Vehicle not found")
    return vehicle


@router.delete("/vehicles/{vehicle_id}", response_model=dict)
async def delete_vehicle(vehicle_id: int):
    if vehicle_id not in vehicles_db:
        raise HTTPException(status_code=404, detail="Vehicle not found")
    del vehicles_db[vehicle_id]
    return {"detail": "Vehicle deleted"}
