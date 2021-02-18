import random

from assignments.a2p4b import Heap


def test_min():
    def test_with_getter():
        a, b = -100, 10000
        nums = [{"value": random.randint(a, b), "idx": i} for i in range(1000)]
        getter = lambda x: x["value"]
        heep = Heap(lambda x: x["value"], lambda x: x["idx"])
        for n in nums:
            heep.insert(n)
        nums_sorted = sorted(map(lambda x: x["value"], nums), reverse=True)
        while not heep.is_empty():
            dequeued = heep.dequeue_min()
            popped = nums_sorted.pop()
            if getter(dequeued) != popped:
                print("FAIL: nums = ", nums)
        assert not nums_sorted

    for i in range(100):
        test_with_getter()


if __name__ == '__main__':
    test_min()
