import glob
import json
from unittest import TestCase


class DataTest(TestCase):
    """Obey the testing goat."""

    def test_metadata_file_updated(self):
        """
        A testing template -- make to update tests.yml if you change the
        testing name.
        """

        with open("data/harvard/missing-files.json") as f:
            data = json.load(f)

        self.assertEqual(
            len(glob.glob("data/harvard/*/*.json")),
            len(data),
            msg="The number of files in data/harvard/ is not equal to the number of files in missing-files.json",
        )
