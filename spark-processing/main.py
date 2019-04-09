import sys
from argument_parser import ArgParser
### main method that executes batch job ###

if __name__ == '__main__':
    arguments = ArgParser()
    s3_bucket_name = arguments.readBucketArgument()
    print("Bucket name: \"" + s3_bucket_name + "\"")
