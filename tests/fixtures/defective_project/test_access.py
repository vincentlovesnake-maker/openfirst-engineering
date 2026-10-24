import unittest

from access import can_read_document


class AccessTests(unittest.TestCase):
    def test_owner_can_read(self):
        self.assertTrue(can_read_document("alice", "alice"))

    def test_other_user_cannot_read_private_document(self):
        self.assertFalse(can_read_document("mallory", "alice"))


if __name__ == "__main__":
    unittest.main()
