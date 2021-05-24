import sys
from pprint import pprint

usage = 'Usage: python sums.py box_total number_of_digits_in_box\n\twhere box_total_number is less than or equal to 45\n\tand number_of_digits is an integer from 1 to 9'

def update_digits(digit_list):
    for inx in range(len(digit_list) - 1, -1,-1):
        digit_list[inx] += 1

        if digit_list[inx] < 10:
            break
        else:
            digit_list[inx] = 1
        
    return digit_list

def is_valid_set(digit_list, collected_list):
    sorted_digits = sorted(digit_list)
    if sorted(list(set(digit_list))) != sorted_digits or sorted_digits in collected_list:
        return False
    else:
        return True

def min_list(num_digits):
    digit_list = []
    for digit in range(1, num_digits+1):
        digit_list.append(digit)
    return digit_list

def max_list(num_digits):
    max_digits_list = []
    for digit in range(10 - num_digits, 10):
        max_digits_list.append(digit)
    return max_digits_list

def max_list_plus_one(num_digits):
    max_digits_list = max_list(num_digits)
    max_digits_list[num_digits - 2] += 1
    return max_digits_list

def greater_than_max(digit_list, max_digits_list):
    # Check if all digits are less than
    for inx in range(len(max_digits_list)):
        if digit_list[inx] < max_digits_list[inx]:
            return False
    return True


def sums(total, num_digits):
    if total > 45:
        print(usage)
        exit()

    #take care of special cases first
    if num_digits == 1:
        return [[total]]
    elif num_digits == 9 and total == 45:
        return [[1,2,3,4,5,6,7,8,9]]
    elif num_digits == 8 and total < 45 and total >= 36:
        missing_digit = 45 - total
        all_digits = [1,2,3,4,5,6,7,8,9]
        all_digits.remove(missing_digit)
        return [all_digits]

    sums_dict = {}
    digit_list = []
    collected_list = []
    sums_list = []

    digit_list = min_list(num_digits)

    if sum(digit_list) > total:
        print(f'Error: First argument {total} must be {sum(digit_list)} or more when second argument is {num_digits}')
        exit()

    max_digits_list = max_list_plus_one(num_digits)
    while not greater_than_max(digit_list, max_digits_list):
        if sum(digit_list) == total and is_valid_set(digit_list, collected_list):
            collected_list.append(sorted(digit_list))

        digit_list = update_digits(digit_list)

    return collected_list

def create_dict_for_num_digits(num_digits):
    min_total = sum(min_list(num_digits))
    max_total = sum(max_list(num_digits))
    cur_total = min_total
    num_dict = {}
    print(f'\nCreating dictionary for {num_digits}, whose min total is {min_total} and max total is {max_total}')
    while cur_total <= max_total:
        num_dict[cur_total] = sums(cur_total, num_digits)
        print(f'{cur_total} ',end=' ')
        cur_total += 1
    return(num_dict)
    
def create_all_dicts():
    all_dicts = {}
    for num_digits in range (1, 10):
        num_dict = create_dict_for_num_digits(num_digits)
        all_dicts[num_digits] = num_dict
    print('\n')
    return all_dicts

if __name__ == "__main__":
    if len(sys.argv) == 1:
        print(usage)
        exit()
    try:
        total = int(sys.argv[1])
        num_digits = int(sys.argv[2])
    except:
        if sys.argv[1] == 'all':
            try:
                num_digits = int(sys.argv[2])
                pprint(create_dict_for_num_digits(num_digits))
            except:
                # print('should not get here unless "all" with no num_digits')
                pprint(create_all_dicts())
                exit()
            exit()
        print(usage)

    if num_digits < 1 or num_digits > 9:
        print(usage)
        exit()


    pprint(sums(total, num_digits))