#!/usr/bin/env python3
import pickle
import sys
from pprint import pprint

sums_dict = {}

def load_sums_dict(pkl_file):
    global sums_dict
    with open(pkl_file,"rb") as f:
        p = pickle.Unpickler(f)
        sums_dict = p.load()
    

def get_possible_totals(num_digits, total=False, already_have=False, excluded_digits=False):
    # import ipdb; ipdb.set_trace()

    global sums_dict
    this_dict = sums_dict[num_digits]
    remaining_dict = {}
    if total:
        totals_list = [total]
        if not already_have:
            remaining_dict = {total : this_dict[total]}
        
    else:
        totals_list = list(this_dict.keys())
        remaining_dict = this_dict

    if already_have:
        # Find only the ones that already have the given digits and generate the lists of remaining ones
        
        for total in totals_list:
            possibles_for_total = this_dict[total]
            for digits_list in possibles_for_total:
                all_there = True
                for digit in already_have:
                    if digit not in digits_list:
                        all_there = False
                        break
                if all_there:
                    if total not in remaining_dict:
                        remaining_dict[total] = []
                    new_digits_list = remaining_dict.get(total, [])
                    new_digits_list.append(digits_list)
                    remaining_dict[total] = new_digits_list
        totals_list = list(remaining_dict.keys())
    
    # import ipdb; ipdb.set_trace()

    if excluded_digits:
        totals_list = []
        updated_remaining_dict = {}
        for total, digits_lists in remaining_dict.items():
            for dig_list in digits_lists:
                exclude_this_list = False
                for excluded in excluded_digits:
                    # if any in excluded_digits, then break out of this loop to exclude the list
                    if excluded in dig_list:
                        exclude_this_list = True
                        break
                if not exclude_this_list:
                    updated_lists = updated_remaining_dict.get(total, [])
                    updated_lists.append(dig_list)
                    updated_remaining_dict[total] = updated_lists
            if total in updated_remaining_dict:
                totals_list.append(total)
        remaining_dict = updated_remaining_dict
    return totals_list, remaining_dict

def report_result(totals_list, remaining_dict, total):
    if not total:
        print("The possible totals are:")
        print(totals_list)
    print('\nAll the possible combinations are:')
    pprint(remaining_dict)


if __name__ == "__main__":
    from sums import min_list, max_list


    usage = '''
Usage: get_sums.py number_of_digits total [already_have]
where 
    - number_of_digits is an integer from 1 to 9
    - total is either 0 (default) or an appropriate number less than or equal to 45. If 0, then all possible totals are considered
    - already_have (optional) is a list of numbers already contributing to the total
      '''

    if len(sys.argv) < 2:
        print(usage)
        exit()
    try:
        num_digits = int(sys.argv[1])
        if len(sys.argv) > 2:
            total = int(sys.argv[2])
        else:
            total = 0
    except:
        print(usage)
        exit()

    if num_digits < 1 or num_digits > 9 or (total and total > 45):
        print(usage)
        exit()

    if total:
        max_total = sum(max_list(num_digits))
        min_total = sum(min_list(num_digits))
        
        if total < min_total or total > max_total:
            print(f'Error: Total {total} must either be 0 or a number between {min_total} and {max_total}, inclusive, when number_of_digits is {num_digits}.\n')
            print(usage)
            exit()

    # if alternative pkl_file is desired, re-write the code to take a -f 'pkl_file' option. This is what it was before I allowed extra numberic args
    # if len(sys.argv) > 3:
    #     pkl_file = sys.argv[3]+'.pkl'
    # else:
    #     pkl_file = 'all_sums.pkl'
    pkl_file = 'all_sums.pkl'

    already_have = []
    if len(sys.argv) > 3:
        try:
            for arg in sys.argv[3:]:
                already_have.append(int(arg))
        except:
            print(usage)
            exit()

    load_sums_dict(pkl_file)
    
    totals_list, remaining_dict = get_possible_totals(num_digits, total, already_have)

    report_result(totals_list, remaining_dict, total)
