import random

from string import ascii_letters as letters


def create_name():
    name = ''
    for i in range(8):
        index = random.randrange(52)
        name += letters[index]
    return name


def create_random_groups(group_list, number_of_participants):
    match_group_index_list = []
    participants_index_list = list(range(number_of_participants))
    new_pil = participants_index_list[:]
    for i in range(len(group_list)-1):
        group = random.sample(new_pil, group_list[i+1]-group_list[i])
        match_group_index_list.append(group)
        for item in group:
            if item in new_pil:
                new_pil.remove(item)
    return match_group_index_list


def create_group_list(number_of_participants):

    number_of_five = number_of_participants % 4
    number_of_elements = number_of_participants // 4
    group_list = [0]

    n = 0
    while len(group_list) <= number_of_elements:
        n += 1
        try:
            c = group_list[-1]
        except:
            c = 0
        if n <= number_of_five:
            group_list.append(c + 5)
        else:
            group_list.append(c + 4)
    return group_list

