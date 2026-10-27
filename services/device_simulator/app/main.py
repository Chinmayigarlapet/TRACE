
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session

from .database import Base, engine, get_db
from .models import Device
from .schemas import (
    DeviceListResponse,
    DeviceResponse,
    DeviceStatusResponse,
)

app = FastAPI(
    title="TRACE Device Simulator",
    description="Simulated enterprise device management service",
    version="0.1.0",
)


@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "service": "device-simulator",
    }


@app.get("/devices", response_model=DeviceListResponse)
def list_devices(db: Session = Depends(get_db)):
    devices = db.scalars(select(Device)).all()

    return {
        "devices": devices,
        "count": len(devices),
    }


@app.get("/devices/{device_id}", response_model=DeviceResponse)
def get_device(
    device_id: str,
    db: Session = Depends(get_db),
):
    device = db.get(Device, device_id)

    if device is None:
        raise HTTPException(
            status_code=404,
            detail="Device not found",
        )

    return device


@app.get(
    "/devices/{device_id}/status",
    response_model=DeviceStatusResponse,
)
def get_device_status(
    device_id: str,
    db: Session = Depends(get_db),
):
    device = db.get(Device, device_id)

    if device is None:
        raise HTTPException(
            status_code=404,
            detail="Device not found",
        )

    return {
        "device_id": device.device_id,
        "status": device.status,
    }
