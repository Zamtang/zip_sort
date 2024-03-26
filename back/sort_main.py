import os
import get_zip_info as z_info

def sort_main():
    zip_info = z_info.get_zip_info('./test_file/')
    move_file(zip_info)

# move file 100 +-
def move_file(zip_info):
    # 파일을 이동할 폴더 이름 설정
    long_folder = 'long'
    short_folder = 'short'

    # 폴더 생성
    for folder in [long_folder, short_folder]:
        if not os.path.exists(folder):
            os.makedirs(folder)

    # zip_info 딕셔너리의 각 항목에 대해 파일 이동 작업 수행
    for zip_file, info in zip_info.items():
        file_count = info['file_count']
        source_path = info['path']
        
        if file_count >= 100:
            target_folder = long_folder
        elif file_count < 100:
            target_folder = short_folder
        
        # 파일 이동
        file_name = os.path.basename(source_path)
        target_path = os.path.join(target_folder, file_name)
        os.rename(source_path, target_path)

        print(f"'{zip_file}' 파일을 '{target_folder}' 폴더로 이동했습니다.")
