import cv2
import os

def create_images_folder():
    folder_name = "CameraCalibration/images"
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
        print(f"Folder '{folder_name}' created successfully.")
    else:
        print(f"Folder '{folder_name}' already exists.")


def capture_calib_data():

    create_images_folder()
    cap = cv2.VideoCapture(1)
    num = 0
    while cap.isOpened():
        succes, img = cap.read()
        k = cv2.waitKey(5)
        if k == 27:
            break
        elif k == ord('s'): # wait for 's' key to save and exit
            cv2.imwrite('CameraCalibration/images/img' + str(num) + '.png', img)
            print("image saved!")
            num += 1
        cv2.imshow('Img',img)
    # Release and destroy all windows before termination
    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    capture_calib_data()