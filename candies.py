"""
There are n children standing in a line. Each child is assigned a rating value given in the integer array ratings.

You are giving candies to these children subjected to the following requirements:

Each child must have at least one candy.
Children with a higher rating get more candies than their neighbors.
Return the minimum number of candies you need to have to distribute the candies to the children.
"""
class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        sublists = {}
        items_key = {
            i:[] for i in range(len(ratings))
        }
        state = 0 # 1 -> increasing -1 -> decreasing 0 -> constant
        last_state = 0
        items = []
        indices = []
        list_count = 0
        current_value = 0
        for i,rating in enumerate(ratings):
            if int(i+1) < len(ratings):
                next_rating = ratings[int(i+1)]
                if rating < next_rating: # increasing
                    state = 1
                elif rating == next_rating: # constant
                    state = 0
                else: # decreasing
                    state = -1
            items.append(current_value)
            indices.append(i)
            if int(i+1) < len(ratings):
                if ((last_state != state) and last_state != 0) or (state == 0): # if the sublist has reached to its end
                    if len(items) > 0:
                        min_value = min(items)
                        items = [int(item - min_value + 1) for item in items]
                        sublists[list_count] = [items , indices]
                        for index in indices:
                            items_key[index].append(list_count)
                        list_count += 1
                    if int(state * last_state) == -1: # if two consecutive increasing / decreasing lists exists
                        items = [0]
                        current_value = 0
                        indices = [indices[-1]]
                    else:
                        items = []
                        indices = []
                if rating < next_rating: # increasing
                    current_value += 1
                elif rating == next_rating: # constant
                    current_value = 0
                else: # decreasing
                    current_value -= 1
                last_state = state
        if len(items) > 0: # if the last sublist not added yet
            min_value = min(items)
            items = [int(item - min_value + 1) for item in items]
            sublists[list_count] = [items , indices]
            for index in indices:
                items_key[index].append(list_count)
        results = []
        for i in range(len(ratings)):
            sublist_indices = items_key[i]
            max_value = -1
            # print("list_indices for" , i , sublist_indices)
            for list_index in sublist_indices:
                sublist = sublists[list_index]
                # print("sublist is:" , sublist)
                sublist_index = sublist[1].index(i)
                # print(sublist_index)
                if max_value < sublist[0][sublist_index]:
                    max_value = sublist[0][sublist_index]
                # print('currently max value is' , max_value)
            results.append(max_value)
        print(results)
        return sum(results)

