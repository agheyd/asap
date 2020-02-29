from glob import glob
from os import path
import pandas as pd
import rmats_utils.rmats_importer as importer
import rmats_utils.event_parser as parser
import rmats_utils.rmats_formater as formater

rmats_dir = snakemake.params.rmats_dir

files = glob(path.join(rmats_dir, "*.JCEC.txt"))
types = [path.basename(x).split(".")[0] for x in files]
data_frames_split = [importer.import_files(x,y) for x,y in zip(files, types)]
data_dict = dict(zip(types, data_frames_split))

parsed_data_dict = parser.parse(data_dict)
formated_data_dict = formater.format(parsed_data_dict)
rmats_final_output = pd.concat(formated_data_dict.values())
rmats_final_output.to_csv(snakemake.output[0], sep="\t", index=False)
