# 🚀 Dockerized Streamlit DevOps Project

This project is a complete, production-ready Streamlit application designed for a seamless workflow from Android (via GitHub Codespaces) to Windows 11 (via Docker) and Streamlit Cloud.

## 📁 Project Structure
- `app.py`: The main Streamlit application with interactive widgets and Plotly charts.
- `Dockerfile`: Configuration for building the Docker image (Python 3.11).
- `requirements.txt`: Python dependencies (Streamlit, Pandas, Plotly).
- `packages.txt`: System-level dependencies for Linux environments.
- `.streamlit/config.toml`: Custom configuration for UI and server.
- `.github/workflows/`: CI/CD automation for Docker builds.
- `.devcontainer/`: Configuration for GitHub Codespaces.

---

## ☁️ STREAMLIT CLOUD DEPLOYMENT (Easiest)
1. Push this code to a **GitHub** repository.
2. Go to [share.streamlit.io](https://share.streamlit.io) and log in with GitHub.
3. Click **"New app"**, select your repository, and click **"Deploy!"**.
4. Streamlit Cloud will automatically use `requirements.txt` and `packages.txt` to set up your environment.

---

## 📱 ANDROID SETUP STEPS (GitHub Mobile / Chrome)
1. Open **Chrome** on your Android phone and go to `github.com` (Log in if needed).
2. Tap the **+** icon (top right) -> **New repository**.
3. Name it `streamlit-docker-app`, set it to **Public**, and tap **Create repository**.
4. On the setup page, tap the link **"creating a new file"**.
5. Type `Dockerfile` as the name, paste the content provided, and tap **Commit changes**.
6. Repeat this for all files (`requirements.txt`, `app.py`, etc.).

---

## ☁️ GITHUB CODESPACE LAUNCH (Run from Phone Browser)
1. On your GitHub repository page, tap the green **<> Code** button.
2. Select the **Codespaces** tab and tap **Create codespace on main**.
3. Wait for the environment to load (1-2 minutes).
4. A popup will appear: "Your application is running on port 8501. **Open in Browser**".
5. Tap **Open in Browser** to view your live Streamlit app.

---

## 💻 WINDOWS 11 COMMANDS (PowerShell)
```powershell
# 1. Clone your repository (Replace YOUR_USERNAME)
git clone https://github.com/YOUR_USERNAME/streamlit-docker-app.git
cd streamlit-docker-app

# 2. Build the Docker image
docker build -t streamlit-app:v1.0 .

# 3. Run the container
docker run -d -p 8501:8501 --name my-streamlit-app streamlit-app:v1.0

# 4. Open in browser
Start-Process "http://localhost:8501"
```

---

## 🐳 DOCKER HUB PUSH
1. Log in: `docker login`
2. Tag: `docker tag streamlit-app:v1.0 YOUR_DOCKER_USERNAME/streamlit-app:v1.0`
3. Push: `docker push YOUR_DOCKER_USERNAME/streamlit-app:v1.0`
4. Pull and run on Windows 11:
   `docker run -d -p 8501:8501 YOUR_DOCKER_USERNAME/streamlit-app:v1.0`

---

## 🧪 Stability & Troubleshooting
- **Dependency Handling**: `app.py` includes `try-except` blocks for Plotly imports to ensure the app loads even if dependencies fail.
- **System Packages**: `packages.txt` ensures necessary Linux libraries are available on Streamlit Cloud and Codespaces.
- **Versions**: All libraries are pinned (e.g., `streamlit==1.29.0`) for maximum consistency.
