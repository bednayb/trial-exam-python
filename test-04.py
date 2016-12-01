import exercise_04
import unittest

class Test_your_name_work(unittest.TestCase):



    def test_string(self):
        self.assertEqual(exercise_04.greeter('Aniko'), 'Hello, Aniko!')

    def test_nothing(self):
        self.assertEqual(exercise_04.greeter(''), 'Hello, Mr Nobody!' )

if __name__ == '__main__':
    unittest.main()
