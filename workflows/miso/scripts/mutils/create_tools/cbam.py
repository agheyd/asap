def write_list(sample_list, output_file):
    with open(output_file, 'w') as f:
        for item in sample_list:
            f.write("%s\n" % item)
    return None
