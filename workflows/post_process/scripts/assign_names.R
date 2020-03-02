library(tidyverse)
library(rtracklayer)

# Helpers
format.coords <- function(coord){
  split = strsplit(coord, split = ":")[[1]]
  if (length(split) == 2) {
    return(coord)
  } else if (length(split) == 3) {
    start = strsplit(split[2], "-")[[1]][1]
    end = strsplit(split[3], "-")[[1]][2]
    return(str_glue("{split[1]}:{start}-{end}"))
  }
}

format.func <- function(list){
  return(
    paste(
      list, sep="", collapse = ", "
    ))
}

# Import data
as.table <- read_tsv(
  snakemake@input[[1]]
)

# Import GTF
gtf <- import(
  snakemake@config[["locations"]][["annotation"]]
)
gtf.genes <- gtf[gtf$type == "gene"]

# Get coord ranges

coord.ranges <- as.table %>%
  mutate(tmp_coord = sapply(coord, format.coords)) %>%
  separate(tmp_coord, into = c("chr", "start", "end")) %>%
  makeGRangesFromDataFrame(keep.extra.columns = T)

# Assign gene names
overlap <- findOverlaps(
  query = coord.ranges,
  subject = gtf.genes,
  type = "any"
)

q.hits <- coord.ranges[queryHits(overlap)]
s.hits <- gtf.genes[subjectHits(overlap)]

q.hits$gene <- s.hits$gene_name
q.hits$gene_type <- s.hits$gene_type

coords.named <- as_tibble(q.hits) %>%
  select(
    coord, gene, gene_type
  )

coords.consolidated <- coords.named %>%
  distinct() %>%
  group_by(coord) %>%
  summarise(
    gene = list(gene),
    gene_type = list(gene_type)
  ) %>%
  ungroup() %>%
  mutate(
    gene = sapply(gene, format.func),
    gene_type = sapply(gene_type, format.func)
  )

as.table.consolidated <- as.table %>%
  full_join(coords.consolidated) %>%
  replace_na(list(gene = "unknown", gene_type = "unknown"))

# Write table to disc
write_tsv(
  as.table.consolidated,
  snakemake@output[[1]]
)