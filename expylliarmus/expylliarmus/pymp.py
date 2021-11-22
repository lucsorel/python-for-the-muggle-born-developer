
from pympler.asizeof import asizeof

def report_memory_usage(**kwargs):
    for name, variable in kwargs.items():
        print(f'{name}:', asizeof(variable), 'bytes')
