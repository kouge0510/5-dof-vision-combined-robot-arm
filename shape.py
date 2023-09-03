import cv2

def concat_and_count(set1, set2):
    # 将set2拼接到set1中
    set1.update(set2)
    # 求交集并返回
    return set1


def detect_and_draw_shapes(image, mask, color_value, color_name):
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    # 圆形检测部分很烂，选择更优策略，先执行圆形检测，再执行方形检测

    # circles = cv2.HoughCircles(mask, cv2.HOUGH_GRADIENT, dp=1.2, minDist=100, param1=50, param2=30, minRadius=100, maxRadius=1500)
    #
    # if circles is not None:
    #     circles = np.round(circles[0, :]).astype("int")
    #     for (x, y, r) in circles:
    #         perceived_width = r * 2
    #         distance = calculate_distance(KNOWN_WIDTH, FOCAL_LENGTH, perceived_width)
    #         cv2.circle(img, (x, y), r, color_value, 4)
    #         text = f"{color_name} Circle, Distance: {distance:.2f} m"
    #         cv2.putText(img, text, (x - r, y - r - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
    # 继续其他形状的检测，例如长方形和正方形
    for contour in contours:
        area = cv2.contourArea(contour)
        if area < 20000:
            continue

        epsilon = 0.04 * cv2.arcLength(contour, True)
        approx = cv2.approxPolyDP(contour, epsilon, True)

        shape_name = None
        if len(approx) == 4:
            x, y, w, h = cv2.boundingRect(approx)
            aspect_ratio = float(w) / h
            if 0.9 <= aspect_ratio <= 1.1:
                shape_name = "Square"
            else:
                shape_name = "Rectangle"

            if shape_name:
                cv2.drawContours(image, [approx], 0, color_value, 2)
                text = f"{color_name} {shape_name}"
                cv2.putText(image, text, (approx[0][0][0], approx[0][0][1] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5,
                            (255, 255, 255), 2)
                set_new=concat_and_count({color_name}, {shape_name})
                print(set_new)

    return image
