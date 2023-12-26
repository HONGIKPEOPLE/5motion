import os

def rename_audio_files(audio_root_dir):
    audio_files = [f for f in os.listdir(audio_root_dir) if f.endswith(".wav")]

    for audio_file in audio_files:
        # 파일 이름에서 S 뒤의 네 자리 숫자를 추출합니다.
        current_number = int(audio_file.split("_S")[1].split(".")[0])

        # 새로운 번호를 계산합니다.
        new_number = current_number + 500

        # 새로운 파일 이름을 생성합니다.
        new_name = f"M02_S{str(new_number).zfill(4)}.wav"   ## 수정사항
    

        old_path = os.path.join(audio_root_dir, audio_file)
        new_path = os.path.join(audio_root_dir, new_name)

        os.rename(old_path, new_path)

    print("Audio files renamed successfully.")

if __name__ == "__main__":
    audio_root_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)))
    rename_audio_files(audio_root_dir)
