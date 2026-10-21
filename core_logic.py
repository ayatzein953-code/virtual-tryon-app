import os
from gradio_client import Client, handle_file
from PIL import Image

def process_virtual_tryon(person_img_path, garment_img_path, output_path="output.jpg"):
    """
    تستقبل مسار صورة الشخص وصورة الملابس وترسل الطلب إلى نموذج الذكاء الاصطناعي.
    """
    try:
        # الاتصال بالسيرفر/النموذج
        client = Client("yisol/IDM-VTON")
        
        # إرسال البيانات للنموذج
        result = client.predict(
            dict={"background": handle_file(person_img_path), "layers": [], "composite": None},
            garm_img=handle_file(garment_img_path),
            garment_des="A stylish outfit",
            is_checked=True,
            is_checked_crop=False,
            denoise_steps=30,
            seed=42,
            api_name="/tryon"
        )
        
        if result:
            output_filepath = result[0] if isinstance(result, (list, tuple)) else result
            output_image = Image.open(output_filepath)
            output_image.save(output_path)
            return output_path
        return None

    except Exception as e:
        print(f"Error during processing: {e}")
        return None
