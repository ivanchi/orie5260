import unittest
from dijkstra import find_shortest_path, txt2dic

class testDijkstra(unittest.TestCase):

    def test_find_shortest_path1(self):
        graph1 = txt2dic("graph1.txt")
        expected_graph1 = {1:{ 2: 2, 3: 4, 4: 3}, 2:{5: 1}, 3:{6: 2, 4: 3}, 4:{6: 4, 1: 1}, 5:{6:1}, 6: None}
        self.assertDictEqual(graph1, expected_graph1)
        assert find_shortest_path("graph1.txt", 1, 6) == (4, [1, 2, 5, 6])
        try:
            find_shortest_path("graph1.txt", 2, 1)
        except KeyError:
            print("No solution!")
        assert find_shortest_path("graph1.txt", 3, 2) == (6, [3, 4, 1, 2])
        
    def test_find_shortest_path2(self):
        graph2 = txt2dic("graph2.txt")
        expected_graph2 = {1:{ 2: 4, 3: 4}, 2:{}, 3:{5: 4, 6: 2}, 4:{3:2}, 5:{7:2}, 6: {5:3}, 7:{8:2, 6:2}, 8:{5:2}}
        self.assertDictEqual(graph2, expected_graph2)
        assert find_shortest_path("graph2.txt", 1, 8) == (12, [1, 3, 5, 7, 8])
        try:
            find_shortest_path("graph2.txt", 2, 7)
        except KeyError:
            print("No solution!")
        assert find_shortest_path("graph2.txt", 7, 5) == (4, [7, 8, 5]) 
        assert find_shortest_path("graph2.txt", 4, 8) == (10, [4, 3, 5, 7, 8]) 
        
    def test_find_shortest_path3(self):
        graph3 = txt2dic("graph3.txt")
        expected_graph3 = {1:{ 2: -1, 3: 2}, 2:{4: -1}, 3:{1: 4}, 4:{1:-1, 5:4}, 5: None}
        self.assertDictEqual(graph3, expected_graph3)
        assert find_shortest_path("graph3.txt", 1, 5) == (2, [1, 2, 4, 5])
    
    
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
