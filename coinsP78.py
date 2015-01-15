# def pent_new(n):
#     return (n*(3*n - 1))/2

# def gen_pent_new(n):
#     if n%2:
#         i = (n + 1)/2
#     else:
#         i = -n/2
#     return pent_new(i)

# partitions_new = [1, 1, 2, 3, 5, 7, 11, 15, 22, 30, 42]

# def partition_new(n):
#     try:
#         return partitions_new[n]
#     except IndexError:
#         total, sign, i = 0, 1, 1
#         k = gen_pent_new(i)
#         while n - k >= 0:
#             total += sign*partition_new(n - k)

#             i += 1
#             if i%2: sign *= -1
#             k = gen_pent_new(i)

#         partitions_new.insert(n, total)
#         return total

###########From Stack Overflow,  using eulers generating function

target = 10**6

import itertools

for n in itertools.count(9):
    if not partition_new(n)%target:
        print n
        break