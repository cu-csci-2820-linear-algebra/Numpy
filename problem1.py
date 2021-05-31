#!/usr/bin/env python
# coding: utf-8

# Before you turn this problem in, make sure everything runs as expected. First, **restart the kernel** (in the menubar, select Kernel$\rightarrow$Restart) and then **run all cells** (in the menubar, select Cell$\rightarrow$Run All).
# 
# Make sure you fill in any place that says `YOUR CODE HERE` or "YOUR ANSWER HERE", as well as your name and collaborators below:

# In[ ]:


NAME = ""
COLLABORATORS = ""


# ---

# In[ ]:


import numpy as np
import numpy.testing as test
print("Imported numpy!")


# In[ ]:


IPY_TESTS_ENABLED = 0
if __name__ == '__main__' and "get_ipython" in dir():
    print ("Tests are enabled!")
    IPY_TESTS_ENABLED = 1


# ---
# ## Part A (2 points)
# 
# Write a function that returns the unit vector $e_i$ of length $n$. Because numpy arrays use zero-based indexing, your function should work for $0 \le i \lt n$, and raise a ValueError otherwise.  Also raise a ValueError if $n < 1$.
# 
# $$(e_i)_j = \begin{cases}
# 1 & j = i \\
# 0 & j \ne i
# \end{cases}$$

# In[ ]:


def unit_vector(n, i):
    """Return the zero-based unit vector e_i of length n.    
    """
    # YOUR CODE HERE
    # raise NotImplementedError()
    return


# In[ ]:


def TEST_unit_vector():
    """Check that unitvector returns the correct output for several inputs"""
    test.assert_equal(unit_vector(4, 1), np.array([0, 1, 0, 0]))
    test.assert_equal(unit_vector(2, 0), np.array([1, 0]))

    """Check that squares raises an error for invalid inputs"""
    with test.assert_raises(ValueError):
        unit_vector(-1,0)
    with test.assert_raises(ValueError):
        unit_vector(4,4)
    with test.assert_raises(ValueError):
        unit_vector(4,-1)
        
# running the test
if IPY_TESTS_ENABLED:
    TEST_unit_vector()


# ---
# 
# ## Part B (2 points)
# 
# Write a function axpby that updates the array y with $y \leftarrow \alpha x + \beta y$ given floats $\alpha, \beta$ and 1-D arrays $x, y$.  Because the function's purpose is to modifying $y$, axpby should return `None`.

# In[ ]:


def axpby(a, x, b, y):
    """Compute ax + by"""
    # YOUR CODE HERE
    raise NotImplementedError()


# In[ ]:


def TEST_axpby():
    """Check that sum_of_squares returns the correct answer for various inputs."""
    u = np.array([0.8781019 , 0.18552796, 0.92090045, 0.94656586])
    v = np.array([0.87450809, 0.11574276, 0.19373166, 0.3417372 ])
    alpha = 0.14833610379597723
    beta = -0.08612337722509229
    test.assert_equal(axpby(alpha, u, beta, v), None)
    test.assert_almost_equal(v, np.array([0.05493862, 0.01755234, 0.11991796, 0.11097833]))
    
#running the test
# TEST_axpby()


# ---
# ## Part C (1 point)
# 
# Suppose a student's grades in a course are represented by a vector $g$, with each grade between zero and one: $0 \le g_i \le 1$. The weights for each assessment are given by a vector $w$, such that the student's final weighted grade will be $g^T w$.  This course has sixteen homeworks, four labs, and two exams, ordered in the vector like so:
# $$
# g = \begin{bmatrix}
# hw_1 \\
# \vdots \\
# hw_{16} \\
# lab_1 \\
# \vdots \\
# lab_4 \\
# exam_1 \\
# exam_2 \\
# \end{bmatrix}
# $$
# 
# Write a function final_grade that takes in a student's grades and returns the final value between 0 and 1.  Fill the weight vector such that all homeworks together have a combined weight of 50%, labs 25%, and exams 25%.

# In[ ]:


def final_grade(g):
    # w = ???
    # YOUR CODE HERE
    raise NotImplementedError()
    return g @ w


# In[ ]:


def TEST_final_grade():
    # first check that all grades = 1 gives final grade = 1
    test.assert_almost_equal(np.ones(22), final_grade(np.ones(22)))
    # random test from seed
    from numpy.random import default_rng
    rng = default_rng(11931)
    grades = rng.random(22)
    test.assert_almost_equal(0.42795919911899194, final_grade(grades))
    
# run the test
# TEST_final_grade()

