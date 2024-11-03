import unittest
import random

def add(a,b):
    return a+b

def randomArr(x):
    ar = []
    for i in range (x):
        ar.append(random.randint(0,1000))
    return ar

def bubbleSort(ar):
    for i in range(len(ar)-1, 0, -1):
        for j in range (i):
            if ar[j] > ar[j+1]:
                ar[j], ar[j+1] = ar[j+1], ar[j]
    

class TestBubbleSort(unittest.TestCase):
    def test_positive_cases(self):
        arr = [5,1,3,0,9,7,8]
        self.assertEqual(bubbleSort(arr),arr.sort())
    
    def test_negative_cases(self):
        arr = "string"
        self.assertRaises(TypeError, bubbleSort,arr)
    
    def test_performance_cases(self):
        arr1= randomArr(3)
        self.assertTrue(bubbleSort(arr1) == arr1.sort())
        arr2= randomArr(30)
        self.assertTrue(bubbleSort(arr2) == arr2.sort())
        arr3= randomArr(300)
        self.assertTrue(bubbleSort(arr3) == arr3.sort())
        arr4= randomArr(3000)
        self.assertTrue(bubbleSort(arr4) == arr4.sort())
        arr5= randomArr(30000)
        self.assertTrue(bubbleSort(arr5) == arr5.sort())

    def test_boundary_cases(self):
        arr1 = []
        self.assertEqual(bubbleSort(arr1),None)

        arr2 = [50]
        self.assertEqual(bubbleSort(arr2),arr2.sort())

        arr3 = [1,1,1,1,1]
        self.assertEqual(bubbleSort(arr3),arr3.sort())

        arr4 = [5,4,3,2,1]
        self.assertEqual(bubbleSort(arr4),arr4.sort())


    def test_idempotency_cases(self):
        ar = randomArr(10)
        self.assertEqual(bubbleSort(ar),ar.sort())
        for i in range (100):
            bubbleSort(ar)
            self.assertEqual(bubbleSort(ar),ar.sort())


if __name__ == '__main__':
    unittest.main()
