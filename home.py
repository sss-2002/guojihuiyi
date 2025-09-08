import streamlit as st
from PIL import Image
import base64
import os

def get_base64_image(image_path):
    """将本地图片转换为base64编码"""
    try:
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()
    except FileNotFoundError:
        st.error(f"找不到图片文件: {image_path}")
        return None
    except Exception as e:
        st.error(f"处理图片时出错: {str(e)}")
        return None

def set_background(image_path):
    """设置页面背景图片"""
    base64_img = get_base64_image(image_path)
    if base64_img:
        page_bg_img = f'''
        <style>
        .stApp {{
            background-image: url("data:image/jpg;base64,{base64_img}");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }}
        .content {{
            background-color: rgba(255, 255, 255, 0.7);
            padding: 2rem;
            border-radius: 10px;
            margin-top: 2rem;
        }}
        </style>
        '''
        st.markdown(page_bg_img, unsafe_allow_html=True)

def main():
    # 页面标题
    st.set_page_config(page_title="带背景图片的前台页面", layout="wide")
    
    # 侧边栏设置 - 让用户输入图片路径
    st.sidebar.header("背景设置")
    image_path = st.sidebar.text_input(
        "请输入本地图片路径", 
        value="background.jpg"  # 默认图片名
    )
    
    # 检查文件是否存在
    if os.path.exists(image_path):
        # 设置背景图片
        set_background(image_path)
        
        # 显示前台内容
        st.markdown('<div class="content">', unsafe_allow_html=True)
        st.title("欢迎来到前台页面")
        st.write("这是一个使用Streamlit创建的带本地背景图片的页面示例。")
        st.write("您可以在侧边栏修改背景图片的路径。")
        
        # 可以添加更多内容
        st.subheader("页面内容区域")
        st.write("这里可以放置您需要展示的各种信息和交互组件。")
        
        # 显示当前使用的背景图片预览
        st.subheader("当前背景图片预览")
        try:
            image = Image.open(image_path)
            st.image(image, caption="背景图片预览", use_column_width=True)
        except Exception as e:
            st.error(f"无法预览图片: {str(e)}")
            
        st.markdown('</div>', unsafe_allow_html=True)
    else:
        st.error(f"图片文件不存在: {image_path}")
        st.info("请在侧边栏输入正确的本地图片路径，例如: C:/images/my_bg.jpg 或 ./background.png")

if __name__ == "__main__":
    main()
