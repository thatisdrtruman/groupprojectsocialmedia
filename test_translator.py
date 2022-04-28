import unittest
import translator as Trans


class MyTestCase(unittest.TestCase):
    def test_translator(self):
        self.assertEqual('Comments before modification', Trans.getTransText('修改之前的注释'))


if __name__ == '__main__':
    unittest.main()