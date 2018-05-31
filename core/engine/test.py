import unittest
import core.engine.classes as c
import core.engine.functions as f


class TestStringMethods(unittest.TestCase):
    def test_centrals_equality(self):
        centrals_old = [c.Central(1, 2, [c.Point(2, 4)]), c.Central(3, 4, [c.Point(5, 8)])]
        centrals_new = [c.Central(1, 2, [c.Point(6, 4)]), c.Central(3, 4, [c.Point(5, 8)])]
        self.assertFalse(f.centrals_equals(centrals_new, centrals_old))

        centrals_new[0].points[0].x = 2
        self.assertTrue(f.centrals_equals(centrals_new, centrals_old))
