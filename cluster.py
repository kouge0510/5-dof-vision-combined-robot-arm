import cv2
import numpy as np
import time
import shape as shape  # 形状检测
import zcode as zcode  # zcode检测

'''

以下内容为基本参数

'''

# 标定参数（需要根据实际相机进行标定）
FOCAL_LENGTH = 2.8  # 相机焦距（单位：像素）
KNOWN_WIDTH = 4.2  # 物体的已知宽度（单位：厘米）
blue_lower = np.array([175, 98, 26])  # 蓝色最低值範圍
blue_upper = np.array([244, 182, 112])  # 蓝色最高值範圍
yellow_lower = np.array([26, 120, 200])  # 黄色最低范围
yellow_upper = np.array([70, 248, 255])
red_lower = np.array([16, 10, 144])  # 红色最低范围
red_upper = np.array([90, 100, 255])


def calculate_distance(known_width, focal_length, percieved_width):
    return (known_width * focal_length) / percieved_width


# 主程序，负责调用函数，先执行灰度识别，减少误差，识别二维码，然后再识别形状，再识别颜色
# 蓝色球+黄色球为方案1，红色球+黄色球为方案2,目前均写为一种，最后再分割
def main():
    cap = cv2.VideoCapture(0)
    start_time = time.time()

    while True:
        ret, img = cap.read()
        elapsed_time = (time.time() - start_time) * 1000
        focal_length = FOCAL_LENGTH  # 焦距

        if elapsed_time <= 10000:  # 在10秒内进行颜色检测
            blue_output = cv2.inRange(img, blue_lower, blue_upper)
            kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (11, 11))
            blue_output = cv2.dilate(blue_output, kernel)
            blue_output = cv2.erode(blue_output, kernel)
            contours, hierarchy = cv2.findContours(blue_output, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            for contour in contours:
                area1 = cv2.contourArea(contour)
                blue = (255, 255, 0)
                # 蓝色矿圈定范围
                if area1 > 5000:
                    x, y, w, h = cv2.boundingRect(contour)
                    perceived_width = w

                    # 计算距离
                    distance = calculate_distance(KNOWN_WIDTH, focal_length, perceived_width)

                    # 在图像上绘制距离
                    cv2.putText(img, f"Distance: {distance:.2f} m", (x, y - 10),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
                    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

                    img = cv2.rectangle(img, (x, y), (x + w, y + h), blue, 3)
                    print(f"蓝球距离 {distance:.2f} m")
            # 上述为蓝色检测代码

            red_output = cv2.inRange(img, red_lower, red_upper)
            kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (11, 11))
            red_output = cv2.dilate(red_output, kernel)
            red_output = cv2.erode(red_output, kernel)
            contours, hierarchy = cv2.findContours(red_output, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            for contour in contours:
                area2 = cv2.contourArea(contour)
                red = (0, 0, 255)
                # 红色矿圈定范围
                if area2 > 5000:
                    x, y, w, h = cv2.boundingRect(contour)
                    perceived_width = w

                    # 计算距离
                    distance = calculate_distance(KNOWN_WIDTH, focal_length, perceived_width)

                    # 在图像上绘制距离
                    cv2.putText(img, f"Distance: {distance:.2f} m", (x, y - 10),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
                    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
                    img = cv2.rectangle(img, (x, y), (x + w, y + h), red, 3)
                    print(f"红球距离: {distance:.2f} m")
            # 上述为红色检测代码

            yellow_output = cv2.inRange(img, yellow_lower, yellow_upper)
            kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (11, 11))
            yellow_output = cv2.dilate(yellow_output, kernel)
            yellow_output = cv2.erode(yellow_output, kernel)
            contours, hierarchy = cv2.findContours(yellow_output, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            for contour in contours:
                area3 = cv2.contourArea(contour)
                yellow = (51, 222, 230)
                # 黄色矿圈定范围
                if area3 > 5000:
                    x, y, w, h = cv2.boundingRect(contour)
                    perceived_width = w

                    # 计算距离
                    distance = calculate_distance(KNOWN_WIDTH, focal_length, perceived_width)

                    # 在图像上绘制距离
                    cv2.putText(img, f"Distance: {distance:.2f} m", (x, y - 10),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
                    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
                    img = cv2.rectangle(img, (x, y), (x + w, y + h), yellow, 3)
                    print(f"黄球距离: {distance:.2f} m")
            # 上述为黄球检测代码

            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            decoded_img = zcode.decodeDisplay(gray)

            cv2.imshow('kouge love you', decoded_img)

        else:  # 10秒后开始形状识别
            blue_mask = cv2.inRange(img, blue_lower, blue_upper)
            img = shape.detect_and_draw_shapes(img, blue_mask, (255, 255, 0), "Blue")

            red_mask = cv2.inRange(img, red_lower, red_upper)
            img = shape.detect_and_draw_shapes(img, red_mask, (0, 0, 255), "Red")
            cv2.imshow('rectangle detecting', img)
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            decoded_img = zcode.decodeDisplay(gray)
            cv2.imshow('kouge love you', decoded_img)
        if cv2.waitKey(1) == ord('q'):  # 按Q跳出执行
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()  # 执行的为检测大类函数(包括形状，颜色，二维码)
