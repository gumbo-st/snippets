
import argparse


class ArgparseUtils:

    def __init__(self, common_utils) -> None:
        """
        ArgparseUtils Constructor
        @param pass instance of CommonUtils() class
        @return None
        """
        parser = argparse.ArgumentParser(description='Argparse Example App.')
        
        # add all arguments
        parser.add_argument('--var1', dest='var1', metavar='N', type=int, nargs='+',
            help='set var1')
        parser.add_argument('--var2', dest='var2', metavar='N', type=int, nargs='+',
            help='set var2')
        parser.add_argument('--var3', dest='var3', metavar='N', type=int, nargs='+',
            help='set var3')

        # grab cli flages from passed flags
        args = parser.parse_args()

        # sort flags passed by user 
        if args.var1 is not None:
            common_utils.var1 = args.var1
            print("arg.var1=" + str(args.var1) + ", common_utils.var1=" + str(common_utils.var1))
        if args.var2 is not None:
            common_utils.var2 = args.var2
            print("arg.var2=" + str(args.var2) + ", common_utils.var2=" + str(common_utils.var2))
        if args.var3 is not None:
            common_utils.var3 = args.var3
            print("arg.var3=" + str(args.var3) + ", common_utils.var3=" + str(common_utils.var3))

