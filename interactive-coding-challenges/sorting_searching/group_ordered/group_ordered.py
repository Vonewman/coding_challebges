from collections import OrderedDict
import unittest


## Code: Modified Selection Sort
def make_order_list(list_in):
    order_list = []
    for item in list_in:
        if item not in order_list:
            order_list.append(item)

    return order_list


def group_ordered(list_in):
    if list_in is None:
        return None
    order_list = make_order_list(list_in)
    current = 0
    for item in order_list:
        search = current + 1
        while True:
            try:
                if list_in[search] != item:
                    search += 1
                else:
                    current += 1
                    list_in[current], list_in[search] = list_in[search], \
                        list_in[current]
                    search += 1

            except IndexError:
                break

        return list_in


## Code: Ordered Dict
def group_ordered_alt(list_in):
    if list_in is None:
        return None
    result = OrderedDict()
    for value in list_in:
        result.setdefault(value, [])

    return [v for group in result.values() for v in group]


## Unit Test

### The following unit test is expected to fail until you solve the challenge.

class TestGroupOrdered(unittest.TestCase):
    def test_group_ordered(self, func):

        self.assertEqual(func(None), None)
        print('Success: ' + func.__name__ + " None case.")
        self.assertEqual(func([]), [])
        print('Success: ' + func.__name__ + " Empty case.")
        self.assertEqual(func([1]), [1])
        print('Success: ' + func.__name__ + " Single element case.")
        self.assertEqual(func([1, 2, 1, 3, 2]), [1, 1, 2, 2, 3])
        self.assertEqual(func(['a', 'b', 'a']), ['a', 'a', 'b'])
        self.assertEqual(func([1, 1, 2, 3, 4, 5, 2, 1]), [1, 1, 1, 2, 2, 3, \
                                                          4, 5])
        self.assertEqual(func([1, 2, 3, 4, 3, 4]), [1, 2, 3, 3, 4, 4])
        print('Success: ' + func.__name__)



def main():
    test = TestGroupOrdered()
    test.test_group_ordered(group_ordered)

if __name__ == '__main__':
    main()


