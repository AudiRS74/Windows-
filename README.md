# 🚀 Multi-Platform Streamlit Dashboard (windows.py)

A production-ready Streamlit project designed for **Android**, **Windows 11**, and **Streamlit Cloud**.

---

## ☁️ STREAMLIT CLOUD DEPLOY (Free Hosting)
1. Push this code to a **GitHub** repository.
2. Go to [share.streamlit.io](https://share.streamlit.io).
3. Click **"New app"** and select your repo.
4. **CRITICAL STEP**: Click **"Advanced settings"** at the bottom.
5. In the **"Main file path"** field, delete `streamlit_app.py` and type `windows.py`.
6. Click **Deploy!**

---

## 📱 ANDROID GITHUB SETUP (Mobile Browser)
1. Open **Chrome** on Android -> `github.com` (Login).
2. Tap **+** (Top Right) -> **New repository**.
3. Name it `my-streamlit-project` -> **Public** -> **Create**.
4. Tap **"uploading an existing file"** or use the **"+"** icon to create new files one by one.
5. Copy-paste the content of all 7 files from your source.
6. For folders (like `.github/workflows/`), type the full path as the filename (e.g., `.github/workflows/docker-build.yml`).

---

## ☁️ CODESPACE TEST (Phone Browser)
1. On your GitHub repo page, tap the green **<> Code** button.
2. Select **Codespaces** -> **Create codespace on main**.
3. Once loaded, it will automatically run `pip install` and start the app.
4. Look for the "Ports" tab or the popup "Open in Browser" to see the live app on your phone.

---

## 💻 WINDOWS 11 DOCKER (PowerShell)
Open PowerShell in your project folder and run:
```powershell
# 1. Build the image
docker build -t streamlit-windows:v1.0 .

# 2. Run the container
docker run -d -p 8501:8501 --name streamlit-app streamlit-windows:v1.0

# 3. View the app
Start-Process "http://localhost:8501"
```

---

## 🐳 DOCKER HUB PUSH (One-Click Windows Pull)
1. Login: `docker login`
2. Tag your image: `docker tag streamlit-windows:v1.0 YOUR_DOCKER_USER/streamlit-windows:v1.0`
3. Push image: `docker push YOUR_DOCKER_USER/streamlit-windows:v1.0`
4. **On Windows 11**, just run:
   `docker run -d -p 8501:8501 YOUR_DOCKER_USER/streamlit-windows:v1.0`

---

## 📁 Project Structure
- `windows.py`: Main interactive application.
- `Dockerfile`: Multi-platform container config.
- `requirements.txt`: Pinned Python dependencies.
- `packages.txt`: System-level dependencies.
- `.dockerignore`: Files to exclude from Docker.
- `.github/workflows/`: CI/CD automation.
- `.devcontainer/`: Codespaces cloud config.
