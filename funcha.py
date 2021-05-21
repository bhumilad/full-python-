import time
from functools import cached_property
class Set:
    def __init__(self,seq_of_num):
        self.data=seq_of_num

    @cached_property
    def std(self):
        return statistics.std(self.data)

   