#!/usr/bin/env python
import subprocess, argparse, yaml, os

def parseArgs():
    parser = argparse.ArgumentParser(description='Receive command line arguments')
    parser.add_argument('snakefile', type=os.path.abspath, help='Path to snakefile')
    parser.add_argument('--until', type=str, metavar="TARGET", help='Runs the pipeline until it reaches the specified rules or files. Only runs jobs that are dependencies of the specified rule or files, does not run sibling DAGs.')
    parser.add_argument('--configfile', type=str, help='Specify or overwrite the config file of the workflow'
                        '(see the docs). Values specified in JSON or YAML'
                        'format are available in the global config dictionary'
                        'inside the workflow.')
    args = parser.parse_args()
    return args

def ClusterCmd():

    cluster_cmd = (
    'sbatch '
    '--parsable '
    '--partition={params.partition} '
    '--nodes={params.nodes} '
    '--ntasks={params.ntasks} '
    '--time={params.time} '
    '--mem={params.mem} '
    '--job-name={rule} '
    '--mail-user={params.mail_user} '
    '--mail-type={params.mail_type} '
    '--qos=medium')

    return cluster_cmd

def AddExtra(args):
    extra = ''

    if args.until:
        extra += "--until {}".format(args.until)
    else:
        pass

    if args.configfile:
        extra += "--configfile {}".format(args.configfile)
    else:
        pass

    return extra

def RunSnake():

    args = parseArgs()
    wdir = os.path.dirname(args.snakefile)
    os.chdir(wdir)

    snakefile_path = args.snakefile
    cluster_cmd = ClusterCmd()
    extra = AddExtra(args)

    cmd = (
    'snakemake '
    '-j 40 '
    '--use-conda '
    '--use-singularity '
    '--singularity-args "--bind /scratch:/scratch " '
    '--cluster "{}" '
    '--restart-times 3 '
    '-s {} '
    '{}'
    ).format(cluster_cmd, snakefile_path, extra)

    subprocess.run(cmd, shell=True)

RunSnake()
