def parse_a3ss(x):

    if x.strand == "+":
        event_start = x.longExonStart_0base + 1
        event_end = x.shortES
    elif x.strand == "-":
        event_start = x.shortEE + 1
        event_end = x.longExonEnd

    x["coord"] = "{}:{}-{}".format(
        x.chr, event_start, event_end
    )
    x["flank"] = "{}:{}-{}".format(
        x.chr, x.flankingES, x.flankingEE
    )

    return x

def parse_a5ss(x):

    if x.strand == "+":
        event_start = x.shortEE + 1
        event_end = x.longExonEnd
    elif x.strand == "-":
        event_start = x.longExonStart_0base
        event_end = x.shortES

    x["coord"] = "{}:{}-{}".format(
        x.chr, event_start, event_end
    )
    x["flank"] = "{}:{}-{}".format(
        x.chr, x.flankingES, x.flankingEE
    )

    return x

def parse_mxe(x):
    x["coord"] = "{}:{}-{}:{}-{}".format(
        x.chr,
        x["1stExonStart_0base"] + 1,
        x["1stExonEnd"],
        x["2ndExonStart_0base"] + 1,
        x["2ndExonEnd"]
    )
    x["flank"] = "{chr}:{u_start}-{u_end},{chr}:{d_start}-{d_end}".format(
        chr = x.chr,
        u_start = x.upstreamES,
        u_end = x.upstreamEE,
        d_start = x.downstreamES,
        d_end = x.downstreamEE
    )
    return x

def parse_ri(x):
    x["coord"] = "{}:{}-{}".format(
        x.chr, x.upstreamEE + 1, x.downstreamES
    )
    x["flank"] = "{chr}:{u_start}-{u_end},{chr}:{d_start}-{d_end}".format(
        chr = x.chr,
        u_start = x.upstreamES,
        u_end = x.upstreamEE,
        d_start = x.downstreamES,
        d_end = x.downstreamEE
    )
    return x

def parse_se(x):
    x["coord"] = "{}:{}-{}".format(
        x.chr, x.exonStart_0base + 1, x.exonEnd
    )
    x["flank"] = "{chr}:{u_start}-{u_end},{chr}:{d_start}-{d_end}".format(
        chr = x.chr,
        u_start = x.upstreamES,
        u_end = x.upstreamEE,
        d_start = x.downstreamES,
        d_end = x.downstreamEE
    )
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
