# 🌍 AQI Predictor Pro - Complete Streamlit Application

A comprehensive machine learning application for predicting Air Quality Index (AQI) using multiple advanced algorithms with interactive visualizations and real-time predictions.

![Streamlit](https://img.shields.io/badge/Streamlit-1.28.1-FF4B4B?style=for-the-badge&logo=streamlit)
![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python)
![scikit-learn](https://img.shields.io/badge/scikit--learn-1.3.1-F7931E?style=for-the-badge&logo=scikit-learn)

## 📋 Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Quick Start](#quick-start)
- [Application Structure](#application-structure)
- [Data Requirements](#data-requirements)
- [Usage Guide](#usage-guide)
- [Machine Learning Models](#machine-learning-models)
- [AQI Health Impact Scale](#aqi-health-impact-scale)

---

## ✨ Features

### 🏠 Home Page
- Project overview and quick introduction
- Key features summary
- AQI health impact classification
- Quick start guide

### 📈 Data Preparation
- **Upload Data**: Support for CSV and Excel files
- **Sample Dataset**: Pre-loaded sample data for testing
- **Data Exploration**: 
  - Statistical summaries
  - Missing value detection
  - Correlation heatmap
- **Data Preprocessing**:
  - Handle missing values (drop, forward fill, backward fill, mean imputation)
  - Outlier detection (IQR method, Z-score)
  - Data quality visualization

### 🤖 Model Training
- Train multiple algorithms simultaneously
- **Supported Models**:
  - Linear Regression
  - Decision Tree Regressor
  - Random Forest (Recommended)
  - Support Vector Machine (SVM)
  - Neural Network (MLP)
- Performance comparison metrics
- Automatic feature scaling
- Train/test split configuration

### 🔮 Predictions
- Interactive parameter input interface
- Real-time AQI predictions from all trained models
- AQI classification (Good, Satisfactory, Moderately Polluted, Poor, Very Poor)
- Gauge chart visualization
- Unit-aware input fields

### 📊 Analysis
- **Predictions vs Actual**: Scatter plots with perfect prediction reference line
- **Residual Analysis**: Distribution and residual vs fitted plots
- **Feature Importance**: Visualization of feature contributions (for tree-based models)
- Model-specific insights

### ℹ️ About
- Technical stack information
- Key environmental variables
- Project objectives
- Model selection guide
- Usage instructions

---

## 🚀 Installation

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Step 1: Clone or Download
```bash
git clone <repository-url>
cd aqi-predictor-pro
```

### Step 2: Create Virtual Environment (Recommended)
```bash
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

---

## ⚡ Quick Start

### Run the Application
```bash
streamlit run app.py
```

The app will open in your default browser at `http://localhost:8501`

### First-Time Setup
1. **Home Page**: Read the overview and understand AQI health impacts
2. **Use Sample Data**: Click "Use Sample Dataset" in Data Preparation
3. **Train Models**: Go to Model Training and click "Train Selected Models"
4. **Make Predictions**: Use the Predictions tab to forecast AQI
5. **Analyze Results**: Review detailed metrics in the Analysis tab

---

## 📁 Application Structure

```
aqi-predictor-pro/
├── app.py                 # Main Streamlit application
├── requirements.txt       # Python dependencies
├── README.md             # This file
└── data/
    └── sample_data.csv   # (Optional) Sample dataset
```

---

## 📊 Data Requirements

### Required Columns
Your dataset should include the following features:

| Feature | Unit | Description |
|---------|------|-------------|
| PM2.5 | µg/m³ | Fine particulate matter |
| PM10 | µg/m³ | Coarse particulate matter |
| NO2 | µg/m³ or ppb | Nitrogen dioxide |
| CO | mg/m³ or ppm | Carbon monoxide |
| SO2 | µg/m³ | Sulfur dioxide |
| O3 | µg/m³ or ppb | Ozone |
| Temperature | °C or °F | Ambient temperature |
| Humidity | % | Relative humidity (0-100) |
| Wind_Speed | m/s or km/h | Wind speed |
| AQI | - | Target variable (Air Quality Index) |

### Data Format
- **File Types**: CSV or Excel (.xlsx)
- **Minimum Rows**: 50+ records recommended
- **Missing Values**: Can be handled automatically
- **Data Types**: All numeric values expected

### Sample Data Structure
```csv
PM2.5,PM10,NO2,CO,SO2,O3,Temperature,Humidity,Wind_Speed,AQI
45.2,82.1,32.5,1.2,14.3,28.5,24.5,65.2,5.1,145
48.5,85.3,35.2,1.4,15.1,30.2,25.1,62.5,4.8,152
...
```

---

## 📖 Usage Guide

### 1. Home Page (🏠 Home)
- Understand the project scope
- Learn about AQI health impacts
- Review application features

### 2. Data Preparation (📈 Data Preparation)

#### Upload Data Tab
- Click "Browse files" to upload CSV or Excel
- Or click "Use Sample Dataset" checkbox for demo data
- View basic statistics (rows, columns, completeness)

#### Data Exploration Tab
- View descriptive statistics (mean, std, min, max)
- Check for missing values
- Analyze feature correlations with interactive heatmap

#### Preprocessing Tab
- Select missing value handling method
- Choose outlier detection approach
- Click "Apply Preprocessing" to clean data

### 3. Model Training (🤖 Model Training)

1. Select target column (usually "AQI")
2. Configure test set size (default: 20%)
3. Set random state for reproducibility
4. Choose models to train (Random Forest recommended)
5. Click "Train Selected Models"
6. Review performance metrics comparison

**Performance Metrics**:
- **RMSE** (Root Mean Squared Error): Lower is better
- **MAE** (Mean Absolute Error): Lower is better
- **R² Score**: Higher is better (0-1 range, 1 is perfect)

### 4. Predictions (🔮 Predictions)

1. Enter environmental parameters in the input form
2. Values auto-adjust to appropriate units
3. Click "Predict AQI"
4. View predictions from all trained models
5. Check AQI category classification
6. Review gauge chart for best model

### 5. Analysis (📊 Analysis)

#### Predictions vs Actual Tab
- Shows how well predictions match actual values
- Perfect prediction line for reference
- Points above line = overprediction, below = underprediction

#### Residual Analysis Tab
- Histogram of prediction errors
- Residuals vs fitted values plot
- Indicates model bias and variance

#### Feature Importance Tab
- Shows which features most influence predictions
- Available for tree-based models only
- Guides feature engineering efforts

---

## 🤖 Machine Learning Models

### Linear Regression
- **Pros**: Fast, interpretable, low computational cost
- **Cons**: Assumes linear relationship, poor for complex patterns
- **Best For**: Quick baseline models, educational purposes

### Decision Tree
- **Pros**: Interpretable, handles non-linear relationships
- **Cons**: Prone to overfitting, unstable with data changes
- **Best For**: Understanding feature relationships

### Random Forest ⭐ (RECOMMENDED)
- **Pros**: High accuracy, robust, handles non-linearity, feature importance
- **Cons**: Less interpretable than single trees
- **Best For**: Production use, best overall performance

### Support Vector Machine (SVM)
- **Pros**: Powerful for complex patterns, works in high dimensions
- **Cons**: Slower training, requires proper scaling, hard to interpret
- **Best For**: Complex non-linear patterns, smaller datasets

### Neural Network (MLP)
- **Pros**: Can learn very complex patterns, flexible architecture
- **Cons**: Requires more data, longer training, hyperparameter tuning
- **Best For**: Large datasets, very non-linear relationships

---

## 🌡️ AQI Health Impact Scale

| AQI Range | Category | Health Impact | Recommendation |
|-----------|----------|---------------|-----------------|
| 0-50 | Good | No health risk | Enjoy outdoor activities |
| 51-100 | Satisfactory | Minor risk | Sensitive groups exercise caution |
| 101-200 | Moderately Polluted | Some affect sensitive groups | Sensitive groups limit outdoor exposure |
| 201-300 | Poor | Affects general public | Everyone should reduce outdoor exposure |
| 301+ | Very Poor | Health emergency | Avoid outdoor activities entirely |

---

## 🔧 Advanced Configuration

### Customize Model Parameters

Edit the following sections in `app.py`:

**Random Forest** (Line ~420):
```python
RandomForestRegressor(
    n_estimators=100,      # Number of trees (increase for better accuracy)
    max_depth=None,        # Tree depth (limit to prevent overfitting)
    min_samples_split=2,   # Minimum samples to split a node
    random_state=random_state
)
```

**Neural Network** (Line ~424):
```python
MLPRegressor(
    hidden_layer_sizes=(100, 50),  # Hidden layers architecture
    max_iter=1000,                  # Maximum iterations
    learning_rate='adaptive',       # Learning rate schedule
    random_state=random_state
)
```

### Customize Styling

Modify CSS variables in the custom CSS section (Lines 30-35):
```python
--primary-color: #00D9FF;        # Main accent color
--secondary-color: #FF6B9D;      # Secondary accent
--accent-color: #FFD700;         # Highlight color
--dark-bg: #0F1419;              # Background color
```

---

## 📈 Performance Tips

1. **Data Quality**: Clean data leads to better predictions
2. **Feature Selection**: Use relevant environmental variables
3. **Sample Size**: Minimum 100+ records recommended
4. **Scaling**: App automatically scales features
5. **Model Selection**: Random Forest typically performs best for AQI

---

## 🐛 Troubleshooting

### Issue: "Module not found" error
```bash
# Solution: Ensure all dependencies are installed
pip install -r requirements.txt
```

### Issue: App runs slowly
- Reduce dataset size for initial testing
- Close other applications
- Increase Random Forest `n_estimators` carefully

### Issue: Poor model performance
- Check data quality for outliers
- Ensure sufficient data samples
- Verify feature ranges are reasonable
- Try preprocessing with outlier removal

### Issue: File upload fails
- Ensure CSV/Excel format
- Check for UTF-8 encoding
- Verify column names contain no special characters

---

## 📚 References

- [Streamlit Documentation](https://docs.streamlit.io/)
- [scikit-learn Documentation](https://scikit-learn.org/)
- [Plotly Documentation](https://plotly.com/python/)
- [AQI Guidelines](https://www.epa.gov/air-quality-standards)

---

## 📝 License

This project is provided as-is for educational and research purposes.

---

## 👨‍💻 Development

### Built With
- **Streamlit**: Interactive web application framework
- **scikit-learn**: Machine learning library
- **Plotly**: Interactive visualization
- **pandas**: Data manipulation
- **NumPy**: Numerical computing

### Version History
- **v1.0.0** (2024): Initial release with 5 ML algorithms

---

## 💡 Future Enhancements

- [ ] LSTM/RNN models for time-series forecasting
- [ ] Ensemble predictions combining multiple models
- [ ] Model export/save functionality
- [ ] Batch predictions from CSV
- [ ] Advanced hyperparameter tuning UI
- [ ] Cross-validation analysis
- [ ] Data visualization dashboard
- [ ] REST API integration

---

## 📞 Support

For issues or questions:
1. Check the Troubleshooting section
2. Review the About page for technical details
3. Check sample dataset format
4. Ensure data column names match requirements

---

## 🎯 Key Takeaways

✅ **Easy to Use**: Intuitive interface for all skill levels
✅ **Comprehensive**: Complete ML workflow from data to predictions
✅ **Accurate**: Multiple algorithms for optimal results
✅ **Interactive**: Real-time visualizations and feedback
✅ **Educational**: Learn about AQI prediction and ML

---

**Made with ❤️ for environmental science and machine learning enthusiasts**
