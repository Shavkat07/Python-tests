from unittest import TestCase, main

from calculator import calculator


class MyTestCase(TestCase):
    def test_plus(self):
        self.assertEqual(calculator('2+2'), 4)

    def test_minus(self):
        self.assertEqual(calculator('8-2'), 6)

    def test_multi(self):
        self.assertEqual(calculator('4*4'), 16)

    def test_divide(self):
        self.assertEqual(calculator('8/2'), 4)

    def test_no_signs(self):
        with self.assertRaises(ValueError) as e:
            calculator('asggasdgggsf')
        self.assertEqual('Должно содержать хотя бы один знак +-*/', e.exception.args[0])

    def test_two_signs(self):
        with self.assertRaises(ValueError) as e:
            calculator('2+2+2')
        self.assertEqual('Выражение должно содержать 2 целых числа и 1 знак', e.exception.args[0])

    def test_many_signs(self):
        with self.assertRaises(ValueError) as e:
            calculator('2+2*2')
        self.assertEqual('Выражение должно содержать 2 целых числа и 1 знак', e.exception.args[0])

    def test_no_ints(self):
        with self.assertRaises(ValueError) as e:
            calculator('2.7+2.9')
        self.assertEqual('Выражение должно содержать 2 целых числа и 1 знак', e.exception.args[0])

    def test_strings(self):
        with self.assertRaises(ValueError) as e:
            calculator('a+g')
        self.assertEqual('Выражение должно содержать 2 целых числа и 1 знак', e.exception.args[0])


if __name__ == '__main__':
    main()
