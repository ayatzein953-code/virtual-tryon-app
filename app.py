import streamlit as st
from PIL import Image
import os
from core_logic import process_virtual_tryon

st.set_page_config(page_title="AI Virtual Try-On", layout="wide")

st.title("👕 AI Virtual Try-On Studio")
st.write("ارفع صورة الشخص وصورة الملابس لرؤية التغيير الافتراضي باستخدام الذكاء الاصطناعي!")

col1, col2 = st.columns(2)

with col1:
    st.subheader("1. صورة الشخص")
    person_file = st.file_uploader("اختر صورة الشخص", type=["jpg", "jpeg", "png"], key="person")
    if person_file:
        st.image(person_file, caption="صورة الشخص المرفوعة", use_container_width=True)

with col2:
    st.subheader("2. صورة الملابس")
    garment_file = st.file_uploader("اختر صورة الملابس", type=["jpg", "jpeg", "png"], key="garment")
    if garment_file:
        st.image(garment_file, caption="صورة الملابس المرفوعة", use_container_width=True)

st.divider()

if st.button("✨ تطبيق الملابس الآن", type="primary"):
    if person_file and garment_file:
        with st.spinner("جاري معالجة وتطابق الملابس... قد يستغرق الأمر بضع لحظات."):
            # حفظ الصور مؤقتًا للتعامل معها
            person_path = "temp_person.jpg"
            garment_path = "temp_garment.jpg"
            
            with open(person_path, "wb") as f:
                f.write(person_file.getbuffer())
            with open(garment_path, "wb") as f:
                f.write(garment_file.getbuffer())
            
            # تشغيل نموذج الذكاء الاصطناعي
            result_path = process_virtual_tryon(person_path, garment_path, "final_result.jpg")
            
            if result_path and os.path.exists(result_path):
                st.success("✅ تم دمج الملابس بنجاح!")
                result_img = Image.open(result_path)
                st.image(result_img, caption="النتيجة النهائية", use_container_width=True)
            else:
                st.error("❌ حدث خطأ أثناء المعالجة أو أن السيرفر مشغول حالياً. يرجى المحاولة لاحقاً.")
    else:
        st.warning("⚠️ يرجى رفع الصورتين أولاً قبل البدء.")
