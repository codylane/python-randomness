# coding: utf-8

from randomness import weighted_random_generator

import timeit


def test_weighted_random_generator():
    kwargs = dict(
        weights=[66, 12, 22],
        size=100,
        start=1,
        end=3,
    )

    results = weighted_random_generator(**kwargs)

    assert len(results) == kwargs['size']

    actuals = {
        i: 0
        for i in range(kwargs['start'], kwargs['end'] + 1)
    }

    for actual in results:
        actuals[actual] += 1

    assert sum(actuals.values()) == kwargs['size']
    assert len(actuals) == 3

    assert actuals[1] == 66
    assert actuals[2] == 12
    assert actuals[3] == 22


def test_benchmark_of_weighted_random_generator():
    times = 10 ** 4

    result = timeit.timeit(
        setup='from randomness import weighted_random_generator',
        stmt='weighted_random_generator(weights=[66, 12, 22], size=100, start=1, end=3)',  # noqa: E501
        number=times,
    )

    print(f'result=times={times} result={result}')
