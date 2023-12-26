import os

current_dir = os.path.dirname(os.path.abspath(__file__))
image_root_dir = os.path.join(current_dir, "..", "..", "2D_images")

# 원하는 Sentence번호를 range에 입력하면 되는데, ex) 51번부터 100번이라고 하면 두번째 인자는 반드시 101로 쓰세요! range(51,101)
for i in range(201, 206):
    folder_name = f'Sentence{i:03d}'
    folder_path = os.path.join(image_root_dir, folder_name)
    
    # 이미 폴더가 존재하는 경우, 무시하고 계속 진행합니다.
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

print("폴더 생성이 완료되었습니다.")
