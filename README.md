# 📊 Streamlit Data App

A simple Streamlit web app to upload a CSV file, preview data, view summary statistics, and filter by states.

---

## 🚀 Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/subham-bose17/Streamlit-Data-Repo.git
cd Streamlit-Data-Repo
```

---

### 2. Create a Virtual Environment
```bash
python -m venv myenv
```

---

### 3. Activate the Virtual Environment

#### ▶ Windows (PowerShell)
```powershell
myenv\Scripts\activate
```

⚠️ If you see an error like **“running scripts is disabled on this system”**, enable execution for your current user:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

Then try activating again:

```powershell
myenv\Scripts\activate
```

#### ▶ Windows (Command Prompt)
```cmd
myenv\Scripts\activate.bat
```

#### ▶ Linux / macOS
```bash
source myenv/bin/activate
```

---

### 4. Install Dependencies
```bash
pip install -r requirements.txt
```

If `requirements.txt` doesn’t exist yet, install manually:
```bash
pip install streamlit pandas
```

---

### 5. Run the App
```bash
streamlit run app.py
```

---

## 📂 Project Structure
```
Streamlit-Data-Repo/
│
├── data.py            # Main Streamlit application
├── requirements.txt  # Dependencies
├── README.md         # Project documentation
└── myenv/            # Virtual environment (ignored in GitHub)
```

---

## ✨ Features
- Upload CSV file  
- Data preview in interactive table  
- Summary statistics (`df.describe()`)  
- Filter data by **State** column  
