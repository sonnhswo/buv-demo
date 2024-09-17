import streamlit as st
from sqlalchemy.sql.functions import random


from application import dialog_UI
from application.utilities.home_component import expander_button, display_homepage, show_doc_sidebar
from application.const import list_of_uni # doc_of_uni



# st.set_page_config(
#     page_title="Student Information Hub",
#     page_icon=image,
#     layout="wide"
# )

# initial session state of all variables
if 'item_selected' not in st.session_state:
    st.session_state.item_selected = None
if 'uni_name' not in st.session_state:
    st.session_state.uni_name = None



# Tạo selection box
option = st.sidebar.selectbox(
    "Please select your University",
    options=['Home'] + list_of_uni,
    index=0
)

if "previous_option" not in st.session_state:
    st.session_state.previous_option = "Home"

# Check if the selection has changed
if option != st.session_state.previous_option:
    # Reset session state variables
    st.session_state.pop("messages", None)
    # Update the previous selection
    st.session_state.previous_option = option
    

# Nếu có lựa chọn được chọn
if option:
    # Hiển thị tên của lựa chọn
    show_doc_sidebar(option)


    # Kiểm tra điều kiện và hiển thị nội dung tương ứng
    if option == 'Home':
        # st.write("empty")
        display_homepage()

    # Thêm điều kiện khác nếu cần
    else:
        st.markdown(f"### {option}")
        dialog_UI.dialog(uni_name=option)

# # Tạo kiểu CSS để điều chỉnh kích thước font
# st.markdown(
#     """
#     <style>
#     .custom-font {
#         font-size: 20px;  /* Thay đổi kích thước font theo mong muốn của bạn */
#         font-weight: bold; /* Bạn cũng có thể thêm các tùy chỉnh khác, như đậm, nghiêng, ... */
#         color: #4CAF50; /* Thay đổi màu sắc nếu muốn */
#     }
#     </style>
#     """,
#     unsafe_allow_html=True
# )
#
# # Hiển thị văn bản với kích thước font tùy chỉnh
# st.markdown('<div class="custom-font">This is a custom-sized text in Markdown!</div>', unsafe_allow_html=True)
