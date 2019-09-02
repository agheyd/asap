from . import event_parsers as ep

def parser_function(data_dict):

    for k,i in data_dict.items():
        if k == "A3SS":
            data_dict[k] = data_dict[k].apply(lambda x: ep.parse_a3ss(x), axis=1)
        elif k == "A5SS":
            data_dict[k] = data_dict[k].apply(lambda x: ep.parse_a5ss(x), axis=1)
        elif k == "MXE":
            data_dict[k] = data_dict[k].apply(lambda x: ep.parse_mxe(x), axis=1)
        elif k == "SE":
            data_dict[k] = data_dict[k].apply(lambda x: ep.parse_se(x), axis=1)
        elif k == "RI":
            data_dict[k] = data_dict[k].apply(lambda x: ep.parse_ri(x), axis=1)

    return data_dict
