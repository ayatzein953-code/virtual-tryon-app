import os
from gradio_client import Client, handle_file
from PIL import Image
import uuid

def get_temp_path(ext="jpg"):
    """توليد مسار مؤقت فريد للصورة لمنع التداخل."""
    return f"temp_{uuid.uuid4()}.{ext}"

def process_virtual_tryon(person_img_path, garment_img_path, output_path="output.jpg"):
    """
    المنطق الأساسي: استقبال مسار الشخص والملابس واستدعاء نموذج Kolors (أو Leffa) لمعالجة الدمج.
    """
    try:
        # الاتصال بالنموذج (يمكنك استبداله برابط مساحتك الخاصة لاحقاً)
        client = Client("Kwai-Kolors/Kolors-Virtual-Try-On")
        
        result = client.predict(
            person_image=handle_file(person_img_path),
            garment_image=handle_file(garment_img_path),
            seed=42,
            api_name="/infer"
        )
        
        if result:
            output_filepath = result[0] if isinstance(result, (list, tuple)) else result
            output_image = Image.open(output_filepath)
            output_image.save(output_path)
            return output_path
            
        return None

    except Exception as e:
        print(f"Error in core logic: {e}")
        return None
