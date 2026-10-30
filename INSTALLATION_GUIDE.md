# 📦 Installation & Setup Guide for AQI Predictor Pro

## 🎯 Overview

This guide will walk you through:
1. **Installation** (5 minutes)
2. **First Run** (30 seconds)
3. **First Prediction** (3 minutes)

---

## ✅ Prerequisites Check

Before starting, verify you have:
- [ ] **Python 3.8 or higher** - Check: `python --version`
- [ ] **pip** (comes with Python) - Check: `pip --version`
- [ ] **Internet connection** (to download packages)
- [ ] **At least 500MB free disk space**
- [ ] **Any browser** (Chrome, Firefox, Safari, Edge)

### Check Your System

**Windows:**
```bash
python --version
pip --version
```

**macOS/Linux:**
```bash
python3 --version
pip3 --version
```

---

## 🚀 Installation Steps

### STEP 1️⃣: Download Project Files (30 seconds)

#### Option A: From This Interface
- Download all files to your computer
- Create a folder: `AQI-Predictor`
- Extract all files into this folder

#### Option B: Command Line (Advanced)
```bash
mkdir AQI-Predictor
cd AQI-Predictor
# Copy all files here
```

### STEP 2️⃣: Create Virtual Environment (1 minute)

Virtual environments isolate your project packages.

#### Windows:
```bash
# Navigate to your project folder
cd AQI-Predictor

# Create virtual environment
python -m venv venv

# Activate it
venv\Scripts\activate
```

#### macOS/Linux:
```bash
# Navigate to your project folder
cd AQI-Predictor

# Create virtual environment
python3 -m venv venv

# Activate it
source venv/bin/activate
```

**Success Check:** Your terminal should show `(venv)` at the start

### STEP 3️⃣: Install Dependencies (2-3 minutes)

```bash
# Make sure virtual environment is active (you should see (venv) in terminal)

# Install all required packages
pip install -r requirements.txt
```

**What gets installed:**
- ✅ Streamlit (web framework)
- ✅ scikit-learn (machine learning)
- ✅ pandas (data handling)
- ✅ NumPy (numerical computing)
- ✅ Plotly (visualizations)
- ✅ And more...

**Troubleshooting:**
```bash
# If you get permission errors, try:
pip install --user -r requirements.txt

# If you get module not found:
pip install -r requirements.txt --upgrade
```

### STEP 4️⃣: Verify Installation (30 seconds)

```bash
# Test Streamlit installation
streamlit --version

# Should show: Streamlit, version 1.28.1
```

---

## 🎬 First Run

### Launch the Application

```bash
# Make sure you're in the project folder
cd AQI-Predictor

# Make sure virtual environment is active (should see (venv))

# Run the application
streamlit run app.py
```

### What Happens Next:

1. **Terminal Output:**
```
  You can now view your Streamlit app in your browser.
  Local URL: http://localhost:8501
  Network URL: http://192.168.x.x:8501
```

2. **Browser Opens Automatically:**
   - If not, manually open: `http://localhost:8501`
   - You should see the home page with AQI Predictor Pro title

3. **Success! 🎉**
   - App is running
   - You're ready to make predictions

---

## 🏃 Quick First Prediction (3 minutes)

### 1️⃣ Go to Data Preparation
- Click on **"📈 Data Preparation"** in the left sidebar

### 2️⃣ Load Sample Data
- Check the box: **"📊 Use Sample Dataset"**
- Wait for "✅ Sample dataset loaded successfully!" message
- See 50 sample records loaded

### 3️⃣ Train a Model
- Click **"🤖 Model Training"** in the sidebar
- Keep default selections
- Click **"🚀 Train Selected Models"**
- Wait 5-10 seconds for training to complete

### 4️⃣ Make Predictions
- Click **"🔮 Predictions"** in the sidebar
- Adjust the environmental parameters (optional)
- Click **"🎯 Predict AQI"**
- 🎉 See your predictions!

---

## 🔧 Troubleshooting

### ❌ "Command not found: streamlit"
```bash
# Make sure virtual environment is active
# You should see (venv) at the start of your terminal line

# If not, activate it:
# Windows:
venv\Scripts\activate

# macOS/Linux:
source venv/bin/activate

# Then try again:
streamlit run app.py
```

### ❌ "ModuleNotFoundError"
```bash
# Make sure you're in the right folder
cd AQI-Predictor

# Make sure virtual environment is active
# Reinstall requirements
pip install -r requirements.txt --upgrade
```

### ❌ "Address already in use"
The default port 8501 is busy. Try:
```bash
streamlit run app.py --server.port 8502
```
Then open: `http://localhost:8502`

### ❌ "Permission denied" (macOS/Linux)
```bash
# Change file permissions
chmod +x app.py

# Or install to user directory
pip install --user -r requirements.txt
```

### ❌ Browser doesn't open automatically
- Manually open: `http://localhost:8501`
- Or copy the URL from terminal output

### ❌ "Python version too old"
```bash
# Check Python version
python --version

# Need 3.8 or higher
# Download latest from python.org
```

---

## 📋 Folder Structure After Installation

