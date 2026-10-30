
from pydantic import BaseModel, ConfigDict


class DeviceResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    device_id: str
    name: str
    device_type: str
    firmware_version: str
    status: str
    ip_address: str


class DeviceListResponse(BaseModel):
    devices: list[DeviceResponse]
    count: int


class DeviceStatusResponse(BaseModel):
    device_id: str
    status: str
