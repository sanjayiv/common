import sys
import optparse

from utils import formatted_filepath, get_logger

def parse_args():
    default_output = formatted_filepath('output', datestamp=True)
    default_logger = formatted_filepath(suffix='log', sep='.')
    parser = optparse.OptionParser()
    parser.add_option("-i", "--input", default=None, help="Input")
    parser.add_option("-o", "--output", default=default_output, help="Output name")
    parser.add_option("-l", "--logger", default=default_logger, help="Log name")
    (options, args) = parser.parse_args()
    if not (options.input and options.output):
        parser.print_help()
        sys.exit(1)
    return (options, args)

## just like that
## added this to test out git windows
## commit -p
if __name__ == '__main__':
    try:
        options, args = parse_args()
        print options.input, options.output, options.logger
        logger = get_logger(options.logger)
    except SystemExit, ee:
        if 1 == ee.code:
            print "Error: Mandatory arguments missing!!"
        else:
            print str(ee)
    except Exception, ee:
        import traceback
        print traceback.print_exc()

