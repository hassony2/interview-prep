import numpy as np

from sum3_to0 import threeSum

def test_threeSum():
    assert np.array_equal(sorted([[-1,-1,2],[-1,0,1]]), sorted(threeSum([-1,0,1,2,-1,-4])))
    assert np.array_equal(sorted([[-2,-1,3],[-2,0,2],[-1,0,1]]), sorted(threeSum([3,0,-2,-1,1,2])))
