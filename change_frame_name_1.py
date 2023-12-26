import os
import re

# 경로 설정
base_path = r'F:\\vtoi5_F\\231212\\Model1\\2D_images'

# base_path에서 모든 폴더를 순회
for root, dirs, files in os.walk(base_path):
    for dir_name in dirs:
        if dir_name.startswith('Sentence'):
            sentence_path = os.path.join(root, dir_name)
            frame_dirs = [d for d in os.listdir(sentence_path) if d.startswith('frame')]
            frame_dirs.sort(key=lambda x: int(re.search(r'\d+', x).group()))  # 숫자로 정렬
            for i, frame_dir_name in enumerate(frame_dirs, start=1):
                new_frame_dir_name = f'F{i:03d}'  # 세 자릿수 없이 변경
                old_frame_dir_path = os.path.join(sentence_path, frame_dir_name)
                new_frame_dir_path = os.path.join(sentence_path, new_frame_dir_name)
                if not os.path.exists(new_frame_dir_path):
                    os.rename(old_frame_dir_path, new_frame_dir_path)
                else:
                    # 이미 해당 이름의 폴더가 존재하면 다음 숫자로 시도
                    j = i + 1
                    while os.path.exists(os.path.join(sentence_path, f'F{j:03d}')):
                        j += 1
                    new_frame_dir_name = f'Frame{j}'
                    new_frame_dir_path = os.path.join(sentence_path, new_frame_dir_name)
                    os.rename(old_frame_dir_path, new_frame_dir_path)

print("폴더 이름 변경이 완료되었습니다.")
