import argparse

class ArgParser:
    """
    Class parses command line argument to extract S3 bucket name.
    """
    # Parse_args() is called with no arguments.
    # ArgumentParser will determine the command-line arguments from sys.argv.

    def readBucketArgument(self):
        parser = argparse.ArgumentParser(
            description='Program requires S3 bucket name as a string. Example: --bucket \'04-09-2019\'',
            prog='StepUP')
        parser.add_argument('-b','--bucket', help='Name of S3 bucket as string. Example: 04-09-2019', required=True)
        args = parser.parse_args()
        return args.bucket
