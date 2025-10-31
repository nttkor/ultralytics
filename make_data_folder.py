# DTV
# nttkor
# 온라인

# 김경탁_클래스룸2 — 오후 5:06
# 안녕하세요
import pandas as pd
from PIL import Image
import numpy as np
import os

def create_labeled_dataset_from_csv_revised(csv_file_path, output_base_dir="DATASET", image_size=(32, 32)):
    """
    ID, 라벨, 픽셀 데이터 순서의 CSV 파일을 읽어, 라벨별로 폴더링하여 JPG 파일을 생성합니다.
    (가정: 0번째 열=ID, 1번째 열=Label, 2번째 열부터 픽셀 데이터 1024개)

    Args:
        csv_file_path (str): ID, 라벨, 픽셀 데이터가 포함된 CSV 파일 경로.
        output_base_dir (str): 모든 라벨 폴더를 포함할 최상위 디렉토리 이름.
        image_size (tuple): 이미지의 가로 및 세로 크기 (기본값: (32, 32)).
    
    Returns:
        str: 작업 결과 요약 메시지.
    """
    print(f"--- 데이터셋 생성 시작: {csv_file_path} ---")
    
    # 1. CSV 파일 로드
    try:
        df = pd.read_csv(csv_file_path)
    except Exception as e:
        return f"오류: CSV 파일 로드 중 문제가 발생했습니다: {e}"

    # 2. 필수 데이터 범위 지정 및 추출
    # 가정: ID(0번째), Label(1번째), 픽셀 1024개(2번째~1025번째)
    
    expected_pixels = image_size[0] * image_size[1]
    
    # 데이터프레임 전체 컬럼 개수 확인 (ID 1개 + Label 1개 + 픽셀 1024개 = 1026개)
    if df.shape[1] != 1 + 1 + expected_pixels:
        return f"오류: 컬럼 개수({df.shape[1]})가 ID+Label+픽셀({1 + 1 + expected_pixels}개)과 일치하지 않습니다."

    # ID 컬럼을 제외하고, 1번째 열을 라벨, 2번째 열부터를 픽셀 데이터로 지정
    # .iloc[:, 1] -> 1번째 컬럼 (Label)
    # .iloc[:, 2:] -> 2번째 컬럼부터 끝까지 (Pixel Data 1024개)
    labels = df.iloc[:, 1]
    pixel_data_df = df.iloc[:, 2:]
        
    # 3. 최상위 출력 디렉토리 생성
    os.makedirs(output_base_dir, exist_ok=True)
    print(f"최상위 디렉토리 생성: {output_base_dir}")

    total_images_saved = 0
    
    # 4. 데이터프레임을 행별로 순회하며 이미지 생성
    for index in range(len(df)):
        label = str(labels[index])
        
        # 라벨별 서브 디렉토리 생성
        label_dir = os.path.join(output_base_dir, label)
        os.makedirs(label_dir, exist_ok=True)
        
        # 픽셀 데이터 추출 및 배열 변환
        pixel_data = pixel_data_df.iloc[index].values
        
        # NumPy 배열로 변환 및 이미지 크기로 재구성 (그레이스케일 가정)
        try:
            data_array = np.array(pixel_data, dtype=np.uint8).reshape(image_size[1], image_size[0])
            
            # PIL Image 객체 생성 ('L'은 8비트 그레이스케일)
            image = Image.fromarray(data_array, mode='L')
            
            # 파일 이름 설정 (고유 ID 또는 인덱스를 사용)
            # 파일 이름에 라벨과 행 인덱스(순서) 사용
            output_path = os.path.join(label_dir, f"{label}_{index+1}.jpg")
            
            # JPG 파일로 저장
            image.save(output_path, format='JPEG', quality=90)
            total_images_saved += 1
            
        except Exception as e:
            print(f"경고: {index}번 인덱스 이미지 생성/저장 중 오류 발생 (라벨: {label}) - {e}")
            continue

    print(f"--- 데이터셋 생성 완료: 총 {total_images_saved}개의 이미지 저장 ---")
    return f"데이터셋이 '{os.path.abspath(output_base_dir)}' 경로에 성공적으로 생성되었습니다."

# --- 실행 예시 ---

# CSV 파일 경로를 지정해 주세요.
csv_path = 'train.csv' 
result_message = create_labeled_dataset_from_csv_revised(csv_path, output_base_dir="DATASET", image_size=(32, 32))
# 접기
# 이미지.txt
# 4KB
# 이미지
# 요거는 그냥 데이터셋입니다
# 첨부 파일 형식: archive
# DATASET.zip
# 1.76 KB
# 혹시 저 코드 실행 안돼시거나 하면 고냥 요 파일 쓰시면 될거에요
# ﻿
# 김경탁_클래스룸2
# gimgyeongtag_25324