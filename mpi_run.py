import sys
import subprocess
from util.arg_parser import ArgParser
from util.logger import Logger
import trace

def main():
    # Command line arguments
    args = sys.argv[1:]
    arg_parser = ArgParser()
    arg_parser.load_args(args)

    num_workers = arg_parser.parse_int('num_workers', 1)
    assert(num_workers > 0)

    Logger.print('Running with {:d} workers'.format(num_workers))
    cmd = 'mpiexec -n {:d} python DeepMimic_Optimizer.py '.format(num_workers)
    cmd += ' '.join(args)
    Logger.print('cmd: ' + cmd)
    subprocess.call(cmd, shell=True)
    return

# tracer = trace.Trace(
#     ignoredirs=[sys.prefix, sys.exec_prefix],
#     ignoremods=[
#         'inspect', 'contextlib', '_bootstrap',
#         '_weakrefset', 'abc', 'posixpath', 'genericpath', 'textwrap'
#     ],
#     trace=1,
#     count=0)


if __name__ == '__main__':
    #sys.stdout = open('trace_{:04d}.txt'.format(COMM_WORLD.rank), 'w')
    #tracer.runfunc(main)
    main()

