import cv2
import os
import csv
from datetime import datetime

now = datetime.now()

current_dir = os.path.dirname(os.path.abspath(__file__))
video_root_dir = os.path.join(current_dir, "..", "..", "Videos")
image_root_dir = os.path.join(current_dir, "..", "..", "2D_images")

def process_video_range(video_folder, start_index, end_index):
    video_path = os.path.join(video_root_dir, video_folder)

    if not os.path.exists(video_path):
        print(f"Folder not found: {video_path}")
        return False

    video_files = [f for f in os.listdir(video_path) if f.endswith(".MP4") or f.endswith(".avi")]

    if not video_files:
        print(f"No video files found in folder: {video_folder}")
        return False

    csv_filename = f"{video_folder}_VTOI_frame.csv"
    csv_file_path = os.path.abspath(os.path.join(current_dir, '..', '..', 'Sentence_cam27', csv_filename))

    if not os.path.exists(csv_file_path):
        print(f"CSV file not found: {csv_filename}")
        return False

    frame_interval = 1  # Set frame_interval to 1 for continuous frames

    with open(csv_file_path, 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            start_frame = int(row[' start_frame'])
            end_frame = int(row[' end_frame'])
            file_name = row['file_names']

            for frame_num in range(start_frame, end_frame + 1, frame_interval):
                frame_num_save = frame_num
                video_file_name = os.path.splitext(file_name)[0]
                frame_folder = os.path.join(image_root_dir, video_folder, f'frame{frame_num:03d}')
                if not os.path.exists(frame_folder):
                    os.makedirs(frame_folder)

                frame_path = os.path.join(frame_folder, f'{video_file_name}_{frame_num:03d}.png')

                # 이미지 파일이 존재하지 않을 때만 저장
                if not os.path.exists(frame_path):
                    video = cv2.VideoCapture(os.path.join(video_path, video_file_name + ".MP4"))
                    video.set(cv2.CAP_PROP_POS_FRAMES, frame_num_save)
                    ret, frame = video.read()

                    if ret:
                        cv2.imwrite(frame_path, frame)

    return True

def main():
    folders = [folder for folder in os.listdir(video_root_dir) if folder.startswith("Sentence")]
    folders.sort()
    
    start_index = 2  # 시작 인덱스 지정
    end_index = 2  # 끝 인덱스 지정

    processed_count = 0
    for folder in folders[start_index - 1:end_index]:  # 시작부터 끝 인덱스까지 처리
        if process_video_range(folder, start_index, end_index):
            processed_count += 1
            print(f"Processing of {folder} completed. ", now.time())
        else:
            print(f"Processing of {folder} failed or folder does not exist.")

    print("Image extraction for the 001-010 completed. ", now.time())

if __name__ == "__main__":
    main()