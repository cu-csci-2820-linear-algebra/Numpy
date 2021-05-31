import unittest
from problem1 import *

class TestsNpPractice(unittest.TestCase):
    total_grade_ = 0
    total_grade_file = open("TotalGrade.txt","w")

    @classmethod
    def setUpClass(cls):
        TestsNpPractice.total_grade_file.write(str(0))

    @classmethod
    def tearDownClass(cls):
        TestsNpPractice.total_grade_file.truncate(0)
        TestsNpPractice.total_grade_file.write(str(TestsNpPractice.total_grade_))
        TestsNpPractice.total_grade_file.close()
        
    def IncGrade(p):
        TestsNpPractice .total_grade_ += p

    def test_unit_vector(self):
        """Check that unitvector returns the correct output for several inputs"""
        test.assert_equal(unit_vector(4, 1), np.array([0, 1, 0, 0]))
        test.assert_equal(unit_vector(2, 0), np.array([1, 0]))
        TestsNpPractice.IncGrade(1)

    def test_unit_vector_limits(self):
        """Check that squares raises an error for invalid inputs"""
        with test.assert_raises(ValueError):
            unit_vector(-1,0)
        with test.assert_raises(ValueError):
            unit_vector(4,4)
        with test.assert_raises(ValueError):
            unit_vector(4,-1)
        TestsNpPractice.IncGrade(1)


if __name__ == '__main__':
    unittest.main()
