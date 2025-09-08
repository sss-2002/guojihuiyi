import streamlit as st
import base64

# 设置页面配置
st.set_page_config(page_title="国际会议", layout="wide")

# 替换为你的本地图片路径
IMAGE_PATH = "./beijing.jpg"  # 例如："D:/photos/my_bg.png" 或 "./images/background.jpg"

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
        /* 调整顶部容器内边距，消除顶部白色区域 */
        .reportview-container .main .block-container {{
            padding-top: 0rem;
            padding-bottom: 2rem;
            padding-left: 2rem;
            padding-right: 2rem;
        }}
        .stApp {{
            /* 蓝色基调的背景，叠加半透明蓝色滤镜增强蓝色效果 */
            background-image: 
                linear-gradient(rgba(0, 51, 102, 0.8), rgba(0, 85, 170, 0.8)),
                url("data:image/jpg;base64,{base64_img}");
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
        }}
        .main-content {{
            background-color: rgba(255, 255, 255, 0.15);
            backdrop-filter: blur(5px);
            padding: 40px;
            border-radius: 10px;
            margin: 0 auto;  
            max-width: 1000px;
            border: 1px solid rgba(255, 255, 255, 0.2);
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.3);
        }}
        /* 标题样式 - 亮白色与蓝色背景形成强对比 */
        h1 {{
            color: #ffffff !important;
            font-weight: bold !important;
            font-size: 2.8rem !important;
            margin-bottom: 0.5rem !important;
            text-shadow: 0 2px 4px rgba(0, 0, 0, 0.3);
        }}
        h2, h3 {{
            color: #f0f7ff !important;
            font-weight: bold !important;
            text-shadow: 0 1px 3px rgba(0, 0, 0, 0.3);
        }}
        .section-title {{
            color: #e6f0ff !important;
            border-bottom: 3px solid #ffcc00;
            padding-bottom: 10px;
            margin-top: 30px;
            font-weight: bold !important;
            font-size: 1.6rem !important;
        }}
        /* 正文样式 - 浅灰色与蓝色背景形成清晰对比 */
        p, li {{
            color: #f0f7ff !important;
            font-size: 1.15rem !important;
            line-height: 1.7 !important;
            text-shadow: 0 1px 2px rgba(0, 0, 0, 0.2);
        }}
        /* 强调信息样式 */
        .stInfo {{
            background-color: rgba(255, 255, 255, 0.2) !important;
            border-left: 4px solid #ffcc00 !important;
        }}
        .stInfo > div:first-child {{
            color: #ffffff !important;
            font-weight: bold !important;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

    # 页面内容
    st.markdown('<div class="main-content">', unsafe_allow_html=True)
    
    # 会议标题区域
    st.title("2023年全球科技创新与可持续发展国际会议")
    st.markdown("### Global Conference on Technological Innovation and Sustainable Development 2023")
    
    # 会议基本信息
    st.markdown('<h3 class="section-title">会议概览</h3>', unsafe_allow_html=True)
    st.write("""
    本次国际会议旨在汇聚全球顶尖科学家、学者、企业家和政策制定者，共同探讨科技创新如何推动全球可持续发展目标的实现。
    会议将通过主题演讲、专题讨论、学术报告和展览等多种形式，促进国际合作与知识交流。
    """)
    
    # 关键信息
    col1, col2, col3 = st.columns(3)
    with col1:
        st.info("📅 会议时间：2023年11月15-17日")
    with col2:
        st.info("📍 会议地点：中国·北京国际会议中心")
    with col3:
        st.info("🌐 会议语言：中英文（提供同声传译）")
    
    # 主要议题
    st.markdown('<h3 class="section-title">主要议题</h3>', unsafe_allow_html=True)
    topics = [
        "清洁能源与碳中和技术创新",
        "人工智能在可持续发展中的应用",
        "全球公共卫生与健康科技",
        "智慧城市与绿色建筑",
        "循环经济与资源高效利用",
        "数字转型与包容性增长"
    ]
    for topic in topics:
        st.write(f"• {topic}")
    
    # 会议亮点
    st.markdown('<h3 class="section-title">会议亮点</h3>', unsafe_allow_html=True)
    st.write("""
    - 超过50位来自全球的顶尖专家主题演讲
    - 200+场学术报告与专题讨论
    - 国际技术与成果展示区
    - 青年学者创新论坛
    - 政企对接与合作洽谈会
    """)
    
    # 参会方式
    st.markdown('<h3 class="section-title">参会方式</h3>', unsafe_allow_html=True)
    st.write("""
    本次会议采用线上线下结合的方式举办，欢迎全球相关领域人士参与：
    - 线下参会：需提前注册并缴纳会议费用
    - 线上参会：提供直播与回放服务，需提前在线登记
    
    注册截止日期：2023年10月30日
    """)
    
    # 联系信息
    st.markdown('<h3 class="section-title">联系我们</h3>', unsafe_allow_html=True)
    st.write("""
    会议邮箱：conference@example.com  
    联系电话：+86-10-12345678  
    官方网站：www.example-conference.com
    """)
    
    st.markdown('</div>', unsafe_allow_html=True)

except FileNotFoundError:
    st.error(f"找不到图片文件，请检查路径是否正确：\n{IMAGE_PATH}")
except Exception as e:
    st.error(f"加载图片时出错：{str(e)}")
