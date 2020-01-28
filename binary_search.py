import random

random.seed(1)


def binary_search(list_input, item_out):
    low_pos = 0
    high_pos = len(list_input) - 1
    counter = 1
    while low_pos <= high_pos:
        mid_pos = int((high_pos + low_pos) / 2)
        item_guess = list_input[mid_pos]
        if item_guess == item_out:
            print(f'steps = {counter}')
            return mid_pos
        if item_guess > item_out:
            high_pos = mid_pos - 1
            # print(f'going left <--')
        else:
            low_pos = mid_pos + 1
            # print(f'going right -->')
        counter += 1
        print(f'i= {counter}  left= {low_pos}  right= {high_pos}')
    return None


list_test = list(range(1, 100000))
print(f'before shuffle: {list_test}')
list_test = random.sample(list_test, 1023)
list_test.sort()
# random.shuffle(list_test)
print(f'after shuffle: {list_test}\n        len= {len(list_test)}')

rand_number_to_find = random.choice(list_test)
print(f'what I want to find - {random.choice(list_test)}')

answer = binary_search(list_test, rand_number_to_find)
print(f'answer:  pos = {answer}')
