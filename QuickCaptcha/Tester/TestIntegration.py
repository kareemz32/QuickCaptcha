import unittest
from solver_functions import *
# from solver import *


class TestIntegration(unittest.TestCase):

    # Test Case 1: Extracting the keyword from the CAPTCHA
    def test_get_keyword(self):

        self.key = string_processing(
            "Select all squares with\ntraffic lights\nIf there are none, click skip\nSKIP").upper().replace(" ", "")
        self.assertEqual(self.key, "TRAFFICLIGHTS")

        self.key = string_processing(
            "Select all images with\na fire hydrant\nClick verify once there are none left.\nVERIFY").upper().replace(" ", "")
        self.assertEqual(self.key, "FIREHYDRANT")

        self.key = string_processing(
            "Select all images with a\nbus\nClick verify once there are none left.\nVERIFY").upper().replace(" ", "")
        self.assertEqual(self.key, "BUS")

        self.key = string_processing(
            "Select all squares with\nvehicles\nIf there are none, click skip\nSKIP").upper().replace(" ", "")
        self.assertEqual(self.key, "VEHICLES")

        self.key = string_processing(
            "Select all images with\nstairs\nVERIFY").upper().replace(" ", "")
        self.assertEqual(self.key, "STAIRS")

    # Test Case 2: Retrieving the plural version of the keyword
    def test_get_keyword_plural(self):

        self.key = get_plural_key(string_processing(
            "Select all squares with\na stop sign\nIf there are none, click skip\nSKIP").upper().replace(" ", ""))
        self.assertEqual(self.key, "STOPSIGNS")

        self.key = get_plural_key(string_processing(
            "Select all squares with\na sidewalk\nIf there are none, click skip\nSKIP").upper().replace(" ", ""))
        self.assertEqual(self.key, "SIDEWALKS")

        self.key = get_plural_key(string_processing(
            "Select all squares with\ntruck\nIf there are none, click skip\nSKIP").upper().replace(" ", ""))
        self.assertEqual(self.key, "TRUCKS")

        self.key = get_plural_key(string_processing(
            "Select all squares with\na tree\nIf there are none, click skip\nSKIP").upper().replace(" ", ""))
        self.assertEqual(self.key, "TREES")

        self.key = get_plural_key(string_processing(
            "Select all squares with\na mountain\nIf there are none, click skip\nSKIP").upper().replace(" ", ""))
        self.assertEqual(self.key, "MOUNTAINS")

    # Test Case 3: Checking the special case of the keyword

    def test_get_special_case(self):

        self.key = check_special_case(get_plural_key(string_processing(
            "Select all squares with\na motorcycle\nIf there are none, click skip\nSKIP").upper().replace(" ", "")))
        # In solver.py add 'MOTORCYCLES' to check_specialCase
        self.assertEqual(self.key, "BIKE")

        self.key = check_special_case(get_plural_key(string_processing(
            "Select all squares with\na trafficlight\nIf there are none, click skip\nSKIP").upper().replace(" ", "")))
        self.assertEqual(self.key, "STREETLIGHT")

        self.key = check_special_case(get_plural_key(string_processing(
            "Select all squares with\na vehicle\nIf there are none, click skip\nSKIP").upper().replace(" ", "")))
        self.assertEqual(self.key, "CAR")

        self.key = check_special_case(get_plural_key(string_processing(
            "Select all squares with\na bicycle\nIf there are none, click skip\nSKIP").upper().replace(" ", "")))
        self.assertEqual(self.key, "BIKE")

        self.key = check_special_case(get_plural_key(string_processing(
            "Select all squares with\na crosswalk\nIf there are none, click skip\nSKIP").upper().replace(" ", "")))
        self.assertEqual(self.key, "CROSSWALKS")


if __name__ == '__main__':
    unittest.main()
