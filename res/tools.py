import json

def reindex_with_name(dct):
        if str(type(dct))=="<class 'list'>":
            res = {dct[i]['name']: {k : dct[i][k] for k in dct[i] if k!='name'} for i in range(0, len(dct)) }
        else:
            res = ""
        return res


def web_concat_dict_list(dct):
    res = '&'.join([''.join(n) for n in [m for m in [[e+"="+f for e, f in a.items()] for a in dct]]])
    return res

def concat_dict_list_recursive(lst):
# returns a dict object from a list that has dict subitems
    res = {}
    if str(type(lst))=="<class 'list'>":
        for a in lst:
            if str(type(a))=="<class 'dict'>":
                for b,v in a.items():
                    if str(type(v))=="<class 'list'>":
                        v = concat_dict_list_recursive(v)
                    res[b]=v
    if str(type(lst))=="<class 'dict'>":
            for b,v in lst.items():
                if str(type(v))=="<class 'list'>":
                    v = concat_dict_list_recursive(v)

                res[b]=v
    return res
