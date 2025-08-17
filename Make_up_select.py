import cv2
import dlib
from imutils import face_utils
import os
import numpy as np
# print(np.__version__)
# detector = dlib.get_frontal_face_detector()
# predictor = dlib.shape_predictor("D:\shape_predictor_68_face_landmarks.dat")
# for folder, lab in [("D:\download\Make_up_Dataset\Style\Japanese",0), ("D:\download\Make_up_Dataset\Style\Korean",1),
#                     ("D:\download\Make_up_Dataset\Style\Weatern",2)]:
    
#     # [("D:\\download\\Block_Dataset_Shape\\new_Circle",0), ("D:\\download\\Block_Dataset_Shape\\new_Square",1),
#     #                 ("D:\\download\\Block_Dataset_Shape\\new_Triangle",2)]
#     # [("D:\download\Make_up_Dataset\Style\Japanese",0), ("D:\download\Make_up_Dataset\Style\Korean",1),
#     #                 ("D:\download\Make_up_Dataset\Style\Weatern",2)]
    
#     print('lab', lab)
#     for fn in os.listdir(folder):
#         # capture=cv2.VideoCapture(0)
#         # img=cv2.imread("D:\\download\\Block_Dataset_Shape\\Circle\\1.bmp",1)
#         img = cv2.imread(os.path.join(folder,fn))
#         img = cv2.resize(img, (256, 256))
        
#         gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#         # detect face
#         rects = detector(gray, 1)
#         for rect in rects:
#             shape = predictor(gray, rect)
#             coords = face_utils.shape_to_np(shape)  # (68, 2)

#             mouth = coords[48:68]  # Python slice
#             cx_m = int(mouth[:, 0].mean())
#             cy_m = int(mouth[:, 1].mean())
#             print("mouse center:", (cx_m, cy_m))
            
#             left_eye = coords[36:42]
#             cx_le = int(left_eye[:, 0].mean())
#             cy_le = int(left_eye[:, 1].mean())
#             print("left_eye:", (cx_le, cy_le))

#             right_eye = coords[42:48]
#             cx_re = int(right_eye[:, 0].mean())
#             cy_re = int(right_eye[:, 1].mean())
#             print("right_eye:", (cx_re, cy_re))

#             nose = coords[27:36]
#             cx_n = int(nose[:, 0].mean())
#             cy_n = int(nose[:, 1].mean())
#             print("nose:", (cx_n, cy_n))
            
#             # 擷取 mouth
#             # cv2.circle(img, (cx_m, cy_m), 5, (0, 0, 255), -1)
            
#             # cv2.circle(img, (cx_m, cy_m), 80, (0, 0, 255), 0)
            
#             # ptCenter = (160, 160) # center
#             # axesSize = (180, 90) # 長軸半徑, 短轴半徑 
#             # rotateAngle = 0 # 旋轉角度
#             # startAngle = 0
#             # endAngle = 360

#             # point_color = (0, 0, 255) # BGR
#             # thickness = 1 
#             # lineType = 4
#             # cv2.ellipse(img, (cx_m, cy_m), (180, 90), 0, 0, 360, (0,0,255), 0)
            
#             mask = np.zeros(img.shape[:2], dtype=np.uint8)  # mask
#             cv2.ellipse(mask, (cx_m, cy_m), (45, 22), 0, 0, 360, 255, -1)  # 填充區域

#             # 使用 mask 進行位運算，提取區域內圖像
#             masked = cv2.bitwise_and(img, img, mask=mask)

#             # 裁切
#             ys, xs = np.where(mask == 255)
#             # print(ys)
#             # print(xs)
#             y0, y1 = ys.min(), ys.max()
#             x0, x1 = xs.min(), xs.max()
#             cropped = masked[y0:y1 + 1, x0:x1 + 1]
#             cv2.imshow("Result", cropped)
#             cv2.waitKey(0)
            
#             # 擷取 left eye
#             # cv2.circle(img, (cx_le, cy_le), 5, (0, 0, 255), -1)
#             # cv2.circle(img, (cx_le, cy_le), 120, (0, 0, 255), 0)
            
#             mask2 = np.zeros(img.shape[:2], dtype=np.uint8)  # mask
#             cv2.circle(mask2, (cx_le, cy_le), 40, 255, -1)  # 填充區域

