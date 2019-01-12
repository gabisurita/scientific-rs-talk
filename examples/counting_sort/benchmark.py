
import numpy as np
import counting_sort

# input: array[N]
# output: sorted array
# procedure:
#   max_value <- max(array)
#   counter <- new_array(max_value, 0)
#
#   k <- 0
#   for i between 0 and N
#     for r between 0 and counter[i]
#       array[k] <- i
#       k <- k + 1
#
#   return array


def counting_sort_py(array):
    max_value = max(array) + 1
    counts = [0 for _ in range(max_value)]

    for i in range(max_value):
        counts[i] += 1

    return [i for i in range(max_value) for count in range(counts[i])]


def counting_sort_np(array):
    max_value = np.max(array) + 1
    counts = np.zeros(max_value, dtype=np.int)
    counts[array] += 1

    return [i for i in range(max_value) for count in range(counts[i])]


def counting_sort_rust(array):
    return counting_sort.sort(array)


"""
arr = np.arange(1000000)

%timeit counting_sort_py(arr)
%timeit counting_sort_np(arr)
%timeit counting_sort_rust(arr)


arr = (100 * np.random.random(1000000)).astype(int)

%timeit counting_sort_py(arr)
%timeit counting_sort_np(arr)
%timeit counting_sort_rust(arr)
"""
