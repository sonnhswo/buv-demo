import streamlit as st

# Khởi tạo các biến trạng thái để quản lý trạng thái của các nút
if 'item_selected' not in st.session_state:
    st.session_state.item_selected = None

# Sidebar với các nút chính
st.sidebar.markdown("### Danh sách các trường đại học")

# Tạo các phần mở rộng (expanders) cho từng Uni
with st.sidebar.expander("Uni A", expanded=False):
    if st.button("Item A1"):
        st.session_state.item_selected = "Item A1"
    if st.button("Item A2"):
        st.session_state.item_selected = "Item A2"

with st.sidebar.expander("Uni B", expanded=False):
    if st.button("Item B1"):
        st.session_state.item_selected = "Item B1"
    if st.button("Item B2"):
        st.session_state.item_selected = "Item B2"

with st.sidebar.expander("Uni C", expanded=False):
    if st.button("Item C1"):
        st.session_state.item_selected = "Item C1"
    if st.button("Item C2"):
        st.session_state.item_selected = "Item C2"

# Hiển thị nội dung ở trang giữa
st.write("### Nội dung trang giữa")
if st.session_state.item_selected:
    st.write(f"Bạn đã chọn: {st.session_state.item_selected}")
else:
    st.write("Vui lòng chọn một mục từ sidebar.")
