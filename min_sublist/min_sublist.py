def min_sublist(numbers):
    """Find the continuous sublist of `numbers` with the smallest sum.

    If there are multiple, return the first occurrence.

    Args:
        numbers (List[int]): The list of numbers.

    Returns:
        List[int]: (start, end, sum). The start and end indices,
            as well as the sum of the sublist. To retrieve the
            sublist, run `numbers[start:end]`.
    """

    overall_best = [0, 1, numbers[0]]  # (start, end, sum)
    best_that_includes_last = [0, 1, numbers[0]]
    for index_minus_1, n in enumerate(numbers[1:]):
        # index_minus_1 is relative to numbers[1:] so it is 1 less than the true index
        i = index_minus_1 + 1
        best_that_includes_last[1] = i + 1
        if best_that_includes_last[2] > 0:
            best_that_includes_last[0] = i
            best_that_includes_last[2] = n
        else:
            best_that_includes_last[2] += n
        if best_that_includes_last[2] < overall_best[2]:
            overall_best = best_that_includes_last.copy()
    return overall_best
