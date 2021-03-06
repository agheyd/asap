from os import path
from itertools import combinations
import pandas as pd

## Cluster variables
EMAIL = config["parameters"]["user"]["email"]
EMAIL_TYPE = "none" if EMAIL == "" else "end"

## General input variables
GENOME = config["locations"]["genome"]
ANNOTATION = config["locations"]["annotation"]
SAMPLE_SHEET = pd.read_csv(config["locations"]["sample_sheet"]).set_index("sampleID")
SAMPLES = sorted(SAMPLE_SHEET.index)
CONDITIONS = sorted(set(SAMPLE_SHEET["condition"]))
COMPARISONS = ["{}_vs_{}".format(e[0], e[1]) for e in sorted(combinations(CONDITIONS, 2))]

## General output variables
OUTPUT_DIR = config["locations"]["output_dir"]
RESULT_DIR = path.join(OUTPUT_DIR, "results")
LOG_DIR = path.join(OUTPUT_DIR, "log")

## Star specific variables
STAR_DIR = path.join(OUTPUT_DIR, "star")

## Miso specific variables
MISO_IDX_DIR = config["locations"]["miso_annotation_dir"]
MISO_IDX_NAMES = config["parameters"]["miso"]["annotations"]
MISO_DIR = path.join(OUTPUT_DIR, "miso")
MISO_RUN_DIR = path.join(MISO_DIR, "run")
MISO_SUM_DIR = path.join(MISO_DIR, "summary")
MISO_COMP_DIR = path.join(MISO_DIR, "comparison")

## rMATS specific variables
RMATS_DIR = path.join(OUTPUT_DIR, "rmats")

## Whippet specific variables
WHIPPET_DIR = path.join(OUTPUT_DIR, "whippet")
WHIPPET_IDX = config["locations"]["whippet_idx"] if config["locations"]["whippet_idx"] != "" else path.join(WHIPPET_DIR, "index", "index.jls")
