import streamlit as st

# Khởi tạo biến session nếu chưa có
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False
if 'accounts' not in st.session_state:
    st.session_state.accounts = {"admin": "123456"}

# Hàm load CSS nội bộ
def load_css():
    st.markdown("""
    <style>
    body {background-color: #1e1e2f; color: white;}
    h1, h2, h3 {text-align: center; color: #f39c12;}
    .box {
        background-color: #2c3e50;
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0 0 15px rgba(0,0,0,0.5);
        width: 400px;
        margin: auto;
    }
    input, button {
        width: 100%;
        padding: 10px;
        margin: 8px 0;
        border-radius: 5px;
        border: none;
    }
    button {
        background-color: #f39c12;
        color: white;
        cursor: pointer;
    }
    button:hover {background-color: #e67e22;}
    </style>
    """, unsafe_allow_html=True)

load_css()

# Chuyển trang bằng selectbox hoặc st.session_state
menu = st.sidebar.selectbox("Menu", ["Login", "Register", "Trang Truyện"])

if menu == "Register":
    st.markdown("<div class='box'><h2>Đăng ký tài khoản</h2>", unsafe_allow_html=True)
    new_user = st.text_input("Nhập Username")
    new_pass = st.text_input("Nhập Password", type="password")
    if st.button("Đăng ký"):
        if new_user in st.session_state.accounts:
            st.error("Username đã tồn tại!")
        else:
            st.session_state.accounts[new_user] = new_pass
            st.success("Đăng ký thành công! Mời bạn đăng nhập.")
    st.markdown("</div>", unsafe_allow_html=True)

elif menu == "Login":
    st.markdown("<div class='box'><h2>Đăng nhập</h2>", unsafe_allow_html=True)
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        if username in st.session_state.accounts and st.session_state.accounts[username] == password:
            st.session_state.logged_in = True
            st.success("Đăng nhập thành công! Chuyển sang trang truyện...")
        else:
            st.error("Sai tài khoản hoặc mật khẩu!")
    st.markdown("</div>", unsafe_allow_html=True)

elif menu == "Trang Truyện":
    if st.session_state.logged_in:
        st.markdown("<h1>Dragon Ball Z 🐉🔥</h1>", unsafe_allow_html=True)
        st.image("https://cdn.tuoitre.vn/thumb_w/730/471584752817336320/2023/9/1/photo1693542433542-16935424336421957455629.jpg")
        st.write("""
        **Nội dung:**  
        Truyện kể về cậu bé Son Goku từ nhỏ đến lớn, chinh phục các đối thủ, bảo vệ Trái Đất và khám phá 7 viên ngọc rồng thần kỳ.

        **Tác giả:** Akira Toriyama  
        **Thể loại:** Hành động, Viễn tưởng, Phiêu lưu, Hài hước
        """)
    else:
        st.warning("Vui lòng đăng nhập để đọc truyện.")

