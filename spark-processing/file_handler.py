from pyspark.sql.types import StringType
from pyspark.sql import Row
import boto3

class FileHandler:
    """
    Class handles methods related to speech file handling.
    """

    def getAudioFileLocations(self, bucket_name):
        s3_conn = boto3.client('s3')
        s3_result = s3_conn.list_objects_v2(Bucket=bucket_name, Delimiter = "/")

        if 'Contents' not in s3_result:
            return []

        file_list = []
        for key in s3_result['Contents']:
            file_list.append(key['Key'])
        print("List count = " + str(len(file_list)))

        while s3_result['IsTruncated']:
            continuation_key = s3_result['NextContinuationToken']
            s3_result = s3_conn.list_objects_v2(Bucket=bucket_name, Delimiter="/", ContinuationToken=continuation_key)
            for key in s3_result['Contents']:
                file_list.append(key['Key'])
            print("List count = " + str(len(file_list)))
        return file_list
