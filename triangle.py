def area(a,h):
    '''
    Вычисляет площадь треугольника.
    
    Параметры:
        a (float): длина основания треугольника
        h (float): высота треугольника
    
    Возвращаемое значение:
        float: площадь треугольника
    
    Пример:
        >>> area(2, 1)
        1.0
        >>> area(4, 2)
        4.0
    '''
    return a * h / 2

def perimeter(a, b, c):
    '''
    Вычисляет периметр треугольника.
    
    Параметры:
        a (float): длина первой стороны
        b (float): длина второй стороны  
        c (float): длина третьей стороны
    
    Возвращаемое значение:
        float: периметр треугольника
    
    Пример:
        >>> perimeter(1, 1, 1)
        3
        >>> perimeter(2, 3, 4)
        9
    '''
    return a + b + c

import unittest

class TriangleTestCase(unittest.TestCase):

    def test_area_simple(self):
        self.assertEqual(area(2, 1), 1.0)
        self.assertEqual(area(4, 2), 4.0)

    def test_area_zero(self):
        self.assertEqual(area(0, 10), 0)
        self.assertEqual(area(10, 0), 0)

    def test_area_float(self):
        self.assertAlmostEqual(area(2.5, 4), 5.0)
        self.assertAlmostEqual(area(3, 3.5), 5.25)

    def test_area_negative(self):
        self.assertEqual(area(-2, 4), -4.0)
        self.assertEqual(area(3, -6), -9.0)

    def test_perimeter_simple(self):
        self.assertEqual(perimeter(1, 1, 1), 3)
        self.assertEqual(perimeter(2, 3, 4), 9)

    def test_perimeter_zero(self):
        self.assertEqual(perimeter(0, 5, 5), 10)
        self.assertEqual(perimeter(3, 0, 3), 6)

    def test_perimeter_float(self):
        self.assertAlmostEqual(perimeter(1.5, 2.5, 3), 7.0)

    def test_perimeter_negative(self):
        self.assertEqual(perimeter(-2, 4, 5), 7)
        self.assertEqual(perimeter(3, -6, 8), 5)


if __name__ == '__main__':
    unittest.main()


