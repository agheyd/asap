def GetReads(wildcards):

    entry = SAMPLE_SHEET.loc["{wildcard}".format(wildcard=wildcards)]
    read1 = entry.read1
    read2 = entry.read2

    if str(read2) != "nan":
        reads = [read1, read2]
    elif str(read2) == "nan":
        reads = [read1]

    fq_path = config["locations"]["fq_dir"]
    reads = [path.join(fq_path, x) for x in reads]

    return reads
