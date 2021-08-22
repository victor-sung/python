import sys

from stackover import get_jobs

jobs = get_jobs()
print(sys.getsizeof(jobs))