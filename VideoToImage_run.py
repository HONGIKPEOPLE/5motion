import subprocess

scripts_to_run = ["VideoToImage_1.py", "VideoToImage_2.py"]

processes = []

for script in scripts_to_run:
    process = subprocess.Popen(["python", script])
    processes.append(process)

# 모든 스크립트 실행이 완료될 때까지 대기
for process in processes:
    process.wait()

print("모든 스크립트 실행이 완료되었습니다.")
