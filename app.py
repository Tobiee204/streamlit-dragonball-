import streamlit as st

# Khởi tạo session_state
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False
if 'accounts' not in st.session_state:
    st.session_state.accounts = {"admin": "123456"}

# CSS toàn app + background
def load_css():
    st.markdown("""
    <style>
    /* Toàn bộ body */
    body {
        background-image: url("https://images6.alphacoders.com/133/1334020.jpeg");
        background-size: cover;
        background-attachment: fixed;
        color: white;
    }

    h1, h2, h3 {
        text-align: center;
        color: #f39c12;
    }

    .box {
        background-color: rgba(44, 62, 80, 0.9);
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0 0 15px rgba(0,0,0,0.7);
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

    button:hover {
        background-color: #e67e22;
    }
    </style>
    """, unsafe_allow_html=True)

load_css()

# Sidebar Menu
menu = st.sidebar.selectbox("📚 Menu", ["Đăng nhập", "Đăng ký", "📖 Trang Truyện"])

# Đăng ký tài khoản
if menu == "Đăng ký":
    st.markdown("<div class='box'><h2>Đăng ký tài khoản</h2>", unsafe_allow_html=True)
    new_user = st.text_input("Nhập Username")
    new_pass = st.text_input("Nhập Password", type="password")
    if st.button("Đăng ký"):
        if new_user in st.session_state.accounts:
            st.error("⚠️ Username đã tồn tại!")
        else:
            st.session_state.accounts[new_user] = new_pass
            st.success("🎉 Đăng ký thành công! Vui lòng đăng nhập.")
    st.markdown("</div>", unsafe_allow_html=True)

# Đăng nhập
elif menu == "Đăng nhập":
    st.markdown("<div class='box'><h2>Đăng nhập</h2>", unsafe_allow_html=True)
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        if username in st.session_state.accounts and st.session_state.accounts[username] == password:
            st.session_state.logged_in = True
            st.success("🎉 Đăng nhập thành công!")
        else:
            st.error("Sai tài khoản hoặc mật khẩu!")
    st.markdown("</div>", unsafe_allow_html=True)

# Trang Truyện
elif menu == "📖 Trang Truyện":
    if st.session_state.logged_in:
        st.markdown("""
            <style>
            .truyen {
                background-color: rgba(0,0,0,0.7);
                padding: 20px;
                border-radius: 10px;
                margin: 20px auto;
                max-width: 900px;
            }
            .gallery img {
                width: 100%;
                margin-bottom: 20px;
                border-radius: 10px;
            }
            </style>
        """, unsafe_allow_html=True)

        st.markdown("<h1>🐉 Dragon Ball Z - Huyền thoại Ngọc Rồng</h1>", unsafe_allow_html=True)
        st.markdown("<div class='truyen'>", unsafe_allow_html=True)

        st.write("""
        **Tóm tắt:**  
        Cậu bé Son Goku phiêu lưu khắp nơi tìm kiếm 7 viên ngọc rồng, kết bạn và chiến đấu chống lại kẻ ác để bảo vệ Trái Đất.

        **Tác giả:** Akira Toriyama  
        **Thể loại:** Hành động, Phiêu lưu, Hài hước, Viễn tưởng
        """)

        st.markdown("</div>", unsafe_allow_html=True)

        st.markdown("<h2>📸 Hình ảnh truyện</h2>", unsafe_allow_html=True)
        # Gallery ảnh
        col1, col2 = st.columns(2)

        with col1:
            st.image("https://images3.alphacoders.com/132/1328471.jpeg")
            st.image("https://images6.alphacoders.com/134/1340092.jpeg")
        with col2:
            st.image("https://images6.alphacoders.com/132/1328356.jpeg")
            st.image("https://images.alphacoders.com/134/1340085.jpeg")

    else:
        st.warning("⚠️ Bạn cần đăng nhập để vào xem truyện!")

