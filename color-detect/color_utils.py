from colormath.color_objects import sRGBColor, LabColor
from colormath.color_conversions import convert_color
from colormath.color_diff import delta_e_cie2000

# 假设已有标准色卡（你之后可从 csv 加载）
COLOR_CARD = [
    {"label": "低", "lab": LabColor(75, 0, 20)},
    {"label": "中", "lab": LabColor(65, 5, 30)},
    {"label": "高", "lab": LabColor(55, 10, 40)},
]

def rgb_to_lab(rgb):
    srgb = sRGBColor(rgb[0], rgb[1], rgb[2], is_upscaled=True)
    return convert_color(srgb, LabColor)

def find_closest_color(sample_lab):
    min_delta = float('inf')
    closest_label = None
    for entry in COLOR_CARD:
        de = delta_e_cie2000(sample_lab, entry["lab"])
        if de < min_delta:
            min_delta = de
            closest_label = entry["label"]
    return closest_label, min_delta
