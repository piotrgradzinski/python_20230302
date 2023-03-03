import cProfile
import pstats


def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


profiler = cProfile.Profile()

profiler.enable()
fibonacci(33)
profiler.disable()

pstats.Stats(profiler).print_stats()