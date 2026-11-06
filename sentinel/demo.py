from .motion import set_camera_pose
from .aqua import decide_irrigation

if __name__ == "__main__":
    print("Camera simulation:", set_camera_pose(20, -10))
    print("Irrigation simulation:", decide_irrigation(25, 40, True))
