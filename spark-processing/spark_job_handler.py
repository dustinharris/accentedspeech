from pyspark.sql import Row
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType
from pyspark.sql.types import StringType
from audio_processing import AudioProcessor
import pyspark
from pyspark.sql import SparkSession
#from pyspark import SparkConf, SparkContext

class SparkAudioProcessing:
    """
    Class handles methods related to audio processing with Spark.
    """
    def __init__(self):
        self.spark = SparkSession \
            .builder \
            .appName("ListenUp") \
            .getOrCreate()

    def processFiles(self, audio_files_array):
        audio_processor = AudioProcessor()
        audio_files_urls_df = self.audioUrlArrayToDF(audio_files_array)

        # Farm out audio files to Spark workers with a map
        processed_audio_rdd = (
            audio_files_urls_df
            .rdd
            .map(audio_processor.processFromS3)
        )

        processed_audio_schema = StructType([StructField("nativecountry", StringType(), False),
                                             StructField("languagerecorded", StringType(), False),
                                             StructField("mfc", StringType(), False),
                                             StructField("transcription", StringType(), False),
                                             StructField("audiofilelocation", StringType(), False),
                                             StructField("audiolength", StringType(), False),
                                             StructField("processingdatetime", StringType(), False)])

        processed_audio_df = (
            processed_audio_rdd
            .toDF(processed_audio_schema)
            .select("nativecountry", "languagerecorded", "mfc", "transcription", "audiofilelocation", "audiolength", "processingdatetime")
        )

        (
            processed_audio_df
        )

        return processed_audio_df

    def audioUrlArrayToDF(self, audio_files_array):
        url_list_schema = StructType([StructField("url", StringType(), True)])
        url_list_rdd = self.spark.sparkContext.parallelize(audio_files_array).map (lambda x: Row(x))
        audio_files_urls_df = self.spark.createDataFrame(url_list_rdd, url_list_schema)
        return audio_files_urls_df
