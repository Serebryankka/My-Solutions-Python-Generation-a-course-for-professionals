from collections import OrderedDict


def custom_sort(order_dict, by_values=False):
    for key, value in sorted(order_dict.items(), key=lambda x: x[1] if by_values else x[0]):
        order_dict.move_to_end(key)
      
