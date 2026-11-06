from dataclasses import dataclass

@dataclass(frozen=True)
class CameraPose:
    pan: float = 0.0
    tilt: float = 0.0


def set_camera_pose(pan: float, tilt: float, emergency_stop: bool = False) -> CameraPose:
    """Validate a simulated camera orientation; never actuates hardware."""
    if emergency_stop:
        raise RuntimeError("Emergency stop active")
    if not (-90 <= pan <= 90 and -45 <= tilt <= 45):
        raise ValueError("Camera pose outside allowed range")
    return CameraPose(float(pan), float(tilt))
