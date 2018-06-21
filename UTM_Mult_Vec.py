def vecDiviUpperTriMat(b,R):
  '''
  This takes the matrix R and the answer B to solve for X. This takes the reverse itiration of R. For j, this starts at the element i + 1 
  and goes to length B. This takes the element in B and subtracts the product of the matrix times the element in B. 
  Then, divide the answer by the diagonal. This then returns the vector X that solves the equation Ax=b.
  '''
  x = b
  for i in reversed(range(len(R))):
    for j in range(i + 1, len(b)):
      x[i] = x[i] - (R[i][j] * x[j])
    x[i] = x[i] / R[i][i]
  return x

b = [1,2,3]
M = [[4,5,6],
    [0,7,8],
    [0,0,9]]
print(vecDiviUpperTriMat(b,M))
