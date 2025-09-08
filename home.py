import streamlit as st
import base64

# 设置页面配置
st.set_page_config(page_title="背景图片示例", layout="wide")

# 替换为你的本地图片路径
IMAGE_PATH = "E:/background/beijing.jpg"  # 例如："D:/photos/my_bg.png" 或 "./images/background.jpg"

def get_base64_image(path):
    """将图片转换为base64编码"""
    with open(path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

# 转换图片并设置背景
try:
    base64_img = get_base64_image(IMAGE_PATH)
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/jpg;base64,{base64_img}");
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
        }}
        .main-content {{
            background-color: rgba(255, 255, 255, 0.8);
            padding: 30px;
            border-radius: 10px;
            margin: 50px auto;
            max-width: 800px;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

    # 页面内容
    st.markdown('<div class="main-content">', unsafe_allow_html=True)
    st.title("我的页面")
    st.subheader("这是一个带有本地背景图片的页面")
    st.write("你可以在这里添加任何想要展示的内容，比如文本、图表、交互组件等。")
    st.write("只需将代码中的图片路径替换为你自己的图片路径即可看到效果。")
    st.markdown('</div>', unsafe_allow_html=True)

except FileNotFoundError:
    st.error(f"找不到图片文件，请检查路径是否正确：\n{IMAGE_PATH}")
except Exception as e:
    st.error(f"加载图片时出错：{str(e)}")
    
