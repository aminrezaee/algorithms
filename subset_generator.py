from copy import deepcopy



def generate_subsets(items: set[str]):
    subsets = set()    
    _add_subsets(items , set() , subsets)
    return subsets

def _add_subsets(items: set[str], currently_chosen_items: set[str] , subsets:set[str]):
    subsets.add(currently_chosen_items)
    if len(items) == 0:
        return
    item_count = len(items)
    items_copy = deepcopy(items)
    for i in range(item_count):
        item = items[i]
        next_chosen_items = deepcopy(currently_chosen_items)
        next_chosen_items.add(item)
        items_copy.remove(item)
        _add_subsets(items_copy, currently_chosen_items=next_chosen_items)

if __name__ == "__main__":
    print(generate_subsets({'a', 'b', 'c', 'd'}))
