# Python3 program for the above approach
import sys

# Function to calculate the maximum
# Manhattan distance


def MaxDist(A, N):

	# Stores the maximum distance
	maximum = - sys.maxsize

	for i in range(N):
		sum = 0

		for j in range(i + 1, N):

			# Find Manhattan distance
			# using the formula
			# |x1 - x2| + |y1 - y2|
			Sum = (abs(A[i][0] - A[j][0]) +
				abs(A[i][1] - A[j][1]))

			# Updating the maximum
			maximum = max(maximum, Sum)

	print(maximum)


# Driver code
N = 2

# Given co-ordinates
A = [[2, 3], [5, 7]]

# Function call
MaxDist(A, N)
