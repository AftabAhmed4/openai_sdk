# 🚀 Setup Guide: Install & Initialize uv Project

### 1. **Install `uv`**

* Open **Windows PowerShell** as **Administrator**
* Run this command:

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

### 2. **Check Version**

```powershell
uv --version
```

(agar version number show ho jaye to install successful hai ✅)

---

### 3. **Initialize Project**

```powershell
uv init hello_sdk
```

### 4. **Change Directory**

```powershell
cd hello_sdk
```

### 5. **Create Virtual Environment**

```powershell
uv venv
```

### 6. **Activate Virtual Environment**

```powershell
.venv\Scripts\activate
```

Prompt aise show hoga:

```
(hello_sdk) PS D:\aftab\agentic ai\hello_sdk>
```

### 7. **Open in VS Code**

```powershell
code .
```

---
### 8. Install Packages using uv
```
uv add openai-agents python-dotenv chainlit
```