```
AQI-Predictor/
├── venv/                          # Virtual environment (created)
├── app.py                         # Main application
├── requirements.txt               # Dependencies
├── README.md                      # Full documentation
├── QUICKSTART.md                 # Quick start guide
├── PROJECT_SUMMARY.md            # Detailed overview
├── INSTALLATION_GUIDE.md         # This file
├── config.ini                    # Configuration
└── sample_data.csv               # Test data
```

---

## 🎮 Using the Application

### First Time User Path:
1. **Home Tab** (Read overview)
2. **Data Preparation Tab** (Use sample data)
3. **Model Training Tab** (Train models)
4. **Predictions Tab** (Make predictions)
5. **Analysis Tab** (View results)

### With Your Own Data:
1. **Data Preparation Tab** (Upload CSV/Excel)
2. **Exploration Tab** (Check statistics)
3. **Preprocessing Tab** (Clean data)
4. **Model Training Tab** (Train models)
5. **Predictions Tab** (Make predictions)

---

## ⚡ Commands Reference

### Running the App
```bash
# Normal operation
streamlit run app.py

# Specify port
streamlit run app.py --server.port 8502

# Debug mode
streamlit run app.py --logger.level=debug
```

### Virtual Environment
```bash
# Create
python -m venv venv

# Activate (Windows)
venv\Scripts\activate

# Activate (macOS/Linux)
source venv/bin/activate

# Deactivate (all systems)
deactivate
```

### Dependency Management
```bash
# Install from requirements
pip install -r requirements.txt

# Check installed packages
pip list

# Update all packages
pip install --upgrade -r requirements.txt
```

---

## 🆘 Getting Help

### Check These Files In Order:
1. **QUICKSTART.md** - For quick questions
2. **README.md** - For detailed help
3. **app.py** - Look for comments in code
4. **PROJECT_SUMMARY.md** - For technical details

### Common Questions:

**Q: Where do I put my data?**
A: Upload in "📈 Data Preparation" → "📁 Upload Data"

**Q: Which Python version?**
A: 3.8, 3.9, 3.10, or 3.11 (3.12 might work)

**Q: Can I use on Mac/Linux?**
A: Yes! Same commands but use `python3` instead of `python`

**Q: How do I stop the app?**
A: Press `Ctrl+C` in the terminal

**Q: Can I modify the app?**
A: Yes! Edit app.py with any text editor and refresh the browser

---

## 🎯 Next Steps After Installation

### Immediate:
- ✅ Run the app
- ✅ Load sample data
- ✅ Train models
- ✅ Make predictions

### Short-term:
- ✅ Upload your own data
- ✅ Compare models
- ✅ Analyze predictions
- ✅ Customize colors

### Long-term:
- ✅ Deploy to cloud (Streamlit Cloud)
- ✅ Add more features
- ✅ Share with team
- ✅ Integrate with other tools

---

## 🚀 Advanced: Deployment

### Option 1: Streamlit Cloud (Recommended)
1. Push code to GitHub
2. Go to share.streamlit.io
3. Connect GitHub account
4. Deploy with one click
5. Get public URL to share!

### Option 2: Run on Computer (Discussed Above)
- Easiest for development
- No internet needed
- No sharing required

### Option 3: Docker (Advanced)
```bash
# Build container
docker build -t aqi-predictor .

# Run container
docker run -p 8501:8501 aqi-predictor
```

### Option 4: Cloud Server (AWS, Google Cloud, etc.)
- Requires technical setup
- Best for production
- Higher cost

---

## ✨ Success Checklist

After installation, you should have:

- [ ] Python 3.8+ installed
- [ ] Virtual environment created
- [ ] All dependencies installed
- [ ] App runs without errors
- [ ] Sample data loads
- [ ] Models train successfully
- [ ] Predictions generate
- [ ] All pages work
- [ ] Colors display correctly
- [ ] Charts render in browser

---

## 📞 Still Need Help?

### Windows Users:
- Check Python is in PATH
- Use Command Prompt, not PowerShell (if issues)
- Try Python launcher: `py --version`

### macOS Users:
- Use `python3` not `python`
- May need Xcode command line tools
- Homebrew: `brew install python3`

### Linux Users:
- Use `python3` not `python`
- Ubuntu: `sudo apt-get install python3-pip`
- Install build tools: `sudo apt-get install build-essential`

---

## 🎉 Ready to Predict!

You're now fully set up to:
- ✅ Upload air quality data
- ✅ Train ML models
- ✅ Make AQI predictions
- ✅ Analyze results
- ✅ Share insights

**Start your first prediction now!**

```bash
streamlit run app.py
```

---

## 📝 Quick Reference Card

```
╔════════════════════════════════════════════════════════════════╗
║                    QUICK REFERENCE                            ║
╠════════════════════════════════════════════════════════════════╣
║ Create Env   │ python -m venv venv                            ║
║ Activate     │ source venv/bin/activate (Mac/Linux)           ║
║              │ venv\Scripts\activate (Windows)                ║
║ Install      │ pip install -r requirements.txt                ║
║ Run App      │ streamlit run app.py                           ║
║ Open Browser │ http://localhost:8501                          ║
║ Stop App     │ Ctrl+C in terminal                             ║
║ Deactivate   │ deactivate                                     ║
╚════════════════════════════════════════════════════════════════╝
```

---

**Version**: 1.0.0  
**Updated**: 2024  
**Status**: Ready to Use ✅  

Happy predicting! 🌍
