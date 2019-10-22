#!/usr/bin/env python
import subprocess, argparse, yaml, os

def parseArgs():
    parser = argparse.ArgumentParser(description='Receive command line arguments')

    parser.add_argument('snakefile', type=os.path.abspath, help='Path to snakefile')

    parser.add_argument('--until', type=str, metavar="TARGET", help=('''
    Runs the pipeline until it reaches the specified rules or files.
    Only runs jobs that are dependencies of the specified rule or files,
    does not run sibling DAGs.
    '''))

    parser.add_argument('--configfile', metavar="CONFIG", type=str, help=('''
    Specify or overwrite the config file of the workflow
    (see the docs). Values specified in JSON or YAML
    format are available in the global config dictionary
    inside the workflow.
    '''))

    parser.add_argument('--tool', choices=["miso", "rmats", "whippet", "all"], type=str, default="all", help=('''
    Specify which tools to include if only running a subset of tools.
    Currently performs overlap analysis only if all tools are included.
    Default: all
    '''))

    parser.add_argument('--restart', metavar="NUM", type=str, default="3", help=('''
    Number of times to restart failing jobs.
    Mainly used for download pipelines where jobs might fail due to connectivity issues.
    Default: 3
    '''))

    parser.add_argument('--rerun', type=str, help=('''
    Re-run all jobs the output of which is recognized as incomplete.
    '''))

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
        extra += "--until {} ".format(args.until)
    else:
        pass

    if args.configfile:
        extra += "--configfile {} ".format(args.configfile)
    else:
        pass

    if args.tool:
        if args.tool == "miso":
            extra += "--until AddMisoCoord "
        elif args.tool == "rmats":
            extra += "--until AddrMATSCoord "
        elif args.tool == "whippet":
            extra += "--until WhippetDelta "
        elif args.tool == "all":
            extra += ""

    if args.restart:
        extra += "--restart-times {} ".format(args.restart)

    if args.rerun:
        extra += "--rerun-incomplete "

    return extra

def RunSnake():

    args = parseArgs()

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
    '-s {} '
    '{}'
    ).format(cluster_cmd, snakefile_path, extra)

    subprocess.run(cmd, shell=True)

RunSnake()
