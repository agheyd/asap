import pandas as pd

def parse_a3ss(event_name):

    strand = event_name.split(":")[-1]
    alt_exon = event_name.split("@")[1].split(":")
    chrom = alt_exon[0]

    if strand == '+':

        start = int(alt_exon[1].split("|")[0])
        con = int(alt_exon[1].split("|")[1]) -1
        end = int(alt_exon[-2])

        alt_element = chrom + ':' + str(start) + '-' + str(con)

    elif strand == '-':

        start = int(alt_exon[-2]) + 1
        con = int(alt_exon[1].split("|")[0]) + 1
        end = int(alt_exon[1].split("|")[1])

        alt_element = chrom + ':' + str(con) + '-' + str(end)

    return alt_element

def parse_a5ss(event_name):

    strand = event_name.split(":")[-1]
    alt_exon = event_name.split("@")[0].split(":")
    chrom = alt_exon[0]

    if strand == '+':

        start = int(alt_exon[1])
        con = int(alt_exon[-2].split("|")[0]) + 1
        end = int(alt_exon[-2].split("|")[1])

        alt_element = chrom + ':' + str(con) + '-' + str(end)

    elif strand == '-':

        start = int(alt_exon[-2].split("|")[0])
        con = int(alt_exon[-2].split("|")[1]) - 1
        end = int(alt_exon[1])

        alt_element = chrom + ':' + str(start) + '-' + str(con)

    return alt_element

def melt_mxe(table):

    main_table = table[table["type"] != "MXE"]
    mxe_table = table[table["type"] == "MXE"]

    mxe_table_new = pd.DataFrame()

    for index, row in mxe_table.iterrows():
        entry = row
        import ast
        coord = entry["coord"]

        ae1 = coord[0]
        ae1_entry = entry.copy()
        ae1_entry["coord"] = ae1

        ae2 = coord[1]
        ae2_entry = entry.copy()
        ae2_entry["coord"] = ae2

        entry = pd.concat([ae1_entry, ae2_entry], axis=1).T
        mxe_table_new = mxe_table_new.append(entry)

    miso_table = pd.concat([main_table, mxe_table_new]).reset_index(drop=True)

    return miso_table

def parse_mxe(event_name):

    strand = event_name.split(":")[-1]

    if strand == '+':

        ae1 = event_name.split("@")[1].rsplit(":",1)[0]
        ae2 = event_name.split("@")[2].rsplit(":",1)[0]

    elif strand == '-':

        ae1 = event_name.split("@")[2].rsplit(":",1)[0]
        ae2 = event_name.split("@")[1].rsplit(":",1)[0]

    ae1_chr, ae1_start, ae1_end  = ae1.split(":")
    ae1 = "{}:{}-{}".format(ae1_chr, ae1_start, ae1_end)

    ae2_chr, ae2_start, ae2_end  = ae2.split(":")
    ae2 = "{}:{}-{}".format(ae2_chr, ae2_start, ae2_end)

    return [ae1, ae2]

def parse_ri(event_name):

    strand = event_name.split(":")[-1]
    chrom = event_name.split(":")[0]

    if strand == '+':

        ue = event_name.split("@")[0]
        ue_end = ue.split(":")[1].split("-")[1]
        de = event_name.split("@")[1]
        de_start = de.split(":")[1].split("-")[0]

    elif strand == '-':

        ue = event_name.split("@")[1]
        ue_end = ue.split(":")[1].split("-")[0]
        de = event_name.split("@")[0]
        de_start = de.split(":")[1].split("-")[1]

    intron_coord = chrom + ':' + str(int(ue_end)+1) + '-' + str(int(de_start)-1)

    return intron_coord

def parse_se(event_name):

    strand = event_name.split(":")[-1]
    ae = event_name.split("@")[1].rsplit(":",1)[0]

    ae_chr, ae_start, ae_end  = ae.split(":")
    ae = "{}:{}-{}".format(ae_chr, ae_start, ae_end)

    return ae
