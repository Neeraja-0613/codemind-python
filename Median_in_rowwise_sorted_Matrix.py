import numpy as np
class Solution:
    def median(self, mat):
    	# code here 
    	r=[]
    	for i in mat:
    	    for j in i:
    	        r.append(j)
        r.sort()
        return int(np.median(r))
