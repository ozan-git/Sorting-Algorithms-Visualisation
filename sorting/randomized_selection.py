# It was created on November 14, 2021.
# Written by Orhan Ozan Yildiz.
from numpy import random


# RANDOMIZED-SELECT(A,p,r,i)
# (1) if p == r
# (2)     return A[p]
# (3) q = RANDOMIZED-PARTITION(A,p,r)
# (4) k = q - p + 1
# (5) if i==k          // the pivot value is the answer
# (6)     return A[q]
# (7) elseif i < k
# (8)     return RANDOMIZED-SELECT(A,p,q-1,i)
# (9) else return RANDOMIZED-SELECT(A,q+1,r,i-k)
def randomized_selection(A, p, r, i):
	# (1 and 2)
	if 0 < i <= p - r + 1:

		# Divide the array around a random element and get the position of the
		# pivot element in the sorted array.
		q = partition_random(A, p, r)

		# If place is more, repeat for the left subarray,
		# if not, repeat for the right subarray.
		if q - p == i - 1:
			return A[q]
		if q - p > i - 1:
			return randomized_selection(A, p, q - 1, i)
		return randomized_selection(A, q + 1, r, i - q + p - 1)


# The key to the algorithm is the PARTITION procedure, which rearranges
# the subarray A[p....r] in place.
# PARTITION(A, p, r)
# (1) x = A[r]
# (2) i = p - 1
# (3) for j = p to r - 1
# (4)     if A[j] <= x
# (5)         i = i + 1
# (6)         exchange A[i] with A[j]
# (7) exchange A[i + 1] with A[r]
# (8) return i + 1
def partition(A, p, r):
	x = A[r]
	i = p
	for j in range(p, r):
		if A[j] <= x:
			i += 1
			A[i], A[j] = A[j], A[i]
	A[i], A[r] = A[r], A[i]
	return i


# Picks a random pivot element between l and r and partitions array around the
# randomly picked element.
def partition_random(A, p, r):
	n = r - p + 1
	pivot = int(random.random() % n)
	A[p + pivot], A[r] = A[r], A[p + pivot]
	return partition(A, p, r)
