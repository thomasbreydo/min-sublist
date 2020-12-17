import pandas as pd

FILENAME = "/Users/thomasbreydo/Downloads/a.csv"


def min_sublist(numbers):
    """Find the continuous sublist of `numbers` with the smallest sum.

    If there are multiple, return the first occurrence.

    Args:
        numbers (list of float): The list of numbers.

    Returns:
        list of int | float: (start, end, sum). The start and end indices,
            as well as the sum of the sublist. To retrieve the
            sublist, run `numbers[start:end]`.

    Examples:
        >>> min_sublist([1, -10, 3, -4, -1, 3])
        [1, 5, -12]

        If the list is of non-negative numbers the sublist will contain just the minimum:

        >>> min_sublist([10, 15, 30, 2000])
        [0, 1, 10]
    """

    overall_best = [0, 1, numbers[0]]  # (start, end, sum)
    best_that_includes_last = [0, 1, numbers[0]]  # (start, end, sum)
    for index_minus_1, n in enumerate(numbers[1:]):
        # index_minus_1 is relative to returns[1:] so it is 1 less than the true index
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


def min_cont_return(returns):
    """Find the continuous sublist of `returns` with the smallest
        combined return.

    If there are multiple, return the first occurrence.

    Args:
        returns (list of float): The list of returns, as decimals
            (e.g. 1% -> 0.01).

    Returns:
        list of int | float: (start, end, sum). The start and end indices,
            as well as the sum of the sublist. To retrieve the
            sublist, run `returns[start:end]`.
    """

    overall_best = [0, 1, returns[0]]  # (start, end, sum)
    best_that_includes_last = [0, 1, returns[0]]  # (start, end, sum)
    for index_minus_1, n in enumerate(returns[1:]):
        # index_minus_1 is relative to returns[1:] so it is 1 less than the true index
        i = index_minus_1 + 1
        best_that_includes_last[1] = i + 1
        if best_that_includes_last[2] > 0:
            best_that_includes_last[0] = i
            best_that_includes_last[2] = n
        else:
            best_that_includes_last[2] = (1 + best_that_includes_last[2]) * (1 + n) - 1
        if best_that_includes_last[2] < overall_best[2]:
            overall_best = best_that_includes_last.copy()
    return overall_best


def percent_to_float(x):
    """For example,  ``'-0.5%'`` becomes ``-0.005``

    Args:
        x (str)
    """
    return float(x[:-1]) / 100


def main():
    df = pd.read_csv(FILENAME, header=None, index_col=0)
    out = pd.DataFrame(index=["start_date", "end_date", "total_return"])
    for colname in df:
        returns = df[colname].dropna()
        start, end, total_return = min_cont_return(
            [percent_to_float(x) for x in returns]
        )
        out[colname] = (returns.index[start], returns.index[end - 1], total_return)
    print(out)


if __name__ == "__main__":
    main()
