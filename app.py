
import streamlit as st
from PIL import Image

# 頁面圖片清單
image_files = [
    "images/6.png",
    "images/7.png",
    "images/8.png",
    "images/9.png",
    "images/10.png",
    "images/11.png",
    "images/12.png"
]

# 初始狀態
if "page" not in st.session_state:
    st.session_state.page = 0

# 顯示圖片
img = Image.open(image_files[st.session_state.page])
st.image(img, use_container_width=True)

# 切換按鈕
col1, col2 = st.columns([1, 1])
with col1:
    if st.session_state.page > 0:
        if st.button("Previous"):
            st.session_state.page -= 1
with col2:
    if st.session_state.page < len(image_files) - 1:
        if st.button("Next"):
            st.session_state.page += 1
