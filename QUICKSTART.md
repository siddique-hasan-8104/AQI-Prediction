# 🚀 AQI Predictor Pro - Quick Start Guide

Welcome! This guide will get you up and running in 5 minutes.

## ⏱️ 5-Minute Quick Start

### Step 1: Install (2 minutes)
```bash
# Install dependencies
pip install -r requirements.txt
```

### Step 2: Run (30 seconds)
```bash
# Start the application
streamlit run app.py
```
The app opens automatically at `http://localhost:8501`

### Step 3: Use Sample Data (1 minute)
1. Navigate to **📈 Data Preparation**
2. Click the **"Use Sample Dataset"** checkbox
3. See the data load instantly

### Step 4: Train Models (1 minute)
1. Go to **🤖 Model Training**
2. Select models (all selected by default)
3. Click **"🚀 Train Selected Models"**
4. Wait for training to complete

### Step 5: Make Predictions (30 seconds)
1. Visit **🔮 Predictions**
2. Adjust the environmental parameters (optional)
3. Click **"🎯 Predict AQI"**
4. See predictions from all models!

---

## 🎯 Common Tasks

### Task 1: Upload Your Own Data
```
1. Prepare CSV with columns: PM2.5, PM10, NO2, CO, SO2, O3, Temperature, Humidity, Wind_Speed, AQI
2. Data Preparation → Upload Data → Choose your file
3. Click "View Raw Data" to verify
```

### Task 2: Find the Best Model
```
1. Train all 5 models in Model Training
2. Compare RMSE, MAE, and R² scores
3. Random Forest usually wins! 🏆
4. Use it for production predictions
```

### Task 3: Understand Model Performance
```
1. Go to Analysis tab
2. Select "Predictions vs Actual"
3. Points near the diagonal = good predictions
4. Check "Residual Analysis" for error patterns
```

### Task 4: See Feature Importance
```
1. Analysis → Feature Importance
2. Select a tree-based model (Random Forest recommended)
3. See which pollutants matter most
4. PM2.5 usually most important!
```

### Task 5: Clean Bad Data
```
1. Data Preparation → Preprocessing
2. Choose "Drop rows" for missing values
3. Choose "IQR method" for outliers
4. Click "Apply Preprocessing"
```

---

## 💡 Tips & Tricks

### Tip 1: Test Different Parameters
In Predictions tab, try extreme values:
- Very high pollution: PM2.5 = 200, PM10 = 300
- Clean air: PM2.5 = 10, PM10 = 20
- See how predictions change!

### Tip 2: Compare Models Visually
Model Training shows bar charts comparing:
- RMSE (Root Mean Squared Error)
- MAE (Mean Absolute Error)
- R² Score (explained variance)
Shorter bars and taller R² bars = better!

### Tip 3: Check Data Quality First
Data Exploration tab shows:
- Missing values percentage
- Feature correlations (heatmap)
- Statistical summaries
Always review before training!

### Tip 4: Use Sample Data for Learning
The pre-loaded sample dataset:
- Has realistic AQI values
- Shows all feature relationships
- Perfect for testing all features
- Quick to train on!

### Tip 5: Understand AQI Levels
When predictions show:
- **0-50**: Enjoy outdoor activities 🌞
- **51-100**: Sensitive groups exercise caution ⚠️
- **101-200**: Limit outdoor time ⚠️⚠️
- **201-300**: Avoid outdoors ⛔
- **301+**: Health emergency 🚨

---

## 🎓 Understanding the Models

### Linear Regression 📈
- **Speed**: ⚡ Very Fast
- **Accuracy**: 🎯 Good for simple patterns
- **Interpretability**: 📖 Easy to understand
- **When to use**: Quick baselines, small data

### Decision Tree 🌳
- **Speed**: ⚡ Fast
- **Accuracy**: 🎯 Good for non-linear patterns
- **Interpretability**: 📖 Very interpretable
- **When to use**: Understanding relationships

### Random Forest ⭐ (RECOMMENDED)
- **Speed**: 🐢 Medium
- **Accuracy**: 🎯🎯🎯 Highest accuracy
- **Interpretability**: 📖 Good (can see feature importance)
- **When to use**: Production use, best all-around

