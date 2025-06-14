import streamlit as st
import datetime

# CSS Luxury Style
st.markdown("""
    <style>
    body {
        background-color: #1e1e2f;
        color: white;
    }
    h1, h2 {
        text-align: center;
        color: #f39c12;
        text-shadow: 0 0 10px #f39c12;
    }
    .box {
        background: rgba(44, 62, 80, 0.9);
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0 0 15px rgba(0,0,0,0.7);
        margin-bottom: 20px;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h1>🔮 Xem Bói Tình Duyên & Cung Hoàng Đạo</h1>", unsafe_allow_html=True)

# Nhập thông tin
with st.form("form_boi"):
    name = st.text_input("👤 Nhập tên của bạn")
    dob = st.date_input("📅 Ngày sinh", datetime.date(2000, 1, 1))
    submitted = st.form_submit_button("🔮 Xem ngay")

# Xác định cung hoàng đạo
def zodiac_sign(day, month):
    if (month == 12 and day >= 22) or (month == 1 and day <= 19):
        return "Ma Kết"
    elif (month == 1 and day >= 20) or (month == 2 and day <= 18):
        return "Bảo Bình"
    elif (month == 2 and day >= 19) or (month == 3 and day <= 20):
        return "Song Ngư"
    elif (month == 3 and day >= 21) or (month == 4 and day <= 19):
        return "Bạch Dương"
    elif (month == 4 and day >= 20) or (month == 5 and day <= 20):
        return "Kim Ngưu"
    elif (month == 5 and day >= 21) or (month == 6 and day <= 20):
        return "Song Tử"
    elif (month == 6 and day >= 21) or (month == 7 and day <= 22):
        return "Cự Giải"
    elif (month == 7 and day >= 23) or (month == 8 and day <= 22):
        return "Sư Tử"
    elif (month == 8 and day >= 23) or (month == 9 and day <= 22):
        return "Xử Nữ"
    elif (month == 9 and day >= 23) or (month == 10 and day <= 22):
        return "Thiên Bình"
    elif (month == 10 and day >= 23) or (month == 11 and day <= 21):
        return "Bọ Cạp"
    else:
        return "Nhân Mã"

if submitted:
    sign = zodiac_sign(dob.day, dob.month)
    st.success(f"💫 {name}, bạn thuộc cung **{sign}**!")

    # Hiển thị tình duyên mẫu
    st.markdown("<h2>❤️ Dự đoán tình duyên hôm nay</h2>", unsafe_allow_html=True)
    st.write(f"""
    **{sign}** hôm nay dễ gặp người khiến bạn rung động.  
    Đừng ngại mở lòng, chủ động nhắn tin cho người ấy nhé 😉  
    Hãy giữ tâm trạng vui vẻ và tự tin! ✨
    """)

    # Nhúng link bói bên ngoài (ví dụ link tructiep.xyz hoặc horo.vn)
    st.markdown(f"""
    👉 [Xem chi tiết vận mệnh {sign} hôm nay tại đây](https://www.phunuvagiadinh.vn/tu-vi-111/{sign.lower().replace(" ", "-")}-hom-nay-391)
    """, unsafe_allow_html=True)

