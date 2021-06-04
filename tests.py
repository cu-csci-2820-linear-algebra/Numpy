import unittest
from nppractice import *

class TestsNpPractice(unittest.TestCase):
    total_grade_ = 0
    total_grade_file = open("total_grade.txt","w")

    @classmethod
    def setUpClass(cls):
        TestsNpPractice.total_grade_file.write(str(0))

    @classmethod
    def tearDownClass(cls):
        TestsNpPractice.total_grade_file.truncate(0)
        print("\nTotal: ", TestsNpPractice.total_grade_)
        TestsNpPractice.total_grade_file.write(str(TestsNpPractice.total_grade_))
        TestsNpPractice.total_grade_file.close()
        
    def IncGrade(p):
        TestsNpPractice.total_grade_ += p

    def test_unit_vector(self):
        """Check that unitvector returns the correct output for several inputs"""
        test.assert_equal(unit_vector(4, 1), np.array([0, 1, 0, 0]))
        test.assert_equal(unit_vector(2, 0), np.array([1, 0]))
        TestsNpPractice.IncGrade(20)

    def test_unit_vector_limits(self):
        """Check that squares raises an error for invalid inputs"""
        with test.assert_raises(ValueError):
            unit_vector(-1,0)
        with test.assert_raises(ValueError):
            unit_vector(4,4)
        with test.assert_raises(ValueError):
            unit_vector(4,-1)
        TestsNpPractice.IncGrade(20)

    def test_axpby(self):
        """Check that sum_of_squares returns the correct answer for various inputs."""
        u = np.array([0.8781019 , 0.18552796, 0.92090045, 0.94656586])
        v = np.array([0.87450809, 0.11574276, 0.19373166, 0.3417372 ])
        alpha = 0.14833610379597723
        beta = -0.08612337722509229
        test.assert_equal(axpby(alpha, u, beta, v), None)
        TestsNpPractice.IncGrade(20)
        test.assert_almost_equal(v, np.array([0.05493862, 0.01755234, 0.11991796, 0.11097833]))
        TestsNpPractice.IncGrade(20)

    def test_final_grade(self):
        # first check that all grades = 1 gives final grade = 1
        test.assert_almost_equal(np.ones(22), final_grade(np.ones(22)))
        # random test from seed
        from numpy.random import default_rng
        rng = default_rng(11931)
        grades = rng.random(22)
        test.assert_almost_equal(0.42795919911899194, final_grade(grades))
        TestsNpPractice.IncGrade(20)

if __name__ == '__main__':
    unittest.main()
