import sys
import argparse
import pathlib


class ArgparseUtils:

    def __init__(self, common_utils) -> None:
        """
        ArgparseUtils Constructor
        @param pass instance of CommonUtils() class
        @return None
        """
        parser = argparse.ArgumentParser(description='Argparse Example App.')

        # add all arguments
        parser.add_argument('-v','--verbose', dest='verbose', action='store_true',
            help='Turn on VERBOSE output')
        parser.add_argument('--var1', dest='var1', metavar='N', type=int, nargs='+',
            help='set var1')
        parser.add_argument('--var2', dest='var2', metavar='N', type=int, nargs='+',
            help='set var2')
        parser.add_argument('--var3', dest='var3', metavar='N', type=int, nargs='+',
            help='set var3')
        parser.add_argument('-d','--debug', dest='debug', action='store_true',
            help='Turn on DEBUG output')
        parser.add_argument('--clean', dest='clean', action='store_true',
            help='\nClean up python bytecode files')
        

        # grab cli flages from passed flags
        args = parser.parse_args()

        # print usage if no arg provided
        if len(sys.argv)==1:
            common_utils.prog_exit = True
            parser.print_help()
            print("")
            parser.exit()

        # sort flags passed by user
        if args.verbose == True:
            common_utils.verbose = True
        if args.debug == True:
            common_utils.debug = True
        if args.var1 is not None:
            common_utils.var1 = args.var1
            #print("arg.var1=" + str(args.var1) + ", common_utils.var1=" + str(common_utils.var1))
        if args.var2 is not None:
            common_utils.var2 = args.var2
            #print("arg.var2=" + str(args.var2) + ", common_utils.var2=" + str(common_utils.var2))
        if args.var3 is not None:
            common_utils.var3 = args.var3
            #print("arg.var3=" + str(args.var3) + ", common_utils.var3=" + str(common_utils.var3))
        if args.clean == True:
            # clean python dir of bytecode
            for p in pathlib.Path('.').rglob('*.py[co]'): p.unlink()
            for p in pathlib.Path('.').rglob('__pycache__'): p.rmdir()

