import os
import sys
import zipfile as zf
import sort_main

def get_zip_info(directory_path):
    # 결과를 담을 사전
    zip_info = {}

    # 현재 디렉토리에서 파일 목록을 가져옴
    files_in_directory = os.listdir(directory_path)

    # 현재 디렉토리의 파일 중에서 확장자가 .zip인 것을 찾음
    zip_files = [file for file in files_in_directory if file.endswith('.zip')]
    
    # 만약 zip 파일이 없으면 종료
    if not zip_files:
        print("디렉토리에 zip 파일이 없습니다.")
        sort_main.wait_for_key()
        sys.exit()
    
    # 모든 zip 파일에 대해 반복
    for zip_file in zip_files:
        # zip 파일 경로
        zip_file_path = os.path.join(directory_path, zip_file)

        # zip 파일 열기
        with zf.ZipFile(zip_file_path, 'r') as zip_ref:
            # zip 파일 내부의 파일 목록 가져오기
            file_list = zip_ref.namelist()

            # print for debug
            # print("파일 '{}'의 개수: {}".format(zip_file, len(file_list)))

            # 사전에 파일 경로와 파일 개수 추가
            zip_info[zip_file] = {
                'path': zip_file_path,
                'file_count': len(file_list)
            }

    return zip_info
