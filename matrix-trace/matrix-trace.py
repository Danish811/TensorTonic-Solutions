import numpy as np

def matrix_trace(A):
   i = 0
   sz = len(A)
   res = 0
   for i in range(sz):
       res += A[i][i]
   return res