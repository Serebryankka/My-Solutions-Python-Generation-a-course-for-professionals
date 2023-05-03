def dict_travel(nested_dicts):
    def rec(nested_dicts, string):
        for k, v in sorted(nested_dicts.items()):
            if type(v) is dict:
                rec(v, f'{string}{k}.')
            else:
                #print(f'{string}: {v}')
                print(f'{string}{k}: {v} ')

    rec(nested_dicts, '')
