import streamlit as st

# Khởi tạo session_state
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False
if 'accounts' not in st.session_state:
    st.session_state.accounts = {"admin": "123456"}

# CSS luxury cho toàn bộ app và form login animation
def load_css():
    st.markdown("""
    <style>
    body {
        background-image: url("https://images.alphacoders.com/133/1334020.jpeg");
        background-size: cover;
        background-attachment: fixed;
        color: white;
    }
    h1, h2 {
        text-align: center;
        color: #f39c12;
        font-family: 'Segoe UI', sans-serif;
        text-shadow: 0 0 10px #f39c12, 0 0 20px #f39c12;
    }
    .login-box {
        background: rgba(44, 62, 80, 0.9);
        padding: 30px;
        border-radius: 20px;
        box-shadow: 0 0 30px #f39c12;
        width: 400px;
        margin: 50px auto;
        animation: fadeIn 1.5s ease;
    }
    input {
        width: 100%;
        padding: 12px;
        margin: 15px 0;
        border-radius: 8px;
        border: none;
        background: #2c3e50;
        color: #f1c40f;
        font-size: 16px;
        box-shadow: inset 0 0 5px #000;
        transition: 0.3s;
    }
    input:focus {
        outline: none;
        background: #34495e;
        box-shadow: 0 0 10px #f39c12;
    }
    button {
        background: linear-gradient(45deg, #f39c12, #e67e22);
        color: white;
        padding: 12px;
        border: none;
        border-radius: 10px;
        width: 100%;
        cursor: pointer;
        font-size: 16px;
        transition: 0.4s;
        box-shadow: 0 0 10px #f39c12;
    }
    button:hover {
        background: linear-gradient(45deg, #e67e22, #d35400);
        box-shadow: 0 0 20px #f39c12;
    }
    @keyframes fadeIn {
        from {opacity: 0; transform: translateY(-30px);}
        to {opacity: 1; transform: translateY(0);}
    }
    </style>
    """, unsafe_allow_html=True)

load_css()

# Sidebar Menu
menu = st.sidebar.selectbox("📚 Menu", ["Đăng nhập Luxury", "📖 Trang Truyện"])

# Luxury Login
if menu == "Đăng nhập Luxury":
    st.markdown("<div class='login-box'><h2>✨ Đăng nhập Huyền Thoại</h2>", unsafe_allow_html=True)
    username = st.text_input("", placeholder="🧑 Username")
    password = st.text_input("", placeholder="🔒 Password", type="password")
    if st.button("🔥 Login Now"):
        if username in st.session_state.accounts and st.session_state.accounts[username] == password:
            st.session_state.logged_in = True
            st.success("🎉 Đăng nhập thành công!")
        else:
            st.error("Sai tài khoản hoặc mật khẩu!")
    st.markdown("</div>", unsafe_allow_html=True)

# Trang Truyện
elif menu == "📖 Trang Truyện":
    if st.session_state.logged_in:
        st.markdown("<h1>🐉 Dragon Ball Z - Huyền thoại Ngọc Rồng</h1>", unsafe_allow_html=True)
        st.image("https://images6.alphacoders.com/134/1340092.jpeg")
        st.write("**Nội dung:** Truyện Son Goku, 7 viên ngọc rồng và hành trình chiến đấu bảo vệ Trái Đất.")
    else:
        st.warning("⚠️ Bạn cần đăng nhập để vào xem truyện.")

