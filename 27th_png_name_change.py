import os

def rename_files(root_dir):
    for root, dirs, files in os.walk(root_dir):
        for directory in dirs:
            if directory.startswith("Sentence"):
                sentence_dir = os.path.join(root, directory)
                rename_files_in_sentence(sentence_dir)

def rename_files_in_sentence(sentence_dir):
    for frame_dir in find_frame_dirs(sentence_dir):
        rename_files_in_frame(frame_dir)

def find_frame_dirs(sentence_dir):
    frame_dirs = [os.path.join(sentence_dir, directory) for directory in os.listdir(sentence_dir) if directory.startswith("Frame")]
    return frame_dirs

def rename_files_in_frame(frame_dir):
    frame_number = os.path.basename(frame_dir).lstrip('Frame')
    
    for root, _, files in os.walk(frame_dir):
        for file in files:
            old_path = os.path.join(root, file)

            # Constructing the new file name
            new_file_name = f'M01_S0201_C27_F{int(frame_number):03d}.png'
            new_path = os.path.join(root, new_file_name)

            # Renaming the file
            os.rename(old_path, new_path)

if __name__ == "__main__":
    root_directory = r'F:\\vtoi3_F\\231204\\Model11\\2D_images'
    rename_files(root_directory)
