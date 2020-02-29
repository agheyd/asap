def write_list(bam_list, output_file):
    with open(output_file, 'w') as file:
        print(bam_list, file=file)
    return None