#             # 使用 mask 進行位運算，提取區域內圖像
#             masked2 = cv2.bitwise_and(img, img, mask=mask2)

#             # 裁切
#             ys, xs = np.where(mask2 == 255)
#             # print(ys)
#             # print(xs)
#             y0, y1 = ys.min(), ys.max()
#             x0, x1 = xs.min(), xs.max()
#             cropped = masked2[y0:y1 + 1, x0:x1 + 1]
#             cv2.imshow("Result", cropped)
#             cv2.waitKey(0)
            
#             # 擷取 right eye
#             # cv2.circle(img, (cx_re, cy_re), 5, (0, 0, 255), -1)
#             # cv2.circle(img, (cx_re, cy_re), 120, (0, 0, 255), 0)
            
#             mask3 = np.zeros(img.shape[:2], dtype=np.uint8)  # mask
#             cv2.circle(mask3, (cx_re, cy_re), 40, 255, -1)  # 填充區域

#             # 使用 mask 進行位運算，提取區域內圖像
#             masked3 = cv2.bitwise_and(img, img, mask=mask3)

#             # 裁切
#             ys, xs = np.where(mask3 == 255)
#             y0, y1 = ys.min(), ys.max()
#             x0, x1 = xs.min(), xs.max()
#             cropped = masked3[y0:y1 + 1, x0:x1 + 1]
#             cv2.imshow("Result", cropped)
#             cv2.waitKey(0)
            
#             # 擷取 nose
#             # cv2.circle(img, (cx_n, cy_n), 5, (0, 0, 255), -1)
#             # cv2.circle(img, (cx_n, cy_n), 100, (0, 0, 255), 0)
#             # cv2.ellipse(img, (cx_n, cy_n - 50), (150, 85), 90, 0, 360, (0,0,255), 0)
            
#             mask4 = np.zeros(img.shape[:2], dtype=np.uint8)  # mask
#             cv2.ellipse(mask4, (cx_n, cy_n - 20), (50, 30), 90, 0, 360, 255, -1)  # 填充區域

#             # 使用 mask 進行位運算，提取區域內圖像
#             masked4 = cv2.bitwise_and(img, img, mask=mask4)

#             # 裁切
#             ys, xs = np.where(mask4 == 255)
#             y0, y1 = ys.min(), ys.max()
#             x0, x1 = xs.min(), xs.max()
#             cropped = masked4[y0:y1 + 1, x0:x1 + 1]
#             cv2.imshow("Result", cropped)
#             cv2.waitKey(0)
            
#             # cv2.imshow("Result", img)
#             # cv2.waitKey(0)
            
#             # 擷取 顴骨
#             mask4 = np.zeros(img.shape[:2], dtype=np.uint8)  # mask
#             cv2.ellipse(mask4, (cx_n - 50, cy_n), (50, 30), 90, 0, 360, 255, -1)  # 填充區域
#             cv2.ellipse(mask4, (cx_n + 50, cy_n), (50, 30), 90, 0, 360, 255, -1)  # 填充區域

#             # 使用 mask 進行位運算，提取區域內圖像
#             masked4 = cv2.bitwise_and(img, img, mask=mask4)

#             # 裁切
#             ys, xs = np.where(mask4 == 255)
#             y0, y1 = ys.min(), ys.max()
#             x0, x1 = xs.min(), xs.max()
#             cropped = masked4[y0:y1 + 1, x0:x1 + 1]
#             cv2.imshow("Result", cropped)
#             cv2.waitKey(0)
            
#             cv2.imshow("Result", img)
#             cv2.waitKey(0)
        
#         # print(img.shape)
#         # cv2.imshow('image',img)
#         # cv2.waitKey(0)
        
#         # # img = cv2.resize(img, (320, 320))
#         # # cv2.line(img,(100 // 2, 150 // 2),(250 // 2, 250 // 2),color=(255,0,0),thickness=5)
#         # # cv2.line(img,(300 // 2, 150 // 2),(450 // 2, 250 // 2),color=(255,0,0),thickness=5)
#         # # cv2.line(img,(190 // 2, 350 // 2),(400 // 2, 470 // 2),color=(255,0,0),thickness=5)
#         # # # 从（0，0）-》（100，100）颜色（BGR 255 是蓝）宽度是5
#         # # cv2.imshow('image',img)
#         # # cv2.waitKey(0)
        
