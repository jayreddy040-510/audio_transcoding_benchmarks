import time
import os
from pydub import AudioSegment
import shutil

def resample_pydub(input_filename, output_filename):
    temp_filename = "temp_" + input_filename
    shutil.copyfile(input_filename, temp_filename)

    start_time = time.time()
    audio_segment = AudioSegment.from_mp3(temp_filename)
    original_frame_rate = audio_segment.frame_rate
    print(f"original frame rate: {original_frame_rate}", flush=True)

    start_downsampling_time = time.time()
    downsampled_audio_segment = audio_segment.set_frame_rate(16000)
    end_downsampling_time = time.time()

    altered_frame_rate = downsampled_audio_segment.frame_rate
    print(f"altered frame rate: {altered_frame_rate}", flush=True)
    print(f"total time to downsample: {end_downsampling_time - start_downsampling_time}", flush=True)

    os.remove(temp_filename)

resample_pydub("test.mp3", "downsampled_test.mp3")

