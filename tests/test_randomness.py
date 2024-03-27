# coding: utf-8

from randomness import random_generator
from randomness import weighted_random_generator


def test_random_generator_generates_the_proper_size_of_items():
    size = 1000
    start = 1
    end = 3

    random_nums = random_generator(
        size=size,
        start=start,
        end=end,
    )

    results = [
        random_num
        for random_num in random_nums
    ]

    results_len = len(results)

    assert results_len == size, f'Expected random generator to produduce size {size} but got {results_len}'  # noqa: E501

    expected_range = {
        1: 0,
        2: 0,
        3: 0,
    }

    for i, v in enumerate(results):
        i = (i % end) + 1
        expected_range[i] += 1

        assert v in expected_range

    for i, v in enumerate(expected_range):
        i = (i % end) + 1

        assert expected_range[i] > 0

    total_items = sum([v for v in expected_range.values()])

    assert total_items == size


def test_weighted_random_generator():
    kwargs = dict(
        weights=[66, 12, 33],
        size=100,
        start=1,
        end=3,
    )

    results = weighted_random_generator(**kwargs)

    assert len(results) == kwargs['size']
    print()
    print(len(results))
    print()