### SVM 💪
- **Speed**: 🐢 Slow
- **Accuracy**: 🎯🎯 Excellent for complex patterns
- **Interpretability**: 📖 Hard to understand
- **When to use**: Complex non-linear relationships

### Neural Network 🧠
- **Speed**: 🐢 Slow
- **Accuracy**: 🎯🎯 Excellent with large data
- **Interpretability**: 📖 Very hard
- **When to use**: Very large datasets, complex patterns

---

## 🔧 Configuration Guide

### Change Default Parameters
Edit `app.py` line ~420:
```python
RandomForestRegressor(
    n_estimators=100,    # More = slower but more accurate
    max_depth=None,      # Limit to prevent overfitting
)
```

### Change Colors
Edit custom CSS section (lines 30-35):
```python
--primary-color: #00D9FF;        # Main color (change this!)
--secondary-color: #FF6B9D;      # Secondary
--accent-color: #FFD700;         # Highlight
```

### Add New Features
In `app.py`, add columns to your data:
```python
# Near line 180
input_data[feature] = st.number_input(...)
```

---

## ❓ FAQ

**Q: What if I get "Module not found"?**
A: Run `pip install -r requirements.txt` again

**Q: Why is my model performing poorly?**
A: Check data quality, ensure enough samples (100+), try different models

**Q: Can I use my own data?**
A: Yes! CSV or Excel with same columns as sample data

**Q: Which model should I use?**
A: Random Forest for best results! 🏆

**Q: How many samples do I need?**
A: 100+ records recommended, 50+ minimum

**Q: Can I save my trained models?**
A: Currently saved in session (add `joblib` code for persistence)

**Q: What's the difference between RMSE and MAE?**
A: RMSE penalizes large errors more; MAE is average error

**Q: How do I interpret R² score?**
A: 1.0 = perfect, 0.8+ = excellent, 0.5+ = okay

---

## 📊 Sample Workflow

### Example: Predict AQI for Beijing Data
```
1. Data Preparation → Use Sample Dataset
2. Data Exploration → Check correlations
3. Preprocessing → Remove outliers using IQR
4. Model Training → Train Random Forest
5. Predictions → Enter typical Beijing pollutant levels
6. Analysis → Review predictions vs actual
7. Conclusion → Model predicts with 0.85 R² score!
```

---

## 🚀 Advanced Features

### Feature Importance Analysis
- Random Forest shows which pollutants matter most
- PM2.5 typically most important
- Use for prioritizing monitoring efforts

### Residual Analysis
- Check if model has systematic bias
- Histogram should be centered at 0
- Points should be random in scatter plot

### Model Comparison
- Compare RMSE/MAE/R² across all models
- Best model = highest R², lowest RMSE/MAE
- Consider computational cost for production

---

## 🆘 Troubleshooting

| Problem | Solution |
|---------|----------|
| App won't start | `pip install streamlit` |
| No data loads | Check CSV format and column names |
| Models train slowly | Use sample data or smaller dataset first |
| Predictions seem wrong | Check input units match training data |
| Colors look weird | Restart app with `streamlit run app.py --logger.level=debug` |

---

## 📚 Next Steps

1. **Learn More**: Read full README.md
2. **Customize**: Edit colors, parameters in app.py
3. **Expand**: Add more ML algorithms
4. **Deploy**: Host on Streamlit Cloud (free!)
5. **Share**: Share link with colleagues

---

## 🎉 Congratulations!

You're now ready to predict AQI like a pro! 🌍

**Next Steps:**
- ✅ Explore all tabs
- ✅ Try different models
- ✅ Upload your own data
- ✅ Share results with your team

---

## 📞 Need Help?

- 📖 Read the full README.md
- 🔍 Check the About tab for technical details
- 💬 Review error messages carefully
- 🔧 Check configuration in config.ini

---

**Happy Predicting! 🎯**

Questions? Check the README.md or explore the app! The interface is designed to be self-explanatory.
