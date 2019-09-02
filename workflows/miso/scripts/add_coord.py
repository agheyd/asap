import pandas as pd
from mutils.coord_tools import parser
from mutils.coord_tools import event_parsers

miso_table = pd.read_csv(snakemake.input[0], sep="\t")
miso_table_temp = miso_table.apply(lambda x: parser.parser_function(x), axis=1)
miso_table_final = event_parsers.melt_mxe(miso_table_temp)
miso_table_final.to_csv(snakemake.output[0], index=False, sep="\t")
