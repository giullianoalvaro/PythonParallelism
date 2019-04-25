import random
from timeit import default_timer as timer


def test_func(list_of_items):
    final_list = []
    for item in list_of_items:
        if item < 50:
            final_list.append(item)
    return final_list


if __name__ == "__main__":
    start = timer()
    random_list = [random.randint(0,1000000) for x in range(0,1000000)]
    end = timer()
    print(end - start) # Time in seconds, e.g. 5.38091952400282
    #%timeit test_func(random_list)
