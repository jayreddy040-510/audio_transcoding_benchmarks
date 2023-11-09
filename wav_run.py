import time
from pydub import AudioSegment
import av

def transcode_pydub(input_filename, output_filename):
    start_time = time.time()
    audio_segment = AudioSegment.from_wav(input_filename)
    read_time = time.time() - start_time

    start_write_time = time.time()
    audio_segment.export(output_filename, format="mp3")
    write_time = time.time() - start_write_time

    total_time = read_time + write_time

    return read_time, write_time, total_time

def transcode_pyav(input_filename, output_filename):
    start_time = time.time()
    input_container = av.open(input_filename)
    read_time = time.time() - start_time

    start_write_time = time.time()
    output_container = av.open(output_filename, 'w')
    output_stream = output_container.add_stream('libmp3lame', rate=16000)
    output_stream.bit_rate = 192000 # Set the bit rate for the MP3 encoding if needed

    for frame in input_container.decode(audio=0):
        packet = output_stream.encode(frame)
        output_container.mux(packet)

    # Flush the remaining packets
    for packet in output_stream.encode():
        output_container.mux(packet)

    output_container.close()
    input_container.close()

    write_time = time.time() - start_write_time
    total_time = read_time + write_time

    return read_time, write_time, total_time

# Define the input and output filenames
input_filename = 'test_pydub.wav'
pydub_output_filename = 'test_pydub.mp3'
pyav_output_filename = 'test_pyav.mp3'

# Benchmarking PyDub conversion
pydub_read_time, pydub_write_time, pydub_total_time = transcode_pydub(input_filename, pydub_output_filename)
print(f"PyDub conversion - Read time: {pydub_read_time:.4f} seconds, "
      f"Write time: {pydub_write_time:.4f} seconds, "
      f"Total time: {pydub_total_time:.4f} seconds.")

# Benchmarking PyAV conversion
pyav_read_time, pyav_write_time, pyav_total_time = transcode_pyav(input_filename, pyav_output_filename)
print(f"PyAV conversion - Read time: {pyav_read_time:.4f} seconds, "
      f"Write time: {pyav_write_time:.4f} seconds, "
      f"Total time: {pyav_total_time:.4f} seconds.")

