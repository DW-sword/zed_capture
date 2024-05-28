import pyzed.sl as sl
import cv2 as cv
import numpy as np
import time 

def main(cnt_max):
    zed = sl.Camera()
    init_params = sl.InitParameters()
    '''
    调整分辨率,VGA:(376,672) HD720:(720,1280) HD1080:(1080,1920) HD2K:(1242,2208)
    帧率,VGA:100 HD720:60 HD1080:30 HD2K:15
    '''
    init_params.camera_resolution = sl.RESOLUTION.VGA
    init_params.camera_fps = 30
    init_params.camera_image_flip = sl.FLIP_MODE.OFF
    runtime_parameters = sl.RuntimeParameters()
    err = zed.open(init_params)
    if err != sl.ERROR_CODE.SUCCESS:
        exit(-1)
    cnt = 0
    while True:
        img = sl.Mat()
        if zed.grab(runtime_parameters) == sl.ERROR_CODE.SUCCESS:
            zed.retrieve_image(img,sl.VIEW.RIGHT)
            img_rgb = img.get_data()[:,:,:-1]
            cv.imshow('img',img_rgb)
            time.sleep(0.1)
            # 保存路径
            folder_name = 5
            cv.imwrite('/home/lvpin/Desktop/get_zed_photos_svo/{}/{}_{}.png'.format(folder_name,folder_name,cnt),img_rgb)
            cnt += 1
            print(cnt)
            if cnt >= cnt_max:
                break
            if cv.waitKey(1) == ord('q'):
                break
    zed.close()

if __name__ == "__main__":
    # 设定最大拍摄图片数量
    cnt_max = 1000000000
    main(cnt_max)
    