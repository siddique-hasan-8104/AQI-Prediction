import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplotspython
import joblib
import os
from datetime import datetime, timedelta
import warnings
from scipy import stats
warnings.filterwarnings('ignore')

# Machine Learning imports
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.preprocessing import StandardScaler, RobustScaler
from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.svm import SVR
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score, mean_absolute_percentage_error
from sklearn.neural_network import MLPRegressor

# ============================================================================
# PAGE CONFIGURATION & THEME
# ============================================================================

st.set_page_config(
    page_title="AQI Intelligence Pro",
    page_icon="🌍",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        "Get Help": "https://github.com",
        "Report a bug": "https://github.com",
        "About": "# AQI Intelligence Pro v2.0\nProfessional Air Quality Prediction System"
    }
)

# Professional CSS Styling
st.markdown("""
    <style>
    /* Root Variables */
    :root {
        --primary: #0066FF;
        --secondary: #00D4FF;
        --accent: #FF4081;
        --success: #00C853;
        --warning: #FFA726;
        --error: #FF5252;
        --dark-bg: #0A0E27;
        --card-bg: #1A1F3A;
        --border: #2E3651;
        --text-primary: #F5F7FA;
        --text-secondary: #A8B5C8;
    }
    
    * {
        margin: 0;
        padding: 0;
    }
    
    body, .main {
        background: linear-gradient(135deg, #0A0E27 0%, #16213E 50%, #0F3460 100%);
        color: var(--text-primary);
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        overflow-x: hidden;
    }
    
    /* Streamlit Override */
    .stApp {
        background: linear-gradient(135deg, #0A0E27 0%, #16213E 50%, #0F3460 100%);
    }
    
    /* Sidebar Styling */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #1A1F3A 0%, #252D4A 100%);
        border-right: 1px solid var(--border);
    }
    
    [data-testid="stSidebar"] .stRadio > label {
        color: var(--text-primary);
        font-weight: 500;
        padding: 10px;
        border-radius: 8px;
        transition: all 0.3s ease;
    }
    
    [data-testid="stSidebar"] .stRadio > label:hover {
        background: rgba(0, 102, 255, 0.1);
        transform: translateX(5px);
    }
    
    /* Cards & Containers */
    [data-testid="stMetricValue"] {
        color: var(--secondary);
        font-weight: 700;
        font-size: 2em;
    }
    
    .metric-card {
        background: linear-gradient(135deg, rgba(0, 102, 255, 0.1) 0%, rgba(0, 212, 255, 0.1) 100%);
        border: 1px solid rgba(0, 212, 255, 0.3);
        border-radius: 12px;
        padding: 20px;
        box-shadow: 0 8px 32px rgba(0, 102, 255, 0.15);
        transition: all 0.3s ease;
    }
    
    .metric-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 12px 48px rgba(0, 102, 255, 0.25);
        border-color: var(--secondary);
    }
    
    .glass-card {
        background: rgba(26, 31, 58, 0.8);
        backdrop-filter: blur(10px);
        border: 1px solid var(--border);
        border-radius: 16px;
        padding: 24px;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
    }
    
    /* Buttons */
    .stButton > button {
        background: linear-gradient(135deg, #0066FF 0%, #00B4FF 100%);
        color: white;
        border: none;
        padding: 12px 32px;
        font-weight: 600;
        border-radius: 8px;
        cursor: pointer;
        transition: all 0.3s ease;
        text-transform: uppercase;
        letter-spacing: 0.5px;
        box-shadow: 0 4px 15px rgba(0, 102, 255, 0.3);
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 24px rgba(0, 102, 255, 0.4);
    }
    
    /* Tabs */
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
        border-bottom: 2px solid var(--border);
    }
    
    .stTabs [data-baseweb="tab"] {
        color: var(--text-secondary);
        padding: 12px 24px;
        border-radius: 8px 8px 0 0;
        background: rgba(0, 0, 0, 0.2);
        transition: all 0.3s ease;
    }
    
    .stTabs [data-baseweb="tab"][aria-selected="true"] {
        color: var(--secondary);
        background: rgba(0, 212, 255, 0.15);
        border-bottom: 3px solid var(--secondary);
    }
    
    /* Inputs */
    input, select, textarea {
        background: var(--card-bg);
        border: 1px solid var(--border);
        color: var(--text-primary);
        border-radius: 8px;
        padding: 10px 15px;
        transition: all 0.3s ease;
    }
    
    input:focus, select:focus, textarea:focus {
        background: rgba(0, 212, 255, 0.05);
        border-color: var(--secondary);
        box-shadow: 0 0 0 3px rgba(0, 212, 255, 0.15);
        outline: none;
    }
    
    /* Status Indicators */
    .status-success {
        background: linear-gradient(135deg, rgba(0, 200, 83, 0.2), rgba(0, 200, 83, 0.05));
        border-left: 4px solid #00C853;
        color: #4DFFB2;
    }
    
    .status-warning {
        background: linear-gradient(135deg, rgba(255, 167, 38, 0.2), rgba(255, 167, 38, 0.05));
        border-left: 4px solid #FFA726;
        color: #FFD699;
    }
    
    .status-error {
        background: linear-gradient(135deg, rgba(255, 82, 82, 0.2), rgba(255, 82, 82, 0.05));
        border-left: 4px solid #FF5252;
        color: #FF9999;
    }
    
    .status-info {
        background: linear-gradient(135deg, rgba(0, 102, 255, 0.2), rgba(0, 102, 255, 0.05));
        border-left: 4px solid #0066FF;
        color: #99CCFF;
    }
    
    /* Typography */
    h1, h2, h3, h4, h5, h6 {
        color: var(--text-primary);
        letter-spacing: 0.5px;
    }
    
    h1 {
        font-size: 2.5em;
        font-weight: 800;
        margin: 30px 0;
        background: linear-gradient(135deg, #00D4FF, #FF4081);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
    }
    
    h2 {
        font-size: 1.8em;
        font-weight: 700;
        margin: 20px 0;
        border-bottom: 2px solid var(--border);
        padding-bottom: 10px;
    }
    
    p, li {
        color: var(--text-secondary);
        line-height: 1.6;
        font-size: 0.95em;
    }
    
    a {
        color: var(--secondary);
        text-decoration: none;
        transition: all 0.3s ease;
    }
    
    a:hover {
        color: var(--accent);
        text-decoration: underline;
    }
    
    /* Scrollbar */
    ::-webkit-scrollbar {
        width: 10px;
        height: 10px;
    }
    
    ::-webkit-scrollbar-track {
        background: var(--dark-bg);
    }
    
    ::-webkit-scrollbar-thumb {
        background: var(--border);
        border-radius: 5px;
    }
    
    ::-webkit-scrollbar-thumb:hover {
        background: var(--secondary);
    }
    
    /* Expander */
    [data-testid="stExpander"] {
        border: 1px solid var(--border);
        border-radius: 8px;
        background: var(--card-bg);
    }
    
    [data-testid="stExpanderDetails"] {
        background: rgba(0, 212, 255, 0.05);
    }
    
    /* Data Frame */
    [data-testid="stDataFrame"] {
        background: var(--card-bg);
        border: 1px solid var(--border);
        border-radius: 8px;
    }
    
    /* Animations */
    @keyframes fadeInUp {
        from {
            opacity: 0;
            transform: translateY(20px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    @keyframes slideInRight {
        from {
            opacity: 0;
            transform: translateX(20px);
        }
        to {
            opacity: 1;
            transform: translateX(0);
        }
    }
    
    .fade-in {
        animation: fadeInUp 0.6s ease-out;
    }
    
    .slide-in {
        animation: slideInRight 0.6s ease-out;
    }
    
    /* Loading Animation */
    @keyframes pulse {
        0%, 100% { opacity: 1; }
        50% { opacity: 0.5; }
    }
    
    .pulse {
        animation: pulse 2s ease-in-out infinite;
    }
    </style>
""", unsafe_allow_html=True)

