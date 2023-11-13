import typing


def sliding_window(
    seq: typing.Sequence, size: int
) -> typing.Generator[typing.Sequence, None, None]:
    """
    Example: [1,2,3,4,5] -> [[1,2],[2,3],[3,4],[4,5]]
    :param seq:
    :param size:
    :return:
    """
    for i in range(len(seq) - size + 1):
        yield seq[i : i + size]


def batch(
    seq: typing.Sequence, size: int, allow_unequal: bool = False
) -> typing.Generator[typing.Sequence, None, None]:
    """
    Example: [1,2,3,4] -> [[1,2], [3, 4]]

    Unequal batches will raise an exception.
    :param allow_unequal:
    :param seq:
    :param size:
    :return:
    """
    if not allow_unequal and len(seq) % size != 0:
        raise Exception("Sequence cannot be batched equally")

    for i in range(0, len(seq), size):
        yield seq[i : i + size]
