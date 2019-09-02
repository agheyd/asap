from glob import glob
from os import path
import pandas as pd
import rutils.import_tools.rmats_importer as ri
import rutils.coord_tools.parser as p
import rutils.coord_tools.harmonizers as h

rmats_dir = snakemake.params.rmats_dir

files = glob(path.join(rmats_dir, "*.JCEC.txt"))
types = [path.basename(x).split(".")[0] for x in files]
data_frames_split = [ri.import_files(x,y) for x,y in zip(files, types)]
data_dict = dict(zip(types, data_frames_split))

parsed_data_dict = p.parser_function(data_dict)
harmonized_data_dict = h.harmonizer_function(parsed_data_dict)
rmats_final_output = pd.concat(harmonized_data_dict.values())

rmats_final_output.to_csv(snakemake.output[0] , sep="\t", index=False)
