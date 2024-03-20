# coding: utf-8

from randomness import random_generator


def test_random_generator_generates_the_proper_size_of_items():
    size = 10000
    start = 1
    end = 3

    results = random_generator(
        size=size,
        start=start,
        end=end,
    )

    results_len = len(results)

    assert results_len == size, f'Expected random generator to produduce size {size} but got {results_len}'  # noqa: E501

    expected_range = {
        1: 0,
        2: 1,
        3: 2,
    }

    for i, v in enumerate(results):
        i = i % end + 1
        expected_range[i] += 1
        assert v in expected_range