#         # gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#         # _, m = cv2.threshold(gray, 130, 255, cv2.THRESH_BINARY)
#         # cv2.imshow('image',m)
#         # cv2.waitKey(0)
        
        
        
#         # element1 = cv2.getStructuringElement(cv2.MORPH_RECT,(3,3),(-1,-1))
#         # tmp = cv2.morphologyEx(m,cv2.MORPH_CLOSE,element1,None,(-1,-1),1)
#         # cv2.imshow('image',tmp)
#         # cv2.waitKey(0)
        
#         # cnts, _ = cv2.findContours(m, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

#         # if cnts:
#         #     # 取得面積最大的輪廓
#         #     largest = max(cnts, key=cv2.contourArea)
#         #     M = cv2.moments(largest)
#         #     if M["m00"] != 0:
#         #         cx = int(M["m10"] / M["m00"])
#         #         cy = int(M["m01"] / M["m00"])
#         #         print("最大黑色區塊的中心座標：", (cx, cy))

#         #         # 標示中心點與輪廓
#         #         cv2.drawContours(img, [largest], -1, (0, 255, 0), 2)
#         #         cv2.circle(img, (cx, cy), 5, (0, 0, 255), -1)
#         #         cv2.imshow("Center", img)
#         #         cv2.waitKey(0)
#         #     else:
#         #         print("最大區塊太小，無法計算質心")
#         # else:
#         #     print("找不到任何黑色區塊")
        
        
#         # # contours, _ = cv2.findContours(tmp, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
#         # # centers = []
#         # # for cnt in contours:
#         # #     M = cv2.moments(cnt)
#         # #     if M["m00"] != 0:
#         # #         cx = int(M["m10"] / M["m00"])
#         # #         cy = int(M["m01"] / M["m00"])
#         # #         centers.append((cx, cy))
#         # #         cv2.circle(img, (cx, cy), 5, (0, 0, 255), -1)  # 畫上質心點
#         # # print("Center coordinates:", centers)
#         # # cv2.imshow("centers", img)
#         # # cv2.waitKey(0)
        
        
#         # # element2 = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(16,16),(-1,-1))
#         # # dst = cv2.morphologyEx(tmp,cv2.MORPH_OPEN,element2)
#         # # cv2.imshow('image',dst)
#         # # cv2.waitKey(0)
        
#         # # cnts,_ = cv2.findContours(m, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
#         # # # print(cnts)
#         # # print('cnt', len(cnts))

#         # # area_list = []
#         # # for c in cnts:
#         # #     area = cv2.contourArea(c)
#         # #     area_list.append(area)
#         # # index_list = np.argmax(area_list)
#         # # print(area_list)
#         # # print(index_list)
        
#         # # m = m / 255.0
#         # # print(m.shape)
#         # # cv2.imshow('image',m)
#         # # cv2.waitKey(0)

import dlib
import cv2
from imutils import face_utils
import numpy as np
from skimage.feature import hog, local_binary_pattern
from skimage import filters
from scipy.stats import skew
import pickle
import gzip
from xgboost import XGBClassifier
from shutil import copy

xgboostModel = XGBClassifier(learning_rate = 0.1,
                      n_estimators = 100,
                      max_depth = 3,
                      min_child_weight = 1,
                      gamma = 0,
                      subsample = 1,
                      colsample_bytree = 1,
                      scale_pos_weight = 1,
                      random_state = 27,
                      verbosity = 0,
                      booster = 'gbtree',
                      n_jobs = 1,
                      max_delta_step = 0,
                      colsample_bylevel = 1,
                      colsample_bynode = 1,
                      base_score = 0.5)

def extract_gabor_feats(gray, freqs=[0.1,0.3], thetas=[0, np.pi/4, np.pi/2]):
    feats = []
    for frequency in freqs:
        for theta in thetas:
            real, imag = filters.gabor(gray, frequency=frequency, theta=theta)
            feats.append(real.mean())
            feats.append(real.var())
            feats.append(imag.mean())
            feats.append(imag.var())
    return np.array(feats)  # shape = len(freqs)*len(thetas)*4

