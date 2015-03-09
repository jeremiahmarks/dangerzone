"""inspired by reddit.com/2wl55r"""

import supercircle



def add_and_check(cur_val):
    new_val=[]
    for each_val in cur_val:
        for candidate in range(10):
            valString = str(each_val)+ str(candidate)
            newInt=int(valString)
            if newInt % len(valString)==0:
                new_val.append(newInt)
    print new_val
    return new_val

def get_map_values(starting_set):
	if(len(starting_set)==0):
		return starting_set
	map_of_values={}
	for each_val in starting_set:
		map_of_values[each_val] = get_map_values(add_and_check([each_val]))
	return map_of_values
