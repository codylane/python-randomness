# coding: utf-8

from randomness import random_generator


def test_random_generator_generates_the_proper_size_of_items():
    samples = [1, 2, 3]
    size = 100

    results = random_generator(
        samples=samples,
        size=size,
    )

    results[-1] = 5
    results_len = len(results)

    assert results_len == size, f'Expected random generator to produduce size {size} but got {results_len}'  # noqa: E501

    print()
    print(results)
