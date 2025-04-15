import unittest
from mi_paquete import module

class TestModule(unittest.TestCase):
    def test_saludar(self):
        self.assertEqual(module.saludar(), "Hola desde mi_paquete")

if __name__ == '__main__':
    unittest.main()
