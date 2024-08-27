import threading
import sys; sys.setswitchinterval(10 ** -10)
import unittest
import time

# Practice testing using the unittest and sys modules on a counter with race condition bug.

class Counter:
    def __init__(self, target):
        self.value = 0
        self.target = target
        self.lock = threading.Lock()

    # Bug
    def update_b(self):
        current_value = self.value
        breakpoint()
        time.sleep(0.0001) # Small delay to increase race condition trigger
        self.value = current_value + 1


    # Fix
    def update_s(self):
        with self.lock:
            current_value = self.value
            time.sleep(0.0001) # Small delay to increase race condition trigger
            self.value = current_value + 1

    def run(self):
        threads = [threading.Thread(target=self.update_s) for _ in range(self.target)]

        for t in threads:
            t.start()

        for t in threads:
            t.join()



class TestCounter(unittest.TestCase):
    def setUp(self):
        self.small_params = 5
        # Higher chances of triggering race condition with more threads.
        self.med_params = 5000
        self.large_params = 10000

    def test_small(self):
        small_counter = Counter(self.small_params)
        small_counter.run()
        self.assertEqual(small_counter.value, self.small_params)

    def test_med(self):
        med_counter = Counter(self.med_params)
        med_counter.run()
        self.assertEqual(med_counter.value, self.med_params)

    def test_large(self):
        large_counter = Counter(self.large_params)
        large_counter.run()
        self.assertEqual(large_counter.value, self.large_params)

if __name__ == '__main__':
    unittest.main()

test_counter = Counter(10)
test_counter.run()
