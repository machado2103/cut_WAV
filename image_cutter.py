from pydub import AudioSegment
import os
import wave

def cut_wav_files(input_folder, output_folder, segment_duration):
    # Ensure the output folder exists
    os.makedirs(output_folder, exist_ok=True)

    # Iterate through all files in the input folder
    for filename in os.listdir(input_folder):
        if filename.endswith(".wav"):
            # Load the audio file
            audio_path = os.path.join(input_folder, filename)

            # Read the WAV file using the wave module
            with wave.open(audio_path, 'rb') as wav_file:
                # Get the parameters of the original WAV file
                channels = wav_file.getnchannels()
                sample_width = wav_file.getsampwidth()
                frame_rate = wav_file.getframerate()
                num_frames = wav_file.getnframes()

                # Calculate the number of segments
                num_segments = num_frames // (segment_duration * frame_rate)

                # Read and cut the audio into 5-second segments
                for i in range(num_segments):
                    start_frame = i * segment_duration * frame_rate
                    end_frame = (i + 1) * segment_duration * frame_rate
                    wav_file.setpos(start_frame)
                    segment_frames = wav_file.readframes(end_frame - start_frame)

                    # Create an AudioSegment from the segment frames
                    segment = AudioSegment(
                        segment_frames,
                        frame_rate=frame_rate,
                        sample_width=sample_width,
                        channels=channels
                    )

                    # Save the segment to the output folder
                    output_filename = f"{os.path.splitext(filename)[0]}_segment_{i+1}.wav"
                    output_path = os.path.join(output_folder, output_filename)
                    segment.export(output_path, format="wav")

            print(f"Audio file '{filename}' processed successfully.")

if __name__ == "__main__":
    # Set the input and output folders
    input_folder = "input/WAV/folder/path"
    output_folder = "output/WAV/folder/path"

    # Set the duration for each segment
    segment_duration = 5000  # in miliseconds. In this case is 5s but  change to whatever duration)

    # Call the function to cut the WAV files
    cut_wav_files(input_folder, output_folder, segment_duration)