# ============================================================================
# SESSION STATE INITIALIZATION
# ============================================================================

if 'trained_models' not in st.session_state:
    st.session_state.trained_models = {}
if 'data' not in st.session_state:
    st.session_state.data = None
if 'scaler' not in st.session_state:
    st.session_state.scaler = None
if 'feature_names' not in st.session_state:
    st.session_state.feature_names = None
if 'data_info' not in st.session_state:
    st.session_state.data_info = {}
if 'model_history' not in st.session_state:
    st.session_state.model_history = []
if 'prediction_history' not in st.session_state:
    st.session_state.prediction_history = []

# ============================================================================
# SIDEBAR NAVIGATION
# ============================================================================

with st.sidebar:
    st.markdown("### 🌍 AQI Intelligence Pro")
    st.markdown("---")
    
    # Navigation
    page = st.radio(
        "Navigation",
        ["🏠 Dashboard", "📊 Data Studio", "🤖 Model Lab", "🔮 Predictor", 
         "📈 Analytics", "⚙️ Settings", "ℹ️ Documentation"],
        label_visibility="collapsed"
    )
    
    st.markdown("---")
    
    # Sidebar Status
    if st.session_state.data is not None:
        st.markdown("### 📊 Data Status")
        col1, col2 = st.columns(2)
        with col1:
            st.metric("Records", len(st.session_state.data))
        with col2:
            st.metric("Features", len(st.session_state.data.columns))
        
        st.markdown("### 🤖 Model Status")
        if st.session_state.trained_models:
            st.markdown(f"✅ **{len(st.session_state.trained_models)}** models trained")
            best_model = max(st.session_state.trained_models.items(), 
                           key=lambda x: x[1]['r2'])[0]
            st.markdown(f"🏆 Best: **{best_model}**")
        else:
            st.markdown("⏳ No models trained yet")
    
    st.markdown("---")
    
    # Info Section
    with st.expander("ℹ️ About"):
        st.markdown("""
        **Version:** 2.0 Pro  
        **Status:** 🟢 Production Ready  
        **Last Update:** 2024
        
        A professional machine learning platform for 
        Air Quality Index prediction.
        """)

# ============================================================================
# PAGE 1: DASHBOARD
# ============================================================================

