import unittest
import cambia_texto


class Probar_cambiartexto(unittest.TestCase):
    def test_muyusculas(self):
        palabra = "Buen dia "
        resultado = cambia_texto.todo_mayuscula(palabra)
        self.assertEqual(resultado, "BUEN DIA")


if __name__ == "__main__":
    unittest.main()
