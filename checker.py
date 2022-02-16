def case(sort, arrays: dict, prompt: str):
    print(prompt)
    print("n", "comparisons", "swaps", "time", "arr", sep="\t")

    for checked in arrays.items():
        check(sort, checked[0], checked[1])

    print()


def check(sort, n: int, arr: list):
    arr_copy = arr.copy()
    comparisons, swaps, sort_time = sort(arr_copy)

    if len(arr_copy) <= 10:
        print(n, comparisons, swaps, sort_time, arr_copy, sep="\t")
    else:
        print(n, comparisons, swaps, sort_time, arr_copy[:15], "...", arr_copy[len(arr_copy) - 15:], sep="\t")
