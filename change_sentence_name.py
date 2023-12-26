import os

# 경로 설정
base_path = r'\\mac\\MacOS_Shared_Folder\\03_VTOI\\Model6\\Videos'

# base_path에서 모든 폴더를 순회
for root, dirs, files in os.walk(base_path):
    for dir_name in dirs:
        if dir_name.startswith('Sentence'):
            # 'Sentence'로 시작하는 폴더 이름을 변경
            sentence_number = int(dir_name[8:])
            new_dir_name = f'Sentence{sentence_number}'
            old_dir_path = os.path.join(root, dir_name)
            new_dir_path = os.path.join(root, new_dir_name)

            # 폴더 이름 변경
            os.rename(old_dir_path, new_dir_path)

print("Sentence 폴더 이름 변경이 완료되었습니다.")
