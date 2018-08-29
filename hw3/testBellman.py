import unittest
from bellman import find_negative_circles, txt2dic

class testBellman(unittest.TestCase):

    def test_find_negative_circles1(self):
        graph4 = txt2dic("graph4.txt")
        expected_graph4 = {1:{ 2: -1, 7: 2}, 2:{3: -2}, 3:{1: -5, 6: 2}, 6:{}, 7:{8:1}, 8:{9:1}, 9:{1:2}}
        self.assertDictEqual(graph4, expected_graph4)
        assert find_negative_circles("graph4.txt") == [1, 2, 3]
        
    def test_find_negative_circles2(self):
        assert find_negative_circles("graph5.txt") == [11, 3, 5, 6, 7]
    
    def test_find_negative_circles3(self):
        print(find_negative_circles("graph6.txt"))
        assert find_negative_circles("graph6.txt") == [8, 5, 4, 8]
    
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
