import unittest
from scientific_calculator import sin, cos, tan, sqrt, log, exp, asin, acos, atan

class TestBasicOperations(unittest.TestCase):
   def test_add(self):
      result = add(2, 3)
      self.assertEqual(result, 5)   
      
   def test_subtract(self):
      result = subtract(5, 2)
      self.assertEqual(result, 3)
      
 

class TestScientificOperations(unittest.TestCase):  
    # TESTS FOR SINE OPERATIONS
    def test_sin_positive_input(self):
        result = sin(90)
        self.assertAlmostEqual(result, 1, places=7)

    def test_sin_negative_input(self):
        result = sin(-90)
        self.assertAlmostEqual(result, -1, places=7)

    def test_sin_zero_input(self):
        result = sin(0)
        self.assertEqual(result, 0)

    def test_sin_non_numeric_input(self):
        with self.assertRaises(TypeError):
            sin("hello")
            
   # TESTS FOR COSINE OPERATIONS

    def test_cos_positive_input(self):
        result = cos(0)
        self.assertAlmostEqual(result, 1, places=7)

    def test_cos_negative_input(self):
        result = cos(180)
        self.assertAlmostEqual(result, -1, places=7)

    def test_cos_zero_input(self):
        result = cos(90)
        self.assertAlmostEqual(result, 0, places=7)

    def test_cos_non_numeric_input(self):
        with self.assertRaises(TypeError):
            cos("hello")
            
 # TESTS FOR TANGENT OPERATIONS
    def test_tan_positive_input(self):
        result = tan(45)
        self.assertAlmostEqual(result, 1, places=7)
    
    def test_tan_negative_input(self):
        result = tan(-45)
        self.assertAlmostEqual(result, -1, places=7)

    def test_tan_zero_input(self):
        result = tan(0)
        self.assertEqual(result, 0)

    def test_tan_non_numeric_input(self):
        with self.assertRaises(TypeError):
            tan("hello")

 # TESTS FOR SQUAREROOT OPERATIONS
    def test_sqrt_positive_input(self):
        result = sqrt(16)
        self.assertEqual(result, 4)

    def test_sqrt_non_numeric_input(self):
        with self.assertRaises(TypeError):
            sqrt("hello")

    def test_sqrt_negative_input(self):
        with self.assertRaises(ValueError):
            sqrt(-16)
            
    def test_sqrt_zero_input(self):
        result = sqrt(0)
        self.assertEqual(result, 0)

 # TESTS FOR LOG OPERATIONS
    def test_log_positive_input(self):
        result = log(1)
        self.assertEqual(result, 0)

    def test_log_non_numeric_input(self):
        with self.assertRaises(TypeError):
            log("hello")

    def test_log_negative_input(self):
        with self.assertRaises(ValueError):
            log(-1)

    def test_log_zero_input(self):
        with self.assertRaises(ValueError):
            log(0)
            
 # TESTS FOR EXPONENTIAL OPERATIONS
    def test_exp_positive_input(self):
        result = exp(1)
        self.assertAlmostEqual(result, 2.7182818, places=7)

    def test_exp_non_numeric_input(self):
        with self.assertRaises(TypeError):
            exp("hello")
            
    def test_exp_zero_input(self):
         result = exp(0)
         self.assertEqual(result, 1)

    def test_exp_negative_input(self):
         result = exp(-1)
         self.assertAlmostEqual(result, 0.3678794, places=7)

 # TESTS FOR ASIN OPERATIONS
    def test_asin_positive_input(self):
        result = asin(1)
        self.assertAlmostEqual(result, 90, places=7)
    
    def test_asin_zero_input(self):
        result = asin(0)
        self.assertEqual(result, 0)
    
    def test_asin_negative_input(self):
        result = asin(-1)
        self.assertAlmostEqual(result, -90, places=7) 
    
    def test_asin_invalid_input(self):
        with self.assertRaises(ValueError):
            asin(2) 

    # TESTS FOR ACOS OPERATIONS
    def test_acos_positive_input(self):
        result = acos(1)
        self.assertEqual(result, 0)  # 
    
    def test_acos_zero_input(self):
        result = acos(0)
        self.assertAlmostEqual(result, 90, places=7)   
    
    def test_acos_negative_input(self):
        result = acos(-1)
        self.assertAlmostEqual(result, 180, places=7)  
    
    def test_acos_invalid_input(self):
        with self.assertRaises(ValueError):
            acos(2)  
    
    # TESTS FOR ATAN OPERATIONS
    def test_atan_positive_input(self):
        result = atan(1)
        self.assertAlmostEqual(result, 45, places=7)   
    
    def test_atan_zero_input(self):
        result = atan(0)
        self.assertEqual(result, 0)
    
    def test_atan_negative_input(self):
        result = atan(-1)
        self.assertAlmostEqual(result, -45, places=7)   
 
def add(a, b):
   return a + b
def subtract(a, b):
   return a - b


if __name__ == '__main__':
   unittest.main()