import cv2
import numpy as np
from color_utils import rgb_to_lab, find_closest_color
from roi_utils import extract_roi

# 加载图片
def load_image(path):
    image = cv2.imread(path)
    if image is None:
        raise ValueError(f"无法加载图像：{path}")
    return image

# 主流程
def main(image_path):
    image = load_image(image_path)

    # 提取 ROI（你可以手动选或自动选）
    roi = extract_roi(image)

    # 计算 ROI 区域的平均颜色
    avg_color = np.mean(roi.reshape(-1, 3), axis=0)
    avg_rgb = tuple(map(int, avg_color))
    print("提取的平均 RGB 值：", avg_rgb)

    # 转换为 LAB 并比对色卡
    avg_lab = rgb_to_lab(avg_rgb)
    label, delta_e = find_closest_color(avg_lab)

    print(f"匹配结果：{label}（ΔE={delta_e:.2f}）")

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("请提供图片路径，如：python main.py data/strip.jpg")
    else:
        main(sys.argv[1])
