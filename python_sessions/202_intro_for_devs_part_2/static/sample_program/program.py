import sys


def main(args):
    '''This program takes arguments, capitalizes them, and writes to stdout.
    
       Alternatively:

       import sys
       for arg in sys.argv[1:]:
           sys.stdout.write(arg.upper() + '\n')
    
    '''
    try:
        for arg in args:
            upper_arg = arg.upper()
            sys.stdout.write(upper_arg + '\n')
        sys.exit(0)
    except Exception:
        sys.stderr.write('Error!\n')
        sys.exit(1)


if __name__ == '__main__':
    main(sys.argv[1:])

