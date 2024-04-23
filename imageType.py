import os
from PIL import Image

# تابعی برای تشخیص نوع تصاویر
def detect_image_types(data_dir):
    image_types = {}
    supported_formats = ['jpg', 'jpeg', 'png', 'bmp', 'gif', 'tiff', 'webp']  # فرمت‌های تصویری که مورد بررسی قرار می‌گیرند

    # عبور از تمام فایل‌های موجود در دایرکتوری
    for root, dirs, files in os.walk(data_dir):
        for filename in files:
            # تشخیص فرمت فایل
            file_ext = filename.split('.')[-1].lower()
            if file_ext in supported_formats:
                file_path = os.path.join(root, filename)
                try:
                    # باز کردن تصویر
                    with Image.open(file_path) as img:
                        # دریافت تعداد کانال‌ها
                        num_channels = len(img.getbands())
                        # تعیین نوع تصویر
                        if num_channels == 1:
                            image_type = 'grayscale'
                        elif num_channels == 3:
                            image_type = 'RGB'
                        elif num_channels == 4:
                            image_type = 'RGBA'
                        else:
                            image_type = f'Unknown ({num_channels} channels)'
                        
                        # ذخیره نوع تصویر در دیکشنری
                        if image_type in image_types:
                            image_types[image_type] += 1
                        else:
                            image_types[image_type] = 1
                except Exception as e:
                    print(f"Error processing {filename}: {e}")

    return image_types

# استفاده از تابع برای دریافت نوع تصاویر
data_directory = r"C:\Users\negin\Desktop\vea\data\healthy_lungs"  # آدرس دایرکتوری داده‌های خود را قرار دهید
image_types = detect_image_types(data_directory)

# نمایش نوع و تعداد تصاویر
print("Types of images found:")
for image_type, count in image_types.items():
    print(f"{image_type}: {count} تصاویر")
