
from ..schemas import DiagnosticEvidence


MOCK_DEVICE_STATUS = {
    "DEV-003": {
        "reachable": False,
        "last_seen_seconds_ago": 7200,
        "connection_status": "timeout",
    }
}


def check_device_connectivity(
    device_id: str,
) -> DiagnosticEvidence:
    device = MOCK_DEVICE_STATUS.get(device_id)

    if device is None:
        return DiagnosticEvidence(
            device_id=device_id,
            check_name="check_device_connectivity",
            result={"error": "Device not found"},
        )

    return DiagnosticEvidence(
        device_id=device_id,
        check_name="check_device_connectivity",
        result=device.copy(),
    )
