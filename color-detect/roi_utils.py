def extract_roi(image, roi_size=50):
    h, w, _ = image.shape
    cx, cy = w // 2, h // 2
    half = roi_size // 2
    roi = image[cy - half:cy + half, cx - half:cx + half]
    return roi
