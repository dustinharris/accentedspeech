import boto3
import os
import librosa
from datetime import datetime

class AudioProcessor:
    """
    Class handles methods related to audio processing of binaries.
    """

    def processFromS3(self, audio_df_row):
        file_path = audio_df_row.url
        # strip off the starting s3n:// from the bucket
        current_bucket = os.path.dirname(str(file_path))[6:]
        remote_file_name = os.path.basename(str(file_path))
        local_file_name = os.path.basename(str(file_path))
        nat_country = "test"
        target_lang = "test"

        s3_res = boto3.resource('s3')
        s3_res.Bucket(current_bucket).download_file(remote_file_name,local_file_name)

        y, sr = librosa.load(local_file_name)
        audio_duration = librosa.get_duration(y=y, sr=sr)
        minutes = "00"
        seconds = "%02d" % (int(audio_duration),)
        milliseconds = "%02d" % ((audio_duration - int(audio_duration)),)
        contents = librosa.feature.mfcc(y=y, sr=sr)
        final_audio_duration = str(str(minutes) + ":" + str(seconds) + ":" + str(milliseconds))
        date_time = str(datetime.now(tz=None))

        if len(contents):
            return (nat_country, target_lang, str(contents), "", str(file_path), final_audio_duration, date_time)
