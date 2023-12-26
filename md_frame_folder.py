import csv
import os



csv_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'Sentence'))
image_root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '2D_images'))
video_root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'Videos'))

frame_ranges = {}  # "Sentence"로 시작하는 동영상 파일의 시작 및 끝 프레임을 저장할 딕셔너리

# CSV 파일 디렉토리에서 파일 목록을 가져오고 "Sentence"로 시작하는 파일만 처리
for csv_file in os.listdir(csv_dir):
    if csv_file.startswith("Sentence") and csv_file.endswith(".csv"):
        csv_file_path = os.path.join(csv_dir, csv_file)

        # CSV 파일 열기
        with open(csv_file_path, 'r', newline='') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            
            for row in csv_reader:
                video_name = row['file_names']  # 동영상 파일 이름
                start_frame = int(row[' start_frame'])  # 시작 프레임
                end_frame = int(row[' end_frame'])  # 끝 프레임

                frame_ranges[video_name] = (start_frame, end_frame)

# frame_ranges 딕셔너리에 저장된 정보 확인
for video_name, (start_frame, end_frame) in frame_ranges.items():
    print(f"Video: {video_name}, Start Frame: {start_frame}, End Frame: {end_frame}")   


frame_difference = abs(end_frame - start_frame)
print(f"Frame Difference: {frame_difference}")

frame_num = int(frame_difference/2)
frame_folder = os.path.join(image_root_dir, f'frame{frame_num:04d}')

# 이제 frame_ranges 딕셔너리에 저장된 정보를 사용하여 동영상 편집 작업을 수행할 수 있습니다.
# 필요한 동영상 파일만 처리되었습니다.
