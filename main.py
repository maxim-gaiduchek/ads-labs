from random import sample

from checker import *
from sorts import *

arr_best = {
    10: [i for i in range(10)],
    100: [i for i in range(100)],
    1000: [i for i in range(1000)],
    5000: [i for i in range(5000)],
    10000: [i for i in range(10000)],
    20000: [i for i in range(20000)],
    50000: [i for i in range(50000)]
}

arr_worst = {
    10: [i for i in range(10 - 1, -1, -1)],
    100: [i for i in range(100 - 1, -1, -1)],
    1000: [i for i in range(1000 - 1, -1, -1)],
    5000: [i for i in range(5000 - 1, -1, -1)],
    10000: [i for i in range(10000 - 1, -1, -1)],
    20000: [i for i in range(20000 - 1, -1, -1)],
    50000: [i for i in range(50000 - 1, -1, -1)]
}

arr_random = {
    10: sample(range(10), 10),
    100: sample(range(100), 100),
    1000: sample(range(1000), 1000),
    5000: sample(range(5000), 5000),
    10000: sample(range(10000), 10000),
    20000: sample(range(20000), 20000),
    50000: sample(range(50000), 50000)
}

# print("Bubble sort")
#
# case(bubble_sort, arr_best, "Best")
# case(bubble_sort, arr_worst, "Worst")
# case(bubble_sort, arr_random, "Random")
#
# print()
#
# print("Comb sort")
#
# case(comb_sort, arr_best, "Best")
# case(comb_sort, arr_worst, "Worst")
# case(comb_sort, arr_random, "Random")

print("Bubble sort")

print("Unsorted 100-elements array:", arr_random[100])
print()
print("n", "comparisons", "swaps", "time", "arr", sep="\t")
check(bubble_sort, 100, arr_random[100])
print()

print("Unsorted 1000-elements array:", arr_random[1000][:15], "...")
print()
print("n", "comparisons", "swaps", "time", "arr", sep="\t")
check(bubble_sort, 1000, arr_random[1000])

print()

print("Comb sort")

print("Unsorted 100-elements array:", arr_random[100])
print()
print("n", "comparisons", "swaps", "time", "arr", sep="\t")
check(comb_sort, 100, arr_random[100])
print()

print("Unsorted 1000-elements array:", arr_random[1000][:15], "...")
print()
print("n", "comparisons", "swaps", "time", "arr", sep="\t")
check(comb_sort, 1000, arr_random[1000])
