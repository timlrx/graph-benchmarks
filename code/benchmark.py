import timeit
import statistics


def benchmark(stmt, n, globals):
    times = timeit.repeat(stmt, number=1, globals=globals, repeat=n)
    print('Function:', stmt)
    print('  --------------')
    print(f'  Min:      {min(times)}')
    print(f'  Median:   {statistics.median(times)}')
    print(f'  Mean:     {statistics.mean(times)}')
    print(f'  Stdev:    {statistics.stdev(times)}')
    print(f'  Max:      {max(times)}')
    print('  --------------')
    print(f'  samples:  {len(times)}')
    print()
