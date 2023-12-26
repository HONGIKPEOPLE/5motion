import pandas as pd

# 원본 CSV 파일 읽기
original_file_path = 'Model5.csv'
df_original = pd.read_csv(original_file_path)

# 새로운 CSV 파일들 생성
output_folder = './output_csv_files/'
for i in range(len(df_original)):
    # 파일 이름 생성
    new_file_name = f'Sentence{i + 1:03d}_VTOI_frame.csv'
    
    # 새로운 데이터프레임 생성
    df_new = pd.DataFrame({
        'file_names': [new_file_name],
        ' start_frame': [df_original.loc[i, ' start_frame']],
        ' end_frame': [df_original.loc[i, ' end_frame']]
    })
    
    # 새로운 CSV 파일로 저장
    new_file_path = output_folder + new_file_name
    df_new.to_csv(new_file_path, index=False)

print("새로운 CSV 파일들이 생성되었습니다.")
