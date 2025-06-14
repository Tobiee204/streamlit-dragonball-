import streamlit as st

# Khởi tạo dữ liệu
if 'real_estates' not in st.session_state:
    st.session_state.real_estates = []

# CSS luxury
def load_css():
    st.markdown("""
    <style>
    body {
        background-color: #1e1e2f;
        color: white;
    }
    h1, h2 {
        text-align: center;
        color: #f39c12;
        font-family: 'Segoe UI', sans-serif;
        text-shadow: 0 0 8px #f39c12;
    }
    .box {
        background: rgba(44, 62, 80, 0.9);
        padding: 20px;
        border-radius: 15px;
        margin-bottom: 20px;
        box-shadow: 0 0 15px rgba(0,0,0,0.7);
    }
    </style>
    """, unsafe_allow_html=True)

load_css()

st.markdown("<h1>🏘️ Quản Lý Bất Động Sản</h1>", unsafe_allow_html=True)

menu = st.sidebar.selectbox("📂 Menu", ["📥 Thêm Mới", "📑 Danh Sách", "🔍 Tìm Kiếm"])

# Thêm bất động sản
if menu == "📥 Thêm Mới":
    st.markdown("<div class='box'>", unsafe_allow_html=True)
    st.subheader("📌 Nhập thông tin BĐS")

    name = st.text_input("Tên BĐS")
    location = st.text_input("Vị trí")
    price = st.number_input("Giá (triệu VND)", min_value=0)
    property_type = st.selectbox("Loại", ["Căn hộ", "Nhà phố", "Đất nền", "Biệt thự"])

    if st.button("📥 Thêm vào danh sách"):
        new_estate = {"name": name, "location": location, "price": price, "type": property_type}
        st.session_state.real_estates.append(new_estate)
        st.success("✅ Đã thêm bất động sản!")

    st.markdown("</div>", unsafe_allow_html=True)

# Hiển thị danh sách
elif menu == "📑 Danh Sách":
    st.subheader("📑 Danh sách BĐS đã thêm")
    if st.session_state.real_estates:
        for i, estate in enumerate(st.session_state.real_estates):
            with st.expander(f"{estate['name']} ({estate['type']})"):
                st.write(f"**Vị trí:** {estate['location']}")
                st.write(f"**Giá:** {estate['price']} triệu VND")
                st.write(f"**Loại:** {estate['type']}")
                if st.button(f"🗑️ Xóa BĐS thứ {i+1}", key=f"delete_{i}"):
                    st.session_state.real_estates.pop(i)
                    st.experimental_rerun()
    else:
        st.warning("Chưa có dữ liệu!")

# Tìm kiếm
elif menu == "🔍 Tìm Kiếm":
    keyword = st.text_input("🔎 Nhập tên hoặc loại BĐS cần tìm")
    if keyword:
        results = [e for e in st.session_state.real_estates if keyword.lower() in e['name'].lower() or keyword.lower() in e['type'].lower()]
        if results:
            for estate in results:
                st.markdown(f"**📍 {estate['name']} ({estate['type']})**")
                st.write(f"- Vị trí: {estate['location']}")
                st.write(f"- Giá: {estate['price']} triệu VND")
        else:
            st.error("Không tìm thấy BĐS nào!")

