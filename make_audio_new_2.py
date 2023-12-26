from pydub import AudioSegment
import os
import moviepy.editor as mp
import csv

current_dir = os.path.dirname(os.path.abspath(__file__))
video_root_dir = os.path.join(current_dir, "..", "..", "Videos")
audio_root_dir = os.path.join(current_dir, "..", "..", "Audio")

def convert_video_to_audio(video_folder, start_frame, end_frame, csv_filename):
    video_path = os.path.join(video_root_dir, video_folder)

    if not os.path.exists(video_path):
        print(f"Folder not found: {video_path}")
        return False

    video_files = [f for f in os.listdir(video_path) if f.endswith(".MP4") or f.endswith(".avi")]

    if not video_files:
        print(f"No video files found in folder: {video_folder}")
        return False

    video_file_name = video_files[26]  
    video_file_path = os.path.join(video_path, video_file_name)

    if not os.path.exists(video_file_path):
        print(f"Video file not found: {video_file_name}")
        return False

    audio_filename = f"M02_S{str(video_folder[-3:]).zfill(4)}.wav"
    audio_file_path = os.path.join(audio_root_dir, audio_filename)

    if os.path.exists(audio_file_path):
        print(f"Audio file already exists for {video_folder}")
        return True

    try:
        video = mp.VideoFileClip(video_file_path)
        video = video.subclip(start_frame / video.fps, end_frame / video.fps)
        audio = video.audio
        audio.write_audiofile(audio_file_path, fps=30)  # fps를 30으로 설정
        print(f"Audio completed. CSV file used: {csv_filename}")
        return True
    except OSError as e:
        print(f"Error in file {video_file_path}, {e}")
        return False




def main():
    folders = [folder for folder in os.listdir(video_root_dir) if folder.startswith("Sentence")]
    folders.sort()

    for folder in folders:
        csv_filename = f"{folder}_VTOI_frame.csv"
        csv_file_path = os.path.join(current_dir, '..', '..', 'Sentence_cam27', csv_filename)

        if not os.path.exists(csv_file_path):
            print(f"CSV file not found for {folder}")
            continue

        with open(csv_file_path, 'r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                start_frame = int(row[' start_frame'])
                end_frame = int(row[' end_frame'])
                if convert_video_to_audio(folder, start_frame, end_frame, csv_filename):
                    print(f"Audio conversion for {folder} completed.")
                else:
                    print(f"Audio conversion for {folder} failed or folder does not exist.")



if __name__ == "__main__":
    main()
