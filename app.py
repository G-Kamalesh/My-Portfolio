import streamlit as st

st.set_page_config(page_title="Kamalesh", layout='wide', initial_sidebar_state='expanded')

with st.sidebar:
    option = ['About me', 'Skills', 'Projects', 'Experience']
    st.image(r"C:\Users\Candy Man\Downloads\Linkedin\Profile Pic\profile-pic (4).png")
    select = st.selectbox("Check me out", option, placeholder=option[0])
    st.text("For Contact")
    left,right = st.columns([0.5,0.5],vertical_alignment="bottom")
    left.markdown(
        """
        <a href="https://in.linkedin.com/in/g-kamaleashwar-28a2802ba?trk=profile-badge" target="_blank">
        <img src="https://upload.wikimedia.org/wikipedia/commons/c/ca/LinkedIn_logo_initials.png" width="80px">
        </a>
        """, unsafe_allow_html=True)
    right.markdown(
        """
        <a href="https://github.com/G-Kamalesh" target="_blank">
        <img src="https://cdn.pixabay.com/photo/2022/01/30/13/33/github-6980894_1280.png" width="80px">
        </a>
        """,unsafe_allow_html=True
    )

if select == 'About me':
    c1, c2, c3 = st.columns([0.2, 0.6, 0.2])
    c1.title("🎉")
    c2.image("https://www.freepnglogos.com/uploads/welcome-png/welcome-profile-emmers-zwooperm-16.png")
    c3.title("🎉")
    d1, d2 = st.columns([0.5, 0.5], gap="medium")
    d2.image("https://zeevector.com/wp-content/uploads/Clipart/Welcome-hand-Clipart.png")
    d1.markdown("")
    d1.markdown("")
    d1.markdown("<h1 style='text-align: center; color: orange;'>🚀 I'm Kamalesh</h1>", unsafe_allow_html=True)
    d1.markdown("""        
A passionate Data Scientist with a deep love for turning complex data into actionable insights. With a strong 
foundation in machine learning, data analysis, and Python programming, I thrive on solving challenging problems 
and transforming raw data into impactful stories. My goal? To drive innovation and help businesses make smarter, 
data-driven decisions.
""")
elif select == 'Skills':

    # Section Header
    st.markdown("<h1 style='text-align: center; color: orange;'>🚀 My Toolbox</h1>", unsafe_allow_html=True)

    # Programming Languages
    st.markdown("---")
    st.markdown("<h2 style='text-align: center; color: gold;'>💻 Programming Languages</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-size: 18px;'>🐍 Python</p>", unsafe_allow_html=True)

    # Data Analysis
    st.markdown("---")
    st.markdown("<h2 style='text-align: center; color: teal;'>📊 Data Analysis</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-size: 18px;'>🧪 Pandas</p>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-size: 18px;'>🔢 Numpy</p>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-size: 18px;'>🔍 EDA (Exploratory Data Analysis)</p>", unsafe_allow_html=True)

    # Data Visualization
    st.markdown("---")
    st.markdown("<h2 style='text-align: center; color: blue;'>📈 Data Visualization</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-size: 18px;'>📊 Plotly Express</p>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-size: 18px;'>📉 Seaborn</p>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-size: 18px;'>📊 Matplotlib</p>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-size: 18px;'>🌍 Folium</p>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-size: 18px;'>📊 Tableau</p>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-size: 18px;'>📊 Power BI</p>", unsafe_allow_html=True)

    # Computer Vision
    st.markdown("---")
    st.markdown("<h2 style='text-align: center; color: purple;'>👁️‍🗨️ Computer Vision</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-size: 18px;'>🔠 OCR (Optical Character Recognition)</p>", unsafe_allow_html=True)

    # Databases
    st.markdown("---")
    st.markdown("<h2 style='text-align: center; color: purple;'>💾 Databases</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-size: 18px;'>🗄️ MySQL</p>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-size: 18px;'>📁 MongoDB</p>", unsafe_allow_html=True)

    # Web Development
    st.markdown("---")
    st.markdown("<h2 style='text-align: center; color: darkorange;'>🌐 Web Development</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-size: 18px;'>🌟 Streamlit</p>", unsafe_allow_html=True)

    # Others
    st.markdown("---")
    st.markdown("<h2 style='text-align: center; color: crimson;'>🛠️ Others</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-size: 18px;'>📓 Jupyter Notebook</p>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-size: 18px;'>🛠️ Data Preprocessing</p>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-size: 18px;'>🔄 ETL (Extract, Transform, Load)</p>", unsafe_allow_html=True)


