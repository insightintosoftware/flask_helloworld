import unittest
import app

class TestMy(unittest.TestCase):
    def test_first(self):
        print("hellow!!!")
        app.hello_world()


if __name__ == '__main__':
    unittest.main()