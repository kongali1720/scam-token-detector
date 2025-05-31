import unittest
from app import app

class ScamDetectorWebUITest(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_homepage_loads(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Scam Token Detector', response.data)

    def test_scan_with_valid_input(self):
        response = self.app.post('/', data=dict(
            contract_address='0xdeadbeefdeadbeefdeadbeefdeadbeefdeadbeef'
        ))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Scam Detected', response.data)

    def test_scan_with_empty_input(self):
        response = self.app.post('/', data=dict(contract_address=''))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Please enter a valid contract address.', response.data)

    def test_scan_with_safe_address(self):
        response = self.app.post('/', data=dict(
            contract_address='0x1234567890123456789012345678901234567890'
        ))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Token appears to be safe.', response.data)

if __name__ == '__main__':
    unittest.main()
