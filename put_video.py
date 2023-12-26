import os
import shutil

def move_lowest_video(destination_folder):
    source_folder = os.getcwd()
    video_files = [f for f in os.listdir(source_folder) if f.endswith(('.mp4', '.avi', '.mkv'))]

    if not video_files:
        print(f"{source_folder} 폴더에서 영상 파일을 찾을 수 없습니다.")
        return

    # 영상 파일을 오름차순으로 정렬
    sorted_videos = sorted(video_files)

    # 'SentenceXXX' 폴더에 가장 낮은 영상을 이동
    for i, video in enumerate(sorted_videos):
        destination_path = os.path.join(destination_folder, f"Sentence{i+1:03d}", video)
        os.makedirs(os.path.dirname(destination_path), exist_ok=True)

        source_path = os.path.join(source_folder, video)

        if os.path.exists(source_path):  # 파일이 존재할 때만 이동
            shutil.move(source_path, destination_path)
            print(f"{destination_folder} 폴더로 {video} 파일을 이동했습니다.")
        else:
            print(f"{source_folder} 폴더에서 {video} 파일을 찾을 수 없어 이동하지 않았습니다.")

if __name__ == "__main__":
    # 'Sentence001'부터 'Sentence500'까지의 폴더에 대해 수행
    for i in range(1, 501):
        move_lowest_video(f"Sentence{i:03d}")
