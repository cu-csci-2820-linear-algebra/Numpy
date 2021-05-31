
from problem1 import *

class tests:
    total_grade_ = 0
    def IncGrade(p):
        tests.total_grade_ += p

    def TEST_unit_vector():

        """Check that unitvector returns the correct output for several inputs"""
        test.assert_equal(unit_vector(4, 1), np.array([0, 1, 0, 0]))
        test.assert_equal(unit_vector(2, 0), np.array([1, 0]))
        tests.IncGrade(1)

        """Check that squares raises an error for invalid inputs"""
        with test.assert_raises(ValueError):
            unit_vector(-1,0)
        with test.assert_raises(ValueError):
            unit_vector(4,4)
        with test.assert_raises(ValueError):
            unit_vector(4,-1)
        tests.IncGrade(1)

    def RunTestsAndCalcGrade():
        # here we run all the tests
        tests.TEST_unit_vector()
        
        # here we store the final grade in file for inginious
        total_grade_file = open("TotalGrade.txt","w")
        print("Your Total Grade is: ",tests.total_grade_)
        total_grade_file.write(str(tests.total_grade_))
        total_grade_file.close()


def main():
    t=tests;
    t.RunTestsAndCalcGrade()

if __name__ == '__main__':
    main()