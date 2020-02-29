from os import path
import pandas as pd
from itertools import combinations

def get_reads(wildcards):
    '''Input function for rules that require Fastq files'''
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

def get_star_idx(wildcards):
    '''Determines correct path to star index folder'''
    STAR_IDX = (
        config["locations"]["star_idx_dir"] if
        config["locations"]["star_idx_dir"] != "" else
        rules.GenerateIndex.output
    ) #path.join(STAR_DIR, "index")
    return STAR_IDX

def get_aggregation_rule(wildcards):
    '''Determines correct input for aggregation rule based on tool selection'''
    available_tools = ["miso", "rmats", "whippet"]
    tool_selection = config["parameters"]["general"]["tools"]
    truth_array = [
        True if x in tool_selection else False
        for x in available_tools
    ]
    if all(truth_array):
        return expand(
            path.join(RESULT_DIR, "{comparison}", "overlap.all_tools.tab"),
            comparison=COMPARISONS
        )
    elif not all(truth_array):
        aggregation = []
        if "miso" in tool_selection:
            aggregation += expand(
                path.join(MISO_COMP_DIR, "{comparison}",
                    "{comparison}.merged.w_coord.miso_bf"),
                    comparison=COMPARISONS
            )
        if "rmats" in tool_selection:
            aggregation += expand(
                path.join(RMATS_DIR, "results", "{comparison}",
                    "{comparison}.merged.w_coord.tsv"),
                    comparison=COMPARISONS
            )
        if "whippet" in tool_selection:
            aggregation += expand(
                path.join(WHIPPET_DIR, "delta", "{comparison}",
                "{comparison}.diff.gz"),
                comparison=COMPARISONS
            )
        return aggregation

def get_bam_files(wildcards):
    '''Input function for rules that require BAM files'''
    samples = sorted(
        SAMPLE_SHEET[SAMPLE_SHEET["condition"] == wildcards.condition].index
    )
    bam_files = [path.join(
            STAR_DIR,
            "alignments",
            "{}".format(x),
            "Aligned.sortedByCoord.out.bam"
        ) for x in samples]
    bam_input = ",".join(bam_files)

    return bam_input
