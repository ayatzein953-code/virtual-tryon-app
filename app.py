import os
import streamlit as st
from core_logic import process_virtual_tryon

# --- إعدادات الصفحة ---
st.set_page_config(page_title="AI Virtual Try-On", layout="centered")

st.title("👗 أداة القياس الافتراضي الذكية")
st.write("قومي بررفع صورة الشخص وصورة الملابس المطلوبة، وسيتولى الذكاء الاصطناعي معالجتها بدقة!")

# --- واجهة رفع الصور ---
col1, col2 = st.columns(2)
with col1:
    person_file = st.file_uploader("1️⃣ صورة الشخص (Person):", type=['jpg', 'jpeg', 'png'])
with col2:
    garment_file = st.file_uploader("2️⃣ صورة الملابس (Garment):", type=['jpg', 'jpeg', 'png'])

# --- زر التنفيذ ---
if st.button("🚀 ابدأ تجربة الملابس", type="primary"):
    if person_file is not None and garment_file is not None:
        
        # حفظ الملفات المرفوعة مؤقتاً
        person_path = f"temp_p_{person_file.name}"
        garment_path = f"temp_g_{garment_file.name}"
        
        with open(person_path, "wb") as f:
            f.write(person_file.getbuffer())
        with open(garment_path, "wb") as f:
            f.write(garment_file.getbuffer())
            
        # استدعاء دالة المعالجة من ملف core_logic.py مع مؤشر انتظار
        with st.spinner("⏳ جاري المعالجة وقياس الملابس بواسطة الذكاء الاصطناعي..."):
            final_image_path = process_virtual_tryon(person_path, garment_path)
            
            if final_image_path:
                st.success("✨ تمت العملية بنجاح!")
                st.image(final_image_path, caption="النتيجة النهائية للتجربة", use_container_width=True)
                
                # زر تنزيل الصورة الناتجة
                with open(final_image_path, "rb") as file:
                    st.download_button(
                        label="📥 تحميل الصورة الناتجة",
                        data=file,
                        file_name="virtual_tryon_result.jpg",
                        mime="image/jpeg"
                    )
            else:
                st.error("❌ حدث خطأ أثناء المعالجة، يرجى المحاولة مرة أخرى.")
        
        # تنظيف الملفات المؤقتة من الجهاز
        for p in [person_path, garment_path]:
            if os.path.exists(p):
                os.remove(p)
                
    else:
        st.warning("⚠️ الرجاء رفع صورتي الشخص والملابس أولاً.")
