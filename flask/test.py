import unittest
import app

class TestFlask(unittest.TestCase):

    def setUp(self):
        self.app = app.app.test_client()

    def test_save_values(self):
        response = self.app.post('/', data=dict(submit='save', key='2', cache_value='two'))
        assert response.status_code == 200
        assert b'2' in response.data
        assert b'two' in response.data

if __name__ == 'main':
    unittest.main()