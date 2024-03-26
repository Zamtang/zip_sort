import os
import get_zip_info as z_info
import win_fun

def sort_main():
    try:
        folder_path = win_fun.select_folder()
        # 선택된 폴더의 경로를 사용하여 추가 작업을 수행할 수 있습니다.
        print("선택한 폴더 경로:", folder_path)
    except ValueError as e:
        print("에러 발생:", e)

    zip_info = z_info.get_zip_info(folder_path)
    move_file(zip_info, folder_path)

# move file 100 +-
def move_file(zip_info, sel_path):
    # 파일을 이동할 폴더 이름 설정
    long_folder = os.path.join(sel_path, 'long')
    short_folder = os.path.join(sel_path, 'short')

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

def wait_for_key():
    print("프로그램을 종료하려면 아무 키나 누르세요...")
    input()  # 사용자 입력 대기
    print("프로그램을 종료합니다.")