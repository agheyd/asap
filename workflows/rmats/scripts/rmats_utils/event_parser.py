def parse_a3ss(x):

    if x.strand == "+":
        event_start = x.longExonStart_0base
        event_end = x.shortES
    elif x.strand == "-":
        event_start = x.shortEE
        event_end = x.longExonEnd

    x["coord"] = x.chr + ":" + str(event_start + 1) + "-" + str(event_end)

    return x

def parse_a5ss(x):

    if x.strand == "+":
        event_start = x.shortEE
        event_end = x.longExonEnd
    elif x.strand == "-":
        event_start = x.longExonStart_0base
        event_end = x.shortES

    x["coord"] = x.chr + ":" + str(event_start + 1) + "-" + str(event_end)

    return x

def parse_mxe(x):

    coord_list = ["{}:{}-{}".format(x.chr,
                                    x["1stExonStart_0base"],
                                    x["1stExonEnd"]),
                  "{}:{}-{}".format(x.chr,
                                    x["2ndExonStart_0base"],
                                    x["2ndExonEnd"])]

    x["coord_ae1"], x["coord_ae2"] = coord_list

    return x

def parse_ri(x):

    event_start = str(x.upstreamEE + 1)
    event_end = str(x.downstreamES)
    x["coord"] = x.chr + ":" + event_start + "-" + event_end

    return x

def parse_se(x):

    event_start = str(x.exonStart_0base + 1)
    event_end = str(x.exonEnd)
    x["coord"] = x.chr + ":" + event_start + "-" + event_end

    return x

def parse(data_dict):

    for k,i in data_dict.items():
        if k == "A3SS":
            data_dict[k] = data_dict[k].apply(lambda x: parse_a3ss(x), axis=1)
        elif k == "A5SS":
            data_dict[k] = data_dict[k].apply(lambda x: parse_a5ss(x), axis=1)
        elif k == "MXE":
            data_dict[k] = data_dict[k].apply(lambda x: parse_mxe(x), axis=1)
        elif k == "SE":
            data_dict[k] = data_dict[k].apply(lambda x: parse_se(x), axis=1)
        elif k == "RI":
            data_dict[k] = data_dict[k].apply(lambda x: parse_ri(x), axis=1)

    return data_dict
