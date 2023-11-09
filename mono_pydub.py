import time
from pydub import AudioSegment

def mono_conversion_pydub(input_filename, output_filename):
    # Load the audio file
    audio_segment = AudioSegment.from_file(input_filename)
    original_channels = audio_segment.channels
    print(f"Original number of channels: {original_channels}", flush=True)

    # Measure the time it takes to set channels to mono
    start_time = time.time()
    mono_audio_segment = audio_segment.set_channels(1)
    conversion_time = time.time() - start_time

    altered_channels = mono_audio_segment.channels
    print(f"Altered number of channels: {altered_channels}", flush=True)
    print(f"Total time to convert to mono: {conversion_time}", flush=True)

    # Save the mono audio if needed
    mono_audio_segment.export(output_filename, format="mp3")

# Specify the input and output filenames
input_filename = 'test.mp3'
output_filename = 'test_mono.mp3'

# Run the mono conversion function
mono_conversion_pydub(input_filename, output_filename)

