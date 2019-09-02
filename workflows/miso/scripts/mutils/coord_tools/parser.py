from . import event_parsers as p

def parser_function(x):

    if x.type == "A3SS":
        x["coord"] = p.parse_a3ss(x.event_name)
    elif x.type == "A5SS":
        x["coord"] = p.parse_a5ss(x.event_name)
    elif x.type == "MXE":
        x["coord"] = p.parse_mxe(x.event_name)
    elif x.type == "SE":
        x["coord"] = p.parse_se(x.event_name)
    elif x.type == "RI":
        x["coord"] = p.parse_ri(x.event_name)

    return x
