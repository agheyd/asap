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
