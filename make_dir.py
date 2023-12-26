import csv
import os

# CSV 파일이 있는 디렉토리 경로
csv_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'Sentence'))
# 시작 폴더 번호
a = 201

# CSV 파일 디렉토리에서 파일 목록을 가져오고 "Sentence"로 시작하는 파일만 처리
for csv_file in os.listdir(csv_dir):
    if csv_file.startswith("Sentence") and csv_file.endswith("_frame.csv"):
        csv_file_path = os.path.join(csv_dir, csv_file)

        # "frame" 폴더를 생성합니다.
        with open(csv_file_path, 'r') as csv_file:
            csv_reader = csv.DictReader(csv_file)

            for row in csv_reader:
                  # 파일 이름에서 확장자 제거
                image_root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '2D_images', f'Sentence{a}'))

                start_frame = int(row[' start_frame'])  # 시작 프레임
                end_frame = int(row[' end_frame'])  # 끝 프레임

                frame_difference = abs(end_frame - start_frame)
                frame_num = frame_difference // 2

                

                # "Sentence"로 시작하는 폴더가 이미 존재하면 프레임 폴더 생성
                if os.path.exists(image_root_dir):
                    for i in range(frame_num):
                        frame_folder = os.path.join(image_root_dir, f'frame{str(i).zfill(3)}')

                        # 폴더가 존재하지 않는 경우 생성
                        if not os.path.exists(frame_folder):
                            os.makedirs(frame_folder)

                        print(f"Frame Folder Created: {frame_folder}")

    a = a + 1 