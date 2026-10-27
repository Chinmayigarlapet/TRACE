
from sqlalchemy.orm import Session

from .database import Base, engine
from .models import Device


SAMPLE_DEVICES = [
    {
        "device_id": "DEV-001",
        "name": "Power Monitoring Device",
        "device_type": "PowerMeter",
        "firmware_version": "4.1.0",
        "status": "online",
        "ip_address": "192.168.1.101",
    },
    {
        "device_id": "DEV-002",
        "name": "Industrial Controller",
        "device_type": "Controller",
        "firmware_version": "2.3.0",
        "status": "online",
        "ip_address": "192.168.1.102",
    },
    {
        "device_id": "DEV-003",
        "name": "Remote Monitoring Unit",
        "device_type": "MonitoringUnit",
        "firmware_version": "1.5.2",
        "status": "offline",
        "ip_address": "192.168.1.103",
    },
]


def seed_devices():
    Base.metadata.create_all(bind=engine)

    with Session(engine) as session:
        for data in SAMPLE_DEVICES:
            existing = session.get(Device, data["device_id"])

            if existing is None:
                session.add(Device(**data))

        session.commit()

    print("Device database initialized successfully.")


if __name__ == "__main__":
    seed_devices()
