from collections import namedtuple
from pprint import pprint
import multiprocessing
import concurrent.futures
import os
import time

Scientist = namedtuple('Scientist', field_names=[
  'name',
  'field',
  'born',
  'nobel',
])

scientists = (
  Scientist(name='chemsou', field='math', born=1993, nobel=True),
  Scientist(name='ali', field='math', born=1995, nobel=True),
  Scientist(name='nabil', field='physic', born=1991, nobel=True),
  Scientist(name='anouar', field='math', born=1988, nobel=True),
  Scientist(name='salim', field='physic', born=1990, nobel=True),
  Scientist(name='sami', field='physic', born=1975, nobel=True),
  Scientist(name='omar', field='math', born=1982, nobel=True),
)

pprint(scientists)
print()

def transform(x):
  print(f'Process {os.getpid()} working on record {x.name}')
  time.sleep(1)
  result = {'name': x.name, 'age': 2020 - x.born}
  print(f'Process {os.getpid()} done processing record {x.name}')
  return result

start = time.time()

## sequential code
# result = tuple(map(
#   transform,
#   scientists
# ))

## parralel code
# pool = multiprocessing.Pool()
# result = pool.map(transform, scientists)

## concurrent.futures
with concurrent.futures.ProcessPoolExecutor() as executor:
  result = executor.map(transform, scientists)

end = time.time()

print()
print(f'transform completed in {end - start:.2f} s\n')
pprint(result)
