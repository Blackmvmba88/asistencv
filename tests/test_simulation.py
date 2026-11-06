import unittest
from sentinel.motion import set_camera_pose
from sentinel.aqua import decide_irrigation

class MotionTests(unittest.TestCase):
    def test_center(self):
        self.assertEqual(set_camera_pose(0, 0).pan, 0)

    def test_reject_limit(self):
        with self.assertRaises(ValueError):
            set_camera_pose(91, 0)

    def test_emergency_stop(self):
        with self.assertRaises(RuntimeError):
            set_camera_pose(0, 0, True)

class AquaTests(unittest.TestCase):
    def test_dry_soil(self):
        self.assertTrue(decide_irrigation(20, 40, True).request_water)

    def test_empty_tank(self):
        self.assertFalse(decide_irrigation(20, 40, False).request_water)

    def test_runtime_limit(self):
        self.assertFalse(decide_irrigation(20, 40, True, 120).request_water)

    def test_wet_soil(self):
        self.assertFalse(decide_irrigation(60, 40, True).request_water)

if __name__ == "__main__":
    unittest.main()
