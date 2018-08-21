def recursive_permutations(lst):
    '''Finds all permutations of a string recursively'''

    # First we handle our error and early exit cases
    if len(lst) is 0:
        return None

    elif len(lst) is 1:
        return [lst] # Shows that the only permuation is the list itself

    else:

        permutation_list = [] # Is going to store the permutations of the string

        for index in range(0, len(lst)):
            temp_current = lst[index]

            remaining_elements = lst[ :index ] + lst[index + 1: ] # grabs all elements besides the current element

            for perm in recursive_permutations(remaining_elements):
                permutation_list.append([temp_current] + perm)

    return permutation_list


print(recursive_permutations(['A', 'B', 'C']))