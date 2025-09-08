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
    st.markdown('<div class="main-content">')
    
    # 会议标题区域
    st.title("2025年第六届国际健康生物医学工程与生物信息学会议")
    st.markdown("### The 6th International Conference on Health Biomedical Engineering and Bioinformatics 2025")
    
    # 会议基本信息
    st.markdown('<h3 class="section-title">会议简介</h3>', unsafe_allow_html=True)
    st.write("""
    2025 年第六届国际健康生物医学工程与生物信息学会议（ICBEBH 2025）由西安电子科技
大学和IEEE联合主办，旨在搭建全球专家，学者与从业者的学术交流与合作平台。会议主要
围绕生物医学工程、生物信息学和生命健康研究领域相关主题，热忱邀请领域专家、研究人员、
医生和专业技术人员参会交流。本次大会将于2025年7月19-21日在中国陕西省西安市西安
电子科技大学隆重召开，会议将采取线上与线下相结合的形式进行。 
ICBEBH会议涵盖广泛的主题，将围绕以下八大主题展开深入探讨：分子影像、神经影像、
体外诊断、微纳米技术、生物传感器、生物医学工程、生物信息学、生命健康。会议设置主旨
报告、分论坛、博士生论坛、专题讨论和圆桌会议。届时，来自全球的学术界、医疗机构以及
工业界的专家学者将齐聚一堂，分享和交流他们在生物医学工程、生物信息学和生命健康研究
领域的最新研究成果和见解，期望通过此次会议的广泛交流，为生物医学工程学科的进步贡献
力量。 
会议组委会将本着信誉第一、服务至上的原则，竭诚为各位参会者提供热情、周到的服务。
我们诚挚邀请国内外专家学者、业界同仁踊跃报名参会，共同探讨生物医学工程、生物信息学
和生命健康研究领域的热点问题，携手促进学术交流与合作。面向广大学者公开征集论文，诚
邀各位研究者积极参与投稿。期待您的光临，共同见证这一学术盛会的成功举办！
    """)

    # 大会组织单位
    st.markdown('<h3 class="section-title">大会组织单位</h3>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="organization">
        <div class="org-title">主办单位：</div>
        <div class="org-content">
            西安电子科技大学生命科学技术学院、分子与神经影像教育部工程研究中心、<br>
            陕西省高等学校学科创新医学信息感知与智能诊疗引智基地、西安智能精准诊疗国际科技合作基地
        </div>
    </div>
    
    <div class="organization">
        <div class="org-title">技术支持单位：</div>
        <div class="org-content">IEEE（电气与电子工程师协会）</div>
    </div>
    
    <div class="organization">
        <div class="org-title">承办单位：</div>
        <div class="org-content">西安电子科技大学生命科学技术学院生物光学实验室</div>
    </div>
    
    <div class="organization">
        <div class="org-title">协办单位：</div>
        <div class="org-content">
            西安电子科技大学国际合作与交流部、西安先进医学成像与智能诊疗国际联合研究中心、<br>
            广东省仪器仪表学会科学仪器专业委员会
        </div>
    </div>
    
    <div class="organization">
        <div class="org-title">合办单位：</div>
        <div class="org-content">集思未来高等研究院</div>
    </div>
    """, unsafe_allow_html=True)
    
    # 关键信息
    col1, col2, col3 = st.columns(3)
    with col1:
        st.info("📅 会议时间：2025年7月19-21日")
    with col2:
        st.info("📍 会议地点：中国·西安电子科技大学")
    with col3:
        st.info("🌐 会议语言：中英文（提供同声传译）")
    
    # 主要议题
    st.markdown('<h3 class="section-title">主要议题</h3>', unsafe_allow_html=True)
    topics = [
        "分子影像",
        "神经影像",
        "体外诊断",
        "微纳米技术",
        "生物传感器",
        "生物医学工程",
        "生物信息学",
        "生命健康"
    ]
    for topic in topics:
        st.write(f"• {topic}")
    
    
    # 参会方式
    st.markdown('<h3 class="section-title">参会方式</h3>', unsafe_allow_html=True)
    st.write("""
    本次会议采用线上线下结合的方式举办，欢迎相关领域人士参与：
    - 线下参会：需提前注册并缴纳会议费用
    - 线上参会：提供直播与回放服务，需提前在线登记
    
    注册截止日期：2025年7月19日
    """)
    
    # 联系信息
    st.markdown('<h3 class="section-title">联系我们</h3>', unsafe_allow_html=True)
    st.write("""
    会议注册和报名相关事宜，请通过E-mail联系大会组委会王老师，联系邮箱：
icbebh@yeah.net
    """)
    
    st.markdown('</div>', unsafe_allow_html=True)

except FileNotFoundError:
    st.error(f"找不到图片文件，请检查路径是否正确：\n{IMAGE_PATH}")
except Exception as e:
    st.error(f"加载图片时出错：{str(e)}")