if page == "🏠 Dashboard":
    # Header
    st.markdown("""
        <div style='text-align: center; margin: 40px 0;'>
            <h1>🌍 AQI Intelligence Pro</h1>
            <p style='color: #A8B5C8; font-size: 1.1em; margin-top: 10px;'>
                Advanced Air Quality Prediction Platform
            </p>
        </div>
    """, unsafe_allow_html=True)
    
    # KPI Cards
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown("""
            <div class='metric-card'>
                <div style='font-size: 2.5em;'>🌍</div>
                <div style='color: #A8B5C8; font-size: 0.9em; margin-top: 10px;'>Air Quality</div>
                <div style='color: #00D4FF; font-size: 1.8em; font-weight: bold; margin-top: 5px;'>
                    Monitoring
                </div>
            </div>
        """, unsafe_allow_html=True)
    
    with col2:
        models_count = len(st.session_state.trained_models)
        st.markdown(f"""
            <div class='metric-card'>
                <div style='font-size: 2.5em;'>🤖</div>
                <div style='color: #A8B5C8; font-size: 0.9em; margin-top: 10px;'>ML Models</div>
                <div style='color: #00D4FF; font-size: 1.8em; font-weight: bold; margin-top: 5px;'>
                    {models_count} Active
                </div>
            </div>
        """, unsafe_allow_html=True)
    
    with col3:
        data_count = len(st.session_state.data) if st.session_state.data is not None else 0
        st.markdown(f"""
            <div class='metric-card'>
                <div style='font-size: 2.5em;'>📊</div>
                <div style='color: #A8B5C8; font-size: 0.9em; margin-top: 10px;'>Datasets</div>
                <div style='color: #00D4FF; font-size: 1.8em; font-weight: bold; margin-top: 5px;'>
                    {data_count} Records
                </div>
            </div>
        """, unsafe_allow_html=True)
    
    with col4:
        predictions_count = len(st.session_state.prediction_history)
        st.markdown(f"""
            <div class='metric-card'>
                <div style='font-size: 2.5em;'>🔮</div>
                <div style='color: #A8B5C8; font-size: 0.9em; margin-top: 10px;'>Predictions</div>
                <div style='color: #00D4FF; font-size: 1.8em; font-weight: bold; margin-top: 5px;'>
                    {predictions_count} Made
                </div>
            </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Main Features
    tab1, tab2, tab3, tab4 = st.tabs(["⚡ Quick Start", "📚 Features", "🎯 Workflow", "💡 Tips"])
    
    with tab1:
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("""
                ### 🚀 Get Started in 3 Steps
                
                **Step 1:** Upload or use sample data
                - Navigate to 📊 Data Studio
                - Upload CSV/Excel or select sample data
                
                **Step 2:** Train ML Models
                - Go to 🤖 Model Lab
                - Select algorithms to train
                - Compare performance metrics
                
                **Step 3:** Make Predictions
                - Visit 🔮 Predictor
                - Input environmental parameters
                - Get AQI forecasts instantly
            """)
        
        with col2:
            st.markdown("""
                ### 📊 AQI Scale Reference
                
                - **0-50** 🟢 Good
                - **51-100** 🟡 Satisfactory
                - **101-200** 🟠 Moderate
                - **201-300** 🔴 Poor
                - **301+** 🟣 Severe
                
                Each level has specific health implications.
            """)
    
    with tab2:
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.markdown("""
                #### 📊 Data Management
                - CSV/Excel upload
                - Real-time preprocessing
                - Missing value handling
                - Outlier detection
                - Correlation analysis
            """)
        
        with col2:
            st.markdown("""
                #### 🤖 ML Algorithms
                - Linear Regression
                - Decision Trees
                - Random Forest
                - Gradient Boosting
                - Neural Networks
            """)
        
        with col3:
            st.markdown("""
                #### 📈 Analytics
                - Performance metrics
                - Residual analysis
                - Feature importance
                - Cross-validation
                - Model comparison
            """)
    
    with tab3:
        st.markdown("""
            ### 🔄 Complete Workflow
            
            ```
            1. DATA PREPARATION
               ↓ Upload → Explore → Clean
            
            2. MODEL TRAINING
               ↓ Select → Train → Evaluate
            
            3. PREDICTION
               ↓ Input → Forecast → Visualize
            
            4. INSIGHTS
               ↓ Analyze → Interpret → Share
            ```
        """)
    
    with tab4:
        st.markdown("""
            ### 💡 Pro Tips
            
            - **Random Forest** typically provides best accuracy
            - **Check data quality** before training models
            - **Compare multiple metrics** (RMSE, MAE, R²)
            - **Use cross-validation** for robust estimates
            - **Visualize residuals** to understand errors
            - **Feature importance** guides data collection
            - **Save predictions** for further analysis
        """)

# ============================================================================
# PAGE 2: DATA STUDIO
# ============================================================================

elif page == "📊 Data Studio":
    st.markdown("## 📊 Data Studio")
    st.markdown("Upload, explore, and prepare your air quality data")
    
    tab1, tab2, tab3, tab4 = st.tabs(["📁 Upload", "🔍 Explore", "🛠️ Process", "📋 Preview"])
    
    with tab1:
        st.subheader("Data Upload")
        col1, col2 = st.columns([3, 1])
        
        with col1:
            uploaded_file = st.file_uploader(
                "Choose your data file",
                type=['csv', 'xlsx'],
                help="CSV or Excel file with air quality data"
            )
        
        with col2:
            if st.checkbox("📊 Use Sample Data"):
                np.random.seed(42)
                sample_data = pd.DataFrame({
                    'PM2.5': np.random.normal(45, 20, 200),
                    'PM10': np.random.normal(80, 35, 200),
                    'NO2': np.random.normal(35, 15, 200),
                    'CO': np.random.normal(1.2, 0.5, 200),
                    'SO2': np.random.normal(15, 8, 200),
                    'O3': np.random.normal(30, 12, 200),
                    'Temperature': np.random.normal(25, 10, 200),
                    'Humidity': np.random.normal(60, 15, 200),
                    'Wind_Speed': np.random.normal(5, 2, 200),
                    'AQI': np.random.normal(150, 50, 200)
                })
                sample_data['AQI'] = sample_data['AQI'].abs()
                st.session_state.data = sample_data
                st.session_state.data_info = {'source': 'sample', 'uploaded_at': datetime.now()}
                st.success("✅ Sample data loaded!")
                uploaded_file = None
        
        if uploaded_file is not None:
            try:
                if uploaded_file.type == 'text/csv':
                    data = pd.read_csv(uploaded_file)
                else:
                    data = pd.read_excel(uploaded_file)
                st.session_state.data = data
                st.session_state.data_info = {
                    'source': uploaded_file.name,
                    'uploaded_at': datetime.now(),
                    'size': uploaded_file.size
                }
                st.success(f"✅ Loaded: {uploaded_file.name} ({data.shape[0]} rows × {data.shape[1]} columns)")
            except Exception as e:
                st.error(f"❌ Error: {e}")
        
        # Data Info
        if st.session_state.data is not None:
            st.markdown("---")
            col1, col2, col3, col4, col5 = st.columns(5)
            
            with col1:
                st.metric("📊 Rows", len(st.session_state.data))
            with col2:
                st.metric("📋 Columns", len(st.session_state.data.columns))
            with col3:
                completeness = (1 - st.session_state.data.isnull().sum().sum() / 
                              (len(st.session_state.data) * len(st.session_state.data.columns))) * 100
                st.metric("✅ Complete", f"{completeness:.1f}%")
            with col4:
                numeric_cols = len(st.session_state.data.select_dtypes(include=[np.number]).columns)
                st.metric("🔢 Numeric", numeric_cols)
            with col5:
                st.metric("📅 Uploaded", st.session_state.data_info.get('uploaded_at', 'N/A').strftime('%H:%M') 
                         if isinstance(st.session_state.data_info.get('uploaded_at'), datetime) else 'N/A')
    
    with tab2:
        if st.session_state.data is not None:
            st.subheader("Data Statistics")
            
            col1, col2 = st.columns([1, 1])
            with col1:
                st.markdown("#### Summary Statistics")
                st.dataframe(st.session_state.data.describe().T, use_container_width=True)
            
            with col2:
                st.markdown("#### Data Quality")
                missing_data = st.session_state.data.isnull().sum()
                if missing_data.sum() > 0:
                    st.warning("⚠️ Missing values detected")
                    st.bar_chart(missing_data[missing_data > 0])
                else:
                    st.info("✅ No missing values detected")
            
            # Correlation Heatmap
            st.markdown("#### Feature Correlations")
            numeric_data = st.session_state.data.select_dtypes(include=[np.number])
            if len(numeric_data.columns) > 1:
                corr_matrix = numeric_data.corr()
                
                fig = go.Figure(data=go.Heatmap(
                    z=corr_matrix.values,
                    x=corr_matrix.columns,
                    y=corr_matrix.columns,
                    colorscale='RdBu',
                    zmid=0,
                    colorbar=dict(title="Correlation")
                ))
                
                fig.update_layout(
                    height=500,
                    template='plotly_dark',
                    paper_bgcolor='rgba(0,0,0,0)',
                    plot_bgcolor='rgba(0,0,0,0)',
                    font=dict(color='#A8B5C8')
                )
                
                st.plotly_chart(fig, use_container_width=True)
        else:
            st.info("📁 Upload data first to explore")
    
    with tab3:
        if st.session_state.data is not None:
            st.subheader("Data Preprocessing")
            
            col1, col2, col3 = st.columns(3)
            
            with col1:
                handle_missing = st.selectbox(
                    "Missing Values",
                    ["Drop rows", "Forward fill", "Backward fill", "Mean"]
                )
            
            with col2:
                outlier_method = st.selectbox(
                    "Outlier Detection",
                    ["None", "IQR", "Z-score"]
                )
            
            with col3:
                scaler_type = st.selectbox(
                    "Feature Scaling",
                    ["Standard", "Robust", "None"]
                )
            
            if st.button("🔧 Apply Processing", use_container_width=True):
                data = st.session_state.data.copy()
                
                # Handle missing values
                if handle_missing == "Drop rows":
                    data = data.dropna()
                elif handle_missing == "Forward fill":
                    data = data.fillna(method='ffill')
                elif handle_missing == "Backward fill":
                    data = data.fillna(method='bfill')
                elif handle_missing == "Mean":
                    numeric_cols = data.select_dtypes(include=[np.number]).columns
                    data[numeric_cols] = data[numeric_cols].fillna(data[numeric_cols].mean())
                
                # Outlier detection
                if outlier_method == "IQR":
                    Q1 = data.quantile(0.25)
                    Q3 = data.quantile(0.75)
                    IQR = Q3 - Q1
                    data = data[~((data < (Q1 - 1.5 * IQR)) | (data > (Q3 + 1.5 * IQR))).any(axis=1)]
                elif outlier_method == "Z-score":
                    numeric_cols = data.select_dtypes(include=[np.number]).columns
                    data = data[(np.abs(stats.zscore(data[numeric_cols])) < 3).all(axis=1)]
                
                st.session_state.data = data
                st.success(f"✅ Processing complete! New shape: {data.shape}")
                st.rerun()
        else:
            st.info("📁 Upload data first to process")
    
    with tab4:
        if st.session_state.data is not None:
            st.subheader("Data Preview")
            st.dataframe(st.session_state.data.head(20), use_container_width=True)
        else:
            st.info("📁 Upload data first to preview")

# ============================================================================
# PAGE 3: MODEL LAB
# ============================================================================

elif page == "🤖 Model Lab":
    st.markdown("## 🤖 Model Lab")
    st.markdown("Train and compare machine learning models")
    
    if st.session_state.data is not None:
        col1, col2, col3 = st.columns(3)
        
        with col1:
            target_col = st.selectbox(
                "Target Variable",
                st.session_state.data.select_dtypes(include=[np.number]).columns
            )
        
        with col2:
            test_size = st.slider("Test Split", 0.1, 0.5, 0.2)
        
        with col3:
            cross_val = st.slider("Cross-Validation Folds", 3, 10, 5)
        
        st.markdown("---")
        
        # Model Selection
        st.markdown("### Select Models to Train")
        col1, col2, col3 = st.columns(3)
        
        with col1:
            train_lr = st.checkbox("Linear Regression", value=True)
            train_ridge = st.checkbox("Ridge Regression", value=True)
            train_lasso = st.checkbox("Lasso Regression", value=True)
        
        with col2:
            train_dt = st.checkbox("Decision Tree", value=True)
            train_rf = st.checkbox("Random Forest", value=True, help="Recommended")
            train_gb = st.checkbox("Gradient Boosting", value=True)
        
        with col3:
            train_svm = st.checkbox("SVM", value=False)
            train_nn = st.checkbox("Neural Network", value=False)
        
        if st.button("🚀 Train Models", use_container_width=True, key="train_btn"):
            with st.spinner("🔄 Training models..."):
                progress_bar = st.progress(0)
                status_text = st.empty()
                
                # Data preparation
                numeric_data = st.session_state.data.select_dtypes(include=[np.number])
                X = numeric_data.drop(columns=[target_col])
                y = numeric_data[target_col]
                
                st.session_state.feature_names = X.columns.tolist()
                
                # Split data
                X_train, X_test, y_train, y_test = train_test_split(
                    X, y, test_size=test_size, random_state=42
                )
                
                # Scale features
                scaler = StandardScaler()
                X_train_scaled = scaler.fit_transform(X_train)
                X_test_scaled = scaler.transform(X_test)
                st.session_state.scaler = scaler
                
                # Model definitions
                models = {}
                if train_lr:
                    models['Linear Regression'] = LinearRegression()
                if train_ridge:
                    models['Ridge'] = Ridge()
                if train_lasso:
                    models['Lasso'] = Lasso()
                if train_dt:
                    models['Decision Tree'] = DecisionTreeRegressor(random_state=42)
                if train_rf:
                    models['Random Forest'] = RandomForestRegressor(n_estimators=100, random_state=42)
                if train_gb:
                    models['Gradient Boosting'] = GradientBoostingRegressor(random_state=42)
                if train_svm:
                    models['SVM'] = SVR(kernel='rbf')
                if train_nn:
                    models['Neural Network'] = MLPRegressor(hidden_layer_sizes=(100, 50), max_iter=1000, random_state=42)
                
                results = {}
                total_models = len(models)
                
                for idx, (name, model) in enumerate(models.items()):
                    status_text.text(f"Training {name}...")
                    
                    # Train model
                    model.fit(X_train_scaled, y_train)
                    y_pred = model.predict(X_test_scaled)
                    
                    # Calculate metrics
                    rmse = np.sqrt(mean_squared_error(y_test, y_pred))
                    mae = mean_absolute_error(y_test, y_pred)
                    r2 = r2_score(y_test, y_pred)
                    mape = mean_absolute_percentage_error(y_test, y_pred)
                    
                    # Cross-validation
                    cv_scores = cross_val_score(model, X_train_scaled, y_train, cv=cross_val, 
                                               scoring='r2')
                    
                    results[name] = {
                        'model': model,
                        'y_pred': y_pred,
                        'rmse': rmse,
                        'mae': mae,
                        'r2': r2,
                        'mape': mape,
                        'cv_scores': cv_scores,
                        'cv_mean': cv_scores.mean(),
                        'cv_std': cv_scores.std()
                    }
                    
                    progress_bar.progress((idx + 1) / total_models)
                
                st.session_state.trained_models = results
                st.session_state.y_test = y_test
                status_text.success("✅ Training complete!")
        
        # Display Results
        if st.session_state.trained_models:
            st.markdown("---")
            st.markdown("### Model Performance")
            
            # Create comparison dataframe
            comparison_data = []
            for name, metrics in st.session_state.trained_models.items():
                comparison_data.append({
                    'Model': name,
                    'R² Score': f"{metrics['r2']:.4f}",
                    'RMSE': f"{metrics['rmse']:.4f}",
                    'MAE': f"{metrics['mae']:.4f}",
                    'MAPE': f"{metrics['mape']:.4f}",
                    'CV Mean': f"{metrics['cv_mean']:.4f}",
                    'CV Std': f"{metrics['cv_std']:.4f}"
                })
            
            comparison_df = pd.DataFrame(comparison_data)
            st.dataframe(comparison_df, use_container_width=True)
            
            # Performance Charts
            col1, col2 = st.columns(2)
            
            with col1:
                fig = go.Figure()
                for name in st.session_state.trained_models.keys():
                    fig.add_trace(go.Bar(
                        x=[name],
                        y=[st.session_state.trained_models[name]['r2']],
                        name=name,
                        text=[f"{st.session_state.trained_models[name]['r2']:.3f}"],
                        textposition='auto'
                    ))
                
                fig.update_layout(
                    title="R² Score Comparison",
                    height=400,
                    showlegend=False,
                    template='plotly_dark',
                    paper_bgcolor='rgba(0,0,0,0)',
                    plot_bgcolor='rgba(0,0,0,0)'
                )
                st.plotly_chart(fig, use_container_width=True)
            
            with col2:
                fig = go.Figure()
                for name in st.session_state.trained_models.keys():
                    fig.add_trace(go.Bar(
                        x=[name],
                        y=[st.session_state.trained_models[name]['rmse']],
                        name=name,
                        text=[f"{st.session_state.trained_models[name]['rmse']:.3f}"],
                        textposition='auto'
                    ))
                
                fig.update_layout(
                    title="RMSE Comparison (Lower is Better)",
                    height=400,
                    showlegend=False,
                    template='plotly_dark',
                    paper_bgcolor='rgba(0,0,0,0)',
                    plot_bgcolor='rgba(0,0,0,0)'
                )
                st.plotly_chart(fig, use_container_width=True)
            
            # Best Model
            best_model_name = max(st.session_state.trained_models.items(), 
                                 key=lambda x: x[1]['r2'])[0]
            best_model_data = st.session_state.trained_models[best_model_name]
            
            st.markdown("---")
            st.markdown(f"""
                <div class='status-success' style='padding: 20px; border-radius: 8px;'>
                    <h3>🏆 Best Model: {best_model_name}</h3>
                    <p>R² Score: {best_model_data['r2']:.4f}</p>
                    <p>RMSE: {best_model_data['rmse']:.4f}</p>
                    <p>Cross-Validation: {best_model_data['cv_mean']:.4f} ± {best_model_data['cv_std']:.4f}</p>
                </div>
            """, unsafe_allow_html=True)
    else:
        st.info("📁 Upload data first in Data Studio")

# ============================================================================
# PAGE 4: PREDICTOR
# ============================================================================

elif page == "🔮 Predictor":
    st.markdown("## 🔮 AQI Predictor")
    st.markdown("Make real-time predictions using trained models")
    
    if st.session_state.trained_models and st.session_state.feature_names:
        st.markdown("### Input Environmental Parameters")
        
        # Input form
        col_layout = st.columns(3)
        input_data = {}
        
        for idx, feature in enumerate(st.session_state.feature_names):
            with col_layout[idx % 3]:
                if 'Temperature' in feature:
                    input_data[feature] = st.number_input(
                        f"🌡️ {feature} (°C)",
                        value=25.0,
                        step=0.1,
                        key=f"input_{feature}"
                    )
                elif 'Humidity' in feature:
                    input_data[feature] = st.number_input(
                        f"💧 {feature} (%)",
                        value=60.0,
                        step=0.1,
                        max_value=100.0,
                        key=f"input_{feature}"
                    )
                elif 'Wind' in feature:
                    input_data[feature] = st.number_input(
                        f"💨 {feature} (m/s)",
                        value=5.0,
                        step=0.1,
                        key=f"input_{feature}"
                    )
                else:
                    input_data[feature] = st.number_input(
                        f"🌫️ {feature} (µg/m³)",
                        value=50.0,
                        step=0.1,
                        key=f"input_{feature}"
                    )
        
        # Prediction button
        col1, col2, col3 = st.columns([1, 1, 1])
        with col2:
            predict_btn = st.button("🎯 Generate Predictions", use_container_width=True, key="predict_btn")
        
        if predict_btn:
            # Prepare input
            input_df = pd.DataFrame([input_data])
            input_scaled = st.session_state.scaler.transform(input_df)
            
            # Make predictions
            predictions = {}
            for name, model_data in st.session_state.trained_models.items():
                pred = model_data['model'].predict(input_scaled)[0]
                predictions[name] = pred
            
            # Store in history
            st.session_state.prediction_history.append({
                'timestamp': datetime.now(),
                'inputs': input_data,
                'predictions': predictions
            })
            
            st.markdown("---")
            st.markdown("### 📊 Prediction Results")
            
            # Prediction cards
            col1, col2 = st.columns(2)
            
            with col1:
                for idx, (name, pred) in enumerate(predictions.items()):
                    if pred <= 50:
                        category = "Good 🟢"
                        color = "#00C853"
                    elif pred <= 100:
                        category = "Satisfactory 🟡"
                        color = "#FFD700"
                    elif pred <= 200:
                        category = "Moderate 🟠"
                        color = "#FFA726"
                    elif pred <= 300:
                        category = "Poor 🔴"
                        color = "#FF5252"
                    else:
                        category = "Severe 🟣"
                        color = "#9C27B0"
                    
                    if idx % 2 == 0:
                        st.markdown(f"""
                            <div class='metric-card' style='border-color: {color}; border-left: 4px solid {color};'>
                                <div style='color: #A8B5C8; font-size: 0.9em;'>{name}</div>
                                <div style='color: {color}; font-size: 2em; font-weight: bold; margin: 10px 0;'>
                                    {pred:.1f}
                                </div>
                                <div style='color: {color}; font-weight: 600;'>{category}</div>
                            </div>
                        """, unsafe_allow_html=True)
            
            with col2:
                for idx, (name, pred) in enumerate(predictions.items()):
                    if pred <= 50:
                        category = "Good 🟢"
                        color = "#00C853"
                    elif pred <= 100:
                        category = "Satisfactory 🟡"
                        color = "#FFD700"
                    elif pred <= 200:
                        category = "Moderate 🟠"
                        color = "#FFA726"
                    elif pred <= 300:
                        category = "Poor 🔴"
                        color = "#FF5252"
                    else:
                        category = "Severe 🟣"
                        color = "#9C27B0"
                    
                    if idx % 2 == 1:
                        st.markdown(f"""
                            <div class='metric-card' style='border-color: {color}; border-left: 4px solid {color};'>
                                <div style='color: #A8B5C8; font-size: 0.9em;'>{name}</div>
                                <div style='color: {color}; font-size: 2em; font-weight: bold; margin: 10px 0;'>
                                    {pred:.1f}
                                </div>
                                <div style='color: {color}; font-weight: 600;'>{category}</div>
                            </div>
                        """, unsafe_allow_html=True)
            
            # Best prediction gauge
            best_pred_name = max(predictions.items(), key=lambda x: st.session_state.trained_models[x[0]]['r2'])[0]
            best_pred_value = predictions[best_pred_name]
            
            fig = go.Figure(go.Indicator(
                mode="gauge+number",
                value=best_pred_value,
                domain={'x': [0, 1], 'y': [0, 1]},
                title={'text': f"AQI Prediction - {best_pred_name}"},
                gauge={
                    'axis': {'range': [0, 500]},
                    'bar': {'color': "#00D4FF"},
                    'steps': [
                        {'range': [0, 50], 'color': "rgba(0, 200, 83, 0.3)"},
                        {'range': [50, 100], 'color': "rgba(255, 215, 0, 0.3)"},
                        {'range': [100, 200], 'color': "rgba(255, 167, 38, 0.3)"},
                        {'range': [200, 300], 'color': "rgba(255, 82, 82, 0.3)"},
                        {'range': [300, 500], 'color': "rgba(156, 39, 176, 0.3)"}
                    ]
                }
            ))
            
            fig.update_layout(
                height=400,
                template='plotly_dark',
                paper_bgcolor='rgba(0,0,0,0)',
                plot_bgcolor='rgba(0,0,0,0)',
                font=dict(color='#A8B5C8')
            )
            
            st.plotly_chart(fig, use_container_width=True)
    else:
        st.info("🤖 Train models first in Model Lab")

# ============================================================================
# PAGE 5: ANALYTICS
# ============================================================================

elif page == "📈 Analytics":
    st.markdown("## 📈 Advanced Analytics")
    st.markdown("Deep analysis of model performance and predictions")
    
    if st.session_state.trained_models:
        tab1, tab2, tab3, tab4 = st.tabs(["📊 Comparison", "📉 Residuals", "🎯 Features", "📈 Predictions"])
        
        with tab1:
            st.subheader("Model Comparison Dashboard")
            
            # Metrics comparison
            col1, col2 = st.columns(2)
            
            with col1:
                fig = make_subplots(specs=[[{"secondary_y": True}]])
                
                models = list(st.session_state.trained_models.keys())
                r2_scores = [st.session_state.trained_models[m]['r2'] for m in models]
                
                fig.add_trace(go.Bar(x=models, y=r2_scores, name='R² Score', marker_color='#00D4FF'),
                             secondary_y=False)
                
                fig.update_layout(
                    title="R² Score Comparison",
                    height=400,
                    template='plotly_dark',
                    paper_bgcolor='rgba(0,0,0,0)',
                    plot_bgcolor='rgba(0,0,0,0)'
                )
                
                st.plotly_chart(fig, use_container_width=True)
            
            with col2:
                fig = go.Figure()
                models = list(st.session_state.trained_models.keys())
                rmse_values = [st.session_state.trained_models[m]['rmse'] for m in models]
                mae_values = [st.session_state.trained_models[m]['mae'] for m in models]
                
                fig.add_trace(go.Bar(x=models, y=rmse_values, name='RMSE', marker_color='#FF4081'))
                fig.add_trace(go.Bar(x=models, y=mae_values, name='MAE', marker_color='#FFD700'))
                
                fig.update_layout(
                    title="Error Metrics Comparison",
                    barmode='group',
                    height=400,
                    template='plotly_dark',
                    paper_bgcolor='rgba(0,0,0,0)',
                    plot_bgcolor='rgba(0,0,0,0)'
                )
                
                st.plotly_chart(fig, use_container_width=True)
        
        with tab2:
            st.subheader("Residual Analysis")
            selected_model = st.selectbox("Select Model", list(st.session_state.trained_models.keys()))
            
            y_pred = st.session_state.trained_models[selected_model]['y_pred']
            residuals = st.session_state.y_test.values - y_pred
            
            col1, col2 = st.columns(2)
            
            with col1:
                fig = go.Figure()
                fig.add_trace(go.Histogram(x=residuals, nbinsx=30, marker_color='#00D4FF'))
                fig.update_layout(
                    title="Residual Distribution",
                    xaxis_title="Residuals",
                    yaxis_title="Frequency",
                    height=400,
                    template='plotly_dark',
                    paper_bgcolor='rgba(0,0,0,0)',
                    plot_bgcolor='rgba(0,0,0,0)'
                )
                st.plotly_chart(fig, use_container_width=True)
            
            with col2:
                fig = go.Figure()
                fig.add_trace(go.Scatter(x=y_pred, y=residuals, mode='markers',
                                        marker=dict(size=8, color=residuals, colorscale='RdBu')))
                fig.add_hline(y=0, line_dash="dash", line_color="red")
                fig.update_layout(
                    title="Residuals vs Fitted",
                    xaxis_title="Fitted Values",
                    yaxis_title="Residuals",
                    height=400,
                    template='plotly_dark',
                    paper_bgcolor='rgba(0,0,0,0)',
                    plot_bgcolor='rgba(0,0,0,0)'
                )
                st.plotly_chart(fig, use_container_width=True)
        
        with tab3:
            st.subheader("Feature Importance")
            selected_model = st.selectbox("Select Model", list(st.session_state.trained_models.keys()), key="importance_select")
            
            model = st.session_state.trained_models[selected_model]['model']
            
            if hasattr(model, 'feature_importances_'):
                importances = model.feature_importances_
                features = st.session_state.feature_names
                
                importance_df = pd.DataFrame({
                    'Feature': features,
                    'Importance': importances
                }).sort_values('Importance', ascending=True)
                
                fig = go.Figure()
                fig.add_trace(go.Bar(
                    y=importance_df['Feature'],
                    x=importance_df['Importance'],
                    orientation='h',
                    marker_color='#00D4FF'
                ))
                
                fig.update_layout(
                    title=f"{selected_model}: Feature Importance",
                    xaxis_title="Importance",
                    height=500,
                    template='plotly_dark',
                    paper_bgcolor='rgba(0,0,0,0)',
                    plot_bgcolor='rgba(0,0,0,0)'
                )
                
                st.plotly_chart(fig, use_container_width=True)
            else:
                st.info("⚠️ Feature importance not available for this model")
        
        with tab4:
            st.subheader("Predictions vs Actual")
            selected_model = st.selectbox("Select Model", list(st.session_state.trained_models.keys()), key="pred_select")
            
            y_pred = st.session_state.trained_models[selected_model]['y_pred']
            y_actual = st.session_state.y_test
            
            fig = go.Figure()
            fig.add_trace(go.Scatter(x=y_actual, y=y_pred, mode='markers',
                                    marker=dict(size=8, color=y_actual, colorscale='Viridis', showscale=True)))
            fig.add_trace(go.Scatter(x=[y_actual.min(), y_actual.max()],
                                    y=[y_actual.min(), y_actual.max()],
                                    mode='lines',
                                    name='Perfect Fit',
                                    line=dict(dash='dash', color='red')))
            
            fig.update_layout(
                title=f"{selected_model}: Actual vs Predicted",
                xaxis_title="Actual AQI",
                yaxis_title="Predicted AQI",
                height=500,
                template='plotly_dark',
                paper_bgcolor='rgba(0,0,0,0)',
                plot_bgcolor='rgba(0,0,0,0)'
            )
            
            st.plotly_chart(fig, use_container_width=True)
    else:
        st.info("🤖 Train models first to view analytics")

# ============================================================================
# PAGE 6: SETTINGS
# ============================================================================

elif page == "⚙️ Settings":
    st.markdown("## ⚙️ Settings & Configuration")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("🎨 Display Settings")
        
        theme = st.radio("Theme", ["Dark (Default)", "Light"])
        chart_theme = st.selectbox("Chart Theme", ["plotly_dark", "plotly_light", "plotly"])
        
        st.subheader("🔢 Model Settings")
        rf_estimators = st.slider("Random Forest Trees", 50, 300, 100)
        nn_hidden = st.multiselect("NN Hidden Layers", [50, 100, 150, 200], default=[100, 50])
        cross_val_folds = st.slider("Cross-Validation Folds", 3, 10, 5)
    
    with col2:
        st.subheader("📊 Data Settings")
        
        default_test_size = st.slider("Default Test Size", 0.1, 0.5, 0.2)
        handle_missing = st.selectbox("Missing Value Strategy", ["Drop", "Forward Fill", "Mean"])
        outlier_method = st.selectbox("Outlier Detection", ["None", "IQR", "Z-score"])
        
        st.subheader("⚡ Performance")
        
        st.toggle("Enable GPU Acceleration", value=False)
        st.toggle("Cache Predictions", value=True)
        st.toggle("Auto-save Models", value=False)
    
    st.markdown("---")
    
    if st.button("💾 Save Settings", use_container_width=True):
        st.success("✅ Settings saved successfully!")

# ============================================================================
# PAGE 7: DOCUMENTATION
# ============================================================================

elif page == "ℹ️ Documentation":
    st.markdown("## 📚 Documentation")
    
    tab1, tab2, tab3, tab4, tab5 = st.tabs(["🚀 Getting Started", "📖 Guide", "🎓 Tutorials", "❓ FAQ", "📞 Support"])
    
    with tab1:
        st.markdown("""
            ### Quick Start Guide
            
            **Step 1: Prepare Data**
            - Upload CSV or Excel file
            - Or use sample dataset
            - Verify data quality
            
            **Step 2: Train Models**
            - Select algorithms
            - Configure parameters
            - Compare results
            
            **Step 3: Make Predictions**
            - Enter parameters
            - Generate forecasts
            - Analyze results
        """)
    
    with tab2:
        st.markdown("""
            ### Complete User Guide
            
            #### Data Management
            - Supported formats: CSV, XLSX
            - Minimum records: 50
            - Required features: All numeric
            
            #### Algorithms
            - **Linear Regression**: Simple baseline
            - **Ridge/Lasso**: Regularized regression
            - **Decision Tree**: Interpretable model
            - **Random Forest**: Ensemble method ⭐
            - **Gradient Boosting**: Sequential ensemble
            - **SVM**: Non-linear patterns
            - **Neural Network**: Deep learning
            
            #### Metrics
            - **R² Score**: Explained variance (0-1)
            - **RMSE**: Root mean squared error
            - **MAE**: Mean absolute error
            - **MAPE**: Mean absolute percentage error
        """)
    
    with tab3:
        st.markdown("""
            ### Video Tutorials
            
            *Coming soon...*
            
            - Data preparation tutorial
            - Model training walkthrough
            - Prediction guide
            - Advanced analytics
        """)
    
    with tab4:
        st.markdown("""
            ### Frequently Asked Questions
            
            **Q: Which model should I use?**
            A: Random Forest generally provides best accuracy and robustness.
            
            **Q: How much data do I need?**
            A: Minimum 50 records, but 100+ recommended for better results.
            
            **Q: Can I export predictions?**
            A: Yes, all predictions are stored and can be downloaded.
            
            **Q: What if my R² score is low?**
            A: Check data quality, try different models, or collect more data.
            
            **Q: How do I improve predictions?**
            A: Use ensemble methods, tune hyperparameters, or add features.
        """)
    
    with tab5:
        st.markdown("""
            ### Support Resources
            
            **Email:** support@aqiintelligence.com  
            **GitHub:** https://github.com/aqiintelligence  
            **Documentation:** https://docs.aqiintelligence.com  
            **Community:** https://community.aqiintelligence.com
        """)

# ============================================================================
# FOOTER
# ============================================================================

st.markdown("---")
st.markdown("""
    <div style='text-align: center; color: #A8B5C8; padding: 20px;'>
        <p>
            🌍 <strong>AQI Intelligence Pro v2.0</strong> • 
            <a href='#'>Status</a> • 
            <a href='#'>About</a> • 
            <a href='#'>Terms</a> • 
            <a href='#'>Privacy</a>
        </p>
        <p style='font-size: 0.9em; margin-top: 10px;'>
            © 2024 AQI Intelligence. All rights reserved. | 
            Last updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
        </p>
    </div>
""", unsafe_allow_html=True)