def extract_features(img):
    # 1. HOG 分析輪廓之特徵向量
    img = cv2.resize(img, (128, 128))
    # img_array = img.astype('float32') / 255.0
    # # batch 维度
    # img_batch = np.expand_dims(img_array, axis=0)

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    hog_feat = hog(gray,
                   orientations=6, pixels_per_cell=(16, 16),
                   cells_per_block=(1,1), block_norm='L2-Hys')
    # print('hog', hog_feat)
    # 2. LBP 分析表面紋理
    P = 8
    lbp = local_binary_pattern(cv2.cvtColor(img, cv2.COLOR_BGR2GRAY),
                               P=P, R=1, method='uniform')
    (hist, _) = np.histogram(lbp.ravel(),
                             bins=np.arange(0, P + 3),
                             range=(0, P + 2))
    hist = hist.astype("float")
    hist /= hist.sum()
    # print('lbp', lbp)
    # 3. 色彩矩（HSV）
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    moments = []
    for ch in cv2.split(hsv):
        moments += [np.mean(ch), np.std(ch), skew(ch.flatten())]
    # print('moments', moments)
    real, imag = filters.gabor(gray, frequency=0.6, theta=np.pi / 4)

    feat = np.hstack([hog_feat, hist, moments, real.mean(),
                      ]) # hist_lip.flatten().tolist(), hist_eye.flatten().tolist(), cnn_feats
    print(feat.shape)
    return feat

# initialize
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("D:\shape_predictor_68_face_landmarks.dat")

img = cv2.imread("D:\download\Make_up_Dataset\Style\Korean\888.jpg")
feature = extract_features(img)
features = []
features.append(feature)

style = ""
with gzip.open("D:\\pythonProject\\xgboost_makeup", 'r') as f:
    xgboostModel = pickle.load(f)
    pred = xgboostModel.predict(np.array(features))
    # print(pred)
    # print(type(pred))
    if pred == [0]:
        print(pred)
        style = "Japanese"
        print(style)
        
        file_path = r"D:\download\Make_up_Dataset\Before_Teaching\Japanese"
        save_dir = r"D:\download\Make_up_Dataset\Teaching"
        # dir_name = "newFile"
        
        pathDir = os.listdir(file_path)
        for filename in pathDir:
            print(filename)
            filename_in = os.listdir(os.path.join(file_path, filename))
            print(filename_in)
            for filenames in filename_in:
                print(filenames)
                from_path = os.path.join(file_path, filename, filenames)
                to_path =os.path.join(save_dir, filename, filenames)
            
                # if not os.path.isdir(to_path):
                #     os.makedirs(to_path)
                copy(from_path, to_path)
        print("Transfer Finished")
        
    elif pred == [1]:
        print(pred)
        style = "Korean"
        print(style)
        
        file_path = r"D:\download\Make_up_Dataset\Before_Teaching\Korean"
        save_dir = r"D:\download\Make_up_Dataset\Teaching"
        # dir_name = "newFile"
        
        pathDir = os.listdir(file_path)
        for filename in pathDir:
            print(filename)
            filename_in = os.listdir(os.path.join(file_path, filename))
            print(filename_in)
            for filenames in filename_in:
                print(filenames)
                from_path = os.path.join(file_path, filename, filenames)
                to_path =os.path.join(save_dir, filename, filenames)
            
                # if not os.path.isdir(to_path):
                #     os.makedirs(to_path)
                copy(from_path, to_path)
        print("Transfer Finished")
        
    elif pred == [2]:
        print(pred)
        style = "Weatern"
        print(style)
        
        file_path = r"D:\download\Make_up_Dataset\Before_Teaching\Weatern"
        save_dir = r"D:\download\Make_up_Dataset\Teaching"
        # dir_name = "newFile"
        
        pathDir = os.listdir(file_path)
        for filename in pathDir:
            print(filename)
            filename_in = os.listdir(os.path.join(file_path, filename))
            print(filename_in)
            for filenames in filename_in:
                print(filenames)
                from_path = os.path.join(file_path, filename, filenames)
                to_path =os.path.join(save_dir, filename, filenames)
            
                # if not os.path.isdir(to_path):
                #     os.makedirs(to_path)
                copy(from_path, to_path)
        print("Transfer Finished")

    
img = cv2.resize(img, (256, 256))
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# detect face
rects = detector(gray, 1)
for rect in rects:
    shape = predictor(gray, rect)
    coords = face_utils.shape_to_np(shape)  # (68, 2)

    mouth = coords[48:68]  # Python slice
    cx_m = int(mouth[:, 0].mean())
    cy_m = int(mouth[:, 1].mean())
    print("mouse center:", (cx_m, cy_m))
    
    left_eye = coords[36:42]
    cx_le = int(left_eye[:, 0].mean())
    cy_le = int(left_eye[:, 1].mean())
    print("left_eye:", (cx_le, cy_le))

    right_eye = coords[42:48]
    cx_re = int(right_eye[:, 0].mean())
    cy_re = int(right_eye[:, 1].mean())
    print("right_eye:", (cx_re, cy_re))

    nose = coords[27:36]
    cx_n = int(nose[:, 0].mean())
    cy_n = int(nose[:, 1].mean())
    print("nose:", (cx_n, cy_n))
    
    # 擷取 mouth
    # cv2.circle(img, (cx_m, cy_m), 5, (0, 0, 255), -1)

    # cv2.circle(img, (cx_m, cy_m), 80, (0, 0, 255), 0)

    # ptCenter = (160, 160) # center
    # axesSize = (180, 90) # 長軸半徑, 短轴半徑 
    # rotateAngle = 0 # 旋轉角度
    # startAngle = 0
    # endAngle = 360

    # point_color = (0, 0, 255) # BGR
    # thickness = 1 
    # lineType = 4
    # cv2.ellipse(img, (cx_m, cy_m), (180, 90), 0, 0, 360, (0,0,255), 0)

    mask = np.zeros(img.shape[:2], dtype=np.uint8)  # mask
    cv2.ellipse(mask, (cx_m, cy_m), (45, 22), 0, 0, 360, 255, -1)  # 填充區域

    # 使用 mask 進行位運算，提取區域內圖像
    masked = cv2.bitwise_and(img, img, mask=mask)

    # 裁切
    ys, xs = np.where(mask == 255)
    # print(ys)
    # print(xs)
    y0, y1 = ys.min(), ys.max()
    x0, x1 = xs.min(), xs.max()
    cropped = masked[y0:y1 + 1, x0:x1 + 1]
    
    img_path = "D:\download\Make_up_Dataset\Teaching\Mouth\mouth.jpg"
    cv2.imwrite(img_path, cropped)
    
    file_path = "D:\download\Make_up_Dataset\Teaching\Mouth"
    print(file_path)
    for file in os.listdir(file_path):
        if file.endswith(".txt"):
            print(file_path)
            print(file)
            files = os.path.join(file_path, file)
            with open(files, 'r', encoding='utf-8') as file:  # 'r'表示讀取模式，encoding='utf-8'處理中文
                content = file.read()
                print(content)
    
    cv2.imshow("Result", cropped)
    cv2.waitKey(0)

    # 擷取 eye
    # cv2.circle(img, (cx_le, cy_le), 5, (0, 0, 255), -1)
    # cv2.circle(img, (cx_le, cy_le), 120, (0, 0, 255), 0)

    mask2 = np.zeros(img.shape[:2], dtype=np.uint8)  # mask
    cv2.circle(mask2, (cx_le, cy_le), 40, 255, -1)# 填充區域
    cv2.circle(mask2, (cx_re, cy_re), 40, 255, -1)

    # 使用 mask 進行位運算，提取區域內圖像
    masked2 = cv2.bitwise_and(img, img, mask=mask2)

    # 裁切
    ys, xs = np.where(mask2 == 255)
    # print(ys)
    # print(xs)
    y0, y1 = ys.min(), ys.max()
    x0, x1 = xs.min(), xs.max()
    cropped = masked2[y0:y1 + 1, x0:x1 + 1]
    
    img_path = "D:\download\Make_up_Dataset\Teaching\Eye\eye.jpg"
    cv2.imwrite(img_path, cropped)
    
    file_path = "D:\download\Make_up_Dataset\Teaching\Eye"
    print(file_path)
    for file in os.listdir(file_path):
        if file.endswith(".txt"):
            print(file_path)
            print(file)
            files = os.path.join(file_path, file)
            with open(files, 'r', encoding='utf-8') as file:  # 'r'表示讀取模式，encoding='utf-8'處理中文
                content = file.read()
                print(content)
    
    cv2.imshow("Result", cropped)
    cv2.waitKey(0)

    # # 擷取 right eye
    # # cv2.circle(img, (cx_re, cy_re), 5, (0, 0, 255), -1)
    # # cv2.circle(img, (cx_re, cy_re), 120, (0, 0, 255), 0)

    # mask3 = np.zeros(img.shape[:2], dtype=np.uint8)  # mask
    # cv2.circle(mask3, (cx_re, cy_re), 40, 255, -1)  # 填充區域

    # # 使用 mask 進行位運算，提取區域內圖像
    # masked3 = cv2.bitwise_and(img, img, mask=mask3)

    # # 裁切
    # ys, xs = np.where(mask3 == 255)
    # y0, y1 = ys.min(), ys.max()
    # x0, x1 = xs.min(), xs.max()
    # cropped = masked3[y0:y1 + 1, x0:x1 + 1]
    # cv2.imshow("Result", cropped)
    # cv2.waitKey(0)

    # 擷取 nose + 顴骨
    # cv2.circle(img, (cx_n, cy_n), 5, (0, 0, 255), -1)
    # cv2.circle(img, (cx_n, cy_n), 100, (0, 0, 255), 0)
    # cv2.ellipse(img, (cx_n, cy_n - 50), (150, 85), 90, 0, 360, (0,0,255), 0)

    mask4 = np.zeros(img.shape[:2], dtype=np.uint8)  # mask
    cv2.ellipse(mask4, (cx_n, cy_n - 20), (50, 30), 90, 0, 360, 255, -1)  # 填充區域
    cv2.ellipse(mask4, (cx_n - 50, cy_n), (50, 30), 90, 0, 360, 255, -1)  # 填充區域
    cv2.ellipse(mask4, (cx_n + 50, cy_n), (50, 30), 90, 0, 360, 255, -1)  # 填充區域

    # 使用 mask 進行位運算，提取區域內圖像
    masked4 = cv2.bitwise_and(img, img, mask=mask4)

    # 裁切
    ys, xs = np.where(mask4 == 255)
    y0, y1 = ys.min(), ys.max()
    x0, x1 = xs.min(), xs.max()
    cropped = masked4[y0:y1 + 1, x0:x1 + 1]
    
    img_path = "D:\download\Make_up_Dataset\Teaching\Contour\contour.jpg"
    cv2.imwrite(img_path, cropped)
    
    file_path = "D:\download\Make_up_Dataset\Teaching\Contour"
    print(file_path)
    for file in os.listdir(file_path):
        if file.endswith(".txt"):
            print(file_path)
            print(file)
            files = os.path.join(file_path, file)
            with open(files, 'r', encoding='utf-8') as file:  # 'r'表示讀取模式，encoding='utf-8'處理中文
                content = file.read()
                print(content)
    
    cv2.imshow("Result", cropped)
    cv2.waitKey(0)
    
    # 擷取 臉頰
    mask5 = np.zeros(img.shape[:2], dtype=np.uint8)  # mask
    cv2.circle(mask5, (cx_n - 50, cy_n), 50, 255, -1)
    cv2.circle(mask5, (cx_n + 50, cy_n), 50, 255, -1)

    # 使用 mask 進行位運算，提取區域內圖像
    masked5 = cv2.bitwise_and(img, img, mask=mask5)

    # 裁切
    ys, xs = np.where(mask5 == 255)
    y0, y1 = ys.min(), ys.max()
    x0, x1 = xs.min(), xs.max()
    cropped = masked5[y0:y1 + 1, x0:x1 + 1]
    
    img_path = "D:\\download\\Make_up_Dataset\\Teaching\\Blush\\blush.jpg"
    cv2.imwrite(img_path, cropped)
    
    file_path = "D:\download\Make_up_Dataset\Teaching\Blush"
    print(file_path)
    for file in os.listdir(file_path):
        if file.endswith(".txt"):
            print(file_path)
            print(file)
            files = os.path.join(file_path, file)
            with open(files, 'r', encoding='utf-8') as file:  # 'r'表示讀取模式，encoding='utf-8'處理中文
                content = file.read()
                print(content)
    
    cv2.imshow("Result", cropped)
    cv2.waitKey(0)

    cv2.imshow("Result", img)
    cv2.waitKey(0)