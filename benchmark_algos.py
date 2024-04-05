#!/usr/bin/env python
# coding: utf-8
#
import random
import timeit


DEFAULT_TEST_TIMES = 10 ** 5


def generate_weighted_random_ints(weights, size):
    start_counter = 0
    results = []

    last_index = 0
    array = []

    weight_map = {
        key: i + 1
        for i, key in enumerate(weights)
    }

    index_map = {
        v: 0
        for _, v in weight_map.items()
    }

    for weight in weights:
        for _ in range(start_counter, weight):
            array.append(weight_map[weight])
        start_counter = 0
        last_index += weight

    while len(results) < size:
        random_index = int(random.random() * len(weights))
        if index_map[random_index + 1] < weights[random_index]:
            index_map[random_index + 1] += 1
            results.append(array[random_index])

    __import__('pdb').set_trace()

    return results


def calculate_results(results):
    ones = [_ for _ in results if _ == 1]
    twos = [_ for _ in results if _ == 2]
    threes = [_ for _ in results if _ == 3]

    print(len(ones) + len(twos) + len(threes))
    print(len(ones), len(twos), len(threes))
    print(results)

    return ones, twos, threes


def do_benchmark_mr_music(times=None):
    times = times or DEFAULT_TEST_TIMES

    result = timeit.timeit(
        setup='from __main__ import generate_weighted_random_ints',
        stmt='generate_weighted_random_ints(weights=[66, 12, 22], size=100)',  # noqa: E501
        number=times,
    )

    return result


def do_benchmark_mr_shlep(times=None):
    times = times or DEFAULT_TEST_TIMES

    result = timeit.timeit(
        setup='from randomness import weighted_random_generator',
        stmt='weighted_random_generator(weights=[66, 12, 22], size=100, start=1, end=3)',  # noqa: E501
        number=times,
    )

    return result


if __name__ == '__main__':
    weights = [66, 12, 22]
    size = 100

    results = generate_weighted_random_ints(weights=weights, size=size)
    calculate_results(results)

    print(do_benchmark_mr_music(times=DEFAULT_TEST_TIMES))
    print(do_benchmark_mr_shlep(times=DEFAULT_TEST_TIMES))
