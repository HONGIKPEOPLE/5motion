import os
import pandas as pd

# 경로 설정
directory_path = r'\\mac\3D_Facial_Expression2\Videos\231205ver\Model10\Sentence_cam27'  # 수정1

# 시작 번호 설정
start_number = 4501  #수정2

# 모든 CSV 파일을 읽어서 처리
for filename in sorted(os.listdir(directory_path)):
    if filename.endswith('.csv'):
        csv_path = os.path.join(directory_path, filename)

        # CSV 파일 읽기
        df = pd.read_csv(csv_path)

        # 'file_names' 열의 값을 변경
        for i, row in df.iterrows():
            new_filename = f'M10_S{start_number:04d}_C26_10.mp4'  # 수정3
            df.at[i, 'file_names'] = new_filename
            start_number += 1

        # 변경된 DataFrame을 CSV 파일로 저장
        df.to_csv(csv_path, index=False)

print("파일 이름 변경이 완료되었습니다.")