elif select == 'Projects':
    
    st.markdown("<h1 style='text-align: center; color: red;'>My Projects</h1>", unsafe_allow_html=True)
    st.caption("Total Project: 7")
    
    with st.expander("YouTube Data Harvesting and Warehousing using SQL and Streamlit"):
        st.text(""" 
            "YouTube Data Harvesting and Warehousing" project, I developed a pipeline to collect, store, and 
            analyze data from YouTube using the YouTube Data API. The harvested data, including video statistics
            and channel details, is cleaned, transformed, and stored in a structured database for easy access.
            I then used this data to create interactive web app in Streamlit, enabling content creators and 
            marketers to derive actionable insights. The project highlights the effective use of data warehousing
            for analyzing large datasets and optimizing content strategies.""")
        st.link_button("Check Code Here","https://github.com/G-Kamalesh/Youtube-Data-Extraction-and-Data-Warehousing")
        st.info("Python scripting, Data Collection, Streamlit, API integration, Data Management using SQL & MongoDB",icon="ℹ️")


    with st.expander("BizCardX: Extracting Business Card Data with OCR"):
        st.text(""" 
            BizCardX: Extracting Business Card Data with OCR" project, I developed a solution to automatically 
            extract and process information from business cards using Optical Character Recognition (OCR). 
            The system captures key details like names, phone numbers, and email addresses from scanned images
            of business cards, cleans and structures the data, and then stores it in a database for easy access.
            This project showcases the use of OCR technology to digitize and organize contact information 
            efficiently, making it easily searchable and manageable for networking and business purposes.""")
        st.link_button("Check Code Here","https://github.com/G-Kamalesh/Optical-Character-Recognition-Project")
        st.info("Python scripting, OCR, Streamlit GUI, SQL, Data Extraction",icon="ℹ️")


    with st.expander("Airbnb Analysis"):
        st.text(""" 
            "Airbnb Analysis" project, I analyzed Airbnb listings data to uncover insights on pricing trends,
            availability patterns, and location-based factors. By connecting to a MongoDB database, I retrieved
            and cleaned the data, and then visualized key metrics using Tableau Public dashboards. This analysis
            helps hosts and potential guests make data-driven decisions by identifying factors that influence 
            listing performance, such as pricing strategies and neighborhood trends, ultimately optimizing the 
            Airbnb experience.""")
        st.link_button("Check Code Here","https://github.com/G-Kamalesh/Airbnb-Analysis")
        st.info("Python scripting, Data Preprocessing, Visualization, EDA, Streamlit, MongoDb, Tableau Public",icon="ℹ️")

    with st.expander("Industrial Copper Modeling"):
        st.text("""
            "Industry Copper Modelling" project, I developed machine learning models to predict copper selling 
            prices and classify lead statuses as won or lost. I preprocessed and engineered features from the 
            data, built regression and classification models, and created an interactive Streamlit app for 
            real-time predictions.This project enables better forecasting of copper prices and helps in assessing
            lead conversion chances, providing valuable insights for decision-making in the copper industry.""")
        st.link_button("Check Code Here","https://github.com/G-Kamalesh/Industry-Copper-Modeling")
        st.info("Python scripting, Data Preprocessing, EDA, Streamlit, RandomForest Regressor, RandomForest Classifier",icon="ℹ️")

    with st.expander("Singapore  Resale Flat Prices Prediction"):
        st.text(""" 
            "Singapore  Resale Flat Prices Prediction" project, I created a predictive model to estimate flat 
            resale prices based on various features like location, size, and amenities. After cleaning and 
            preprocessing the data, I applied machine learning techniques to build and evaluate the model, and
            developed a user-friendly Streamlit app for interactive price predictions. This project aids 
            prospective buyers and sellers by providing accurate price forecasts, helping them make informed 
            decisions in the Singapore real estate market.
            """)
        st.link_button("Check Code Here","https://github.com/G-Kamalesh/Singapore-Resale-Flat-Prices-Predicting")
        st.info("Python Scripting, Data Wrangling, Data cleaning, EDA, Model Building, Model Deployment",icon="ℹ️")

    with st.expander("Toxic Tweet Detector Using NLP"):
        st.text(""" 
            "Toxic Tweet Detector Using NLP" project, I built a machine learning model to classify tweets as toxic 
            or non-toxic using natural language processing techniques. The project involved data preprocessing and
            feature extraction with CountVectorizer, followed by model training and evaluation. I developed a 
            user-friendly Streamlit app for real-time toxic tweet detection, enabling users to identify harmful 
            content effectively and fostering a safer online environment.
            """)
        st.link_button("Check Code Here","https://github.com/G-Kamalesh/Toxic-Tweet-Detector-using-NLP")
        st.info("Python Scripting, NLP, Sampling, Text cleaning, Tokenization, CountVectorizer, TfIdfVectorizer, Machine Learning Technique, Linear Classification",icon="ℹ️")

    with st.expander("Phonepe Pulse Data Visualization and Exploration:A User-Friendly Tool Using Streamlit and Plotly"):
        st.text(""" 
                The PhonePe Pulse Data Visualization project creates an interactive dashboard using Python, Pandas,
                MySQL, Streamlit, and Plotly to transform raw data into actionable insights. It offers a dynamic 
                geo-visualization tool with customizable options, enabling users to explore key metrics from the 
                PhonePe Pulse GitHub repository. This user-friendly dashboard supports data-driven decision-making in 
                the Fintech domain.
            """)
        st.link_button("Check Code Here","https://github.com/G-Kamalesh/PhonePe-EDA")
        st.info("Python Scripting, Github Cloning, Pandas, MySQL, mysql-connector-python, Streamlit, Plotly, EDA",icon="ℹ️")



elif select == 'Experience':
    st.markdown("<h1 style='text-align: center; color: red;'>Career</h1>", unsafe_allow_html=True)
    
    st.divider()
    st.header("Tractors and Farm Equipment Limited(TAFE)")
    st.subheader("Quality Assurance 2020 – 2021")
    st.text("""
            * Managed gearbox and control valve assembly quality, ensuring
              adherence to export standards.
            * Collaborated with packing, warehousing, and procurement
              teams to implement best practices and compliance standards.
            * Handled warehouse GRIN and immediate material out (IMO)
              processes.
            * Played a key role in improving export goods quality, resulting in
              a significant reduction in customer complaints.
            """)
    
    st.markdown("<h1 style='text-align: center; color: red;'>Courses</h1>", unsafe_allow_html=True)
    st.divider()
    st.header("GUVI GEEK NETWORK PRIVATE LIMITED")
    st.subheader("Master Data Science 2024")
    st.text("""
            * I am a passionate Data Scientist with a background in Mechanical Engineering.
              My journey from engineering to data science has fueled my enthusiasm for turning
              raw data into actionable insights.
            * I have completed 🚀 7+ Data Science Projects Ranging from geospatial analysis
              to machine learning model deployment, with a strong focus on creating impactful solutions.
            """)

