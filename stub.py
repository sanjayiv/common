import sys
import optparse

def parse_args():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--input", default=None, help="Input")
    parser.add_option("-o", "--output", default=None, help="Output")
    (options, args) = parser.parse_args()
    if not (options.input and options.output):
        parser.print_help()
        sys.exit(1)
    return (options, args)

if __name__ == '__main__':
    try:
        options, args = parse_args()
    except SystemExit, ee:
        if 1 == ee.code:
            print "Error: Mandatory arguments missing!!"
        else:
            print str(ee)
    except Exception, ee:
        import traceback
        print traceback.print_exc()

