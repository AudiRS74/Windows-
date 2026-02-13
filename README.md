# 🚀 Dockerized Streamlit DevOps Project

This project is a complete, production-ready Streamlit application designed for a seamless workflow from Android (via GitHub Codespaces) to Windows 11 (via Docker).

## 📁 Project Structure
- `app.py`: The main Streamlit application with interactive widgets.
- `Dockerfile`: Configuration for building the Docker image (Python 3.11).
- `requirements.txt`: Python dependencies (Streamlit, Pandas, Plotly).
- `.dockerignore`: Files excluded from the Docker build.
- `.github/workflows/`: CI/CD automation for Docker builds.
- `.devcontainer/`: Configuration for GitHub Codespaces.

---

## 📱 ANDROID SETUP STEPS (GitHub Mobile / Chrome)
1. Open **Chrome** on your Android phone and go to `github.com` (Log in if needed).
2. Tap the **+** icon (top right) -> **New repository**.
3. Name it `streamlit-docker-app`, set it to **Public**, and tap **Create repository**.
4. On the setup page, tap the link **"creating a new file"**.
5. Type `Dockerfile` as the name, paste the content provided, and tap **Commit changes**.
6. Repeat this for all 7 files (`requirements.txt`, `app.py`, `.dockerignore`, etc.).
   *Note: For files in folders like `.github/workflows/docker-build.yml`, just type the full path as the filename.*

---

## ☁️ GITHUB CODESPACE LAUNCH (Run from Phone)
1. On your GitHub repository page, tap the green **<> Code** button.
2. Select the **Codespaces** tab and tap **Create codespace on main**.
3. Wait for the browser-based environment to load (takes about 1-2 minutes).
4. A popup will appear: "Your application is running on port 8501. **Open in Browser**".
5. Tap **Open in Browser** to view and use your live Streamlit app.

---

## 💻 WINDOWS 11 COMMANDS (PowerShell)
Run these commands in your PowerShell terminal to run the app locally:

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

## 🐳 DOCKER HUB PUSH (Pull instead of Build)
To push your image so Windows 11 just pulls it:
1. Log in to Docker on your machine: `docker login`
2. Tag your image: `docker tag streamlit-app:v1.0 YOUR_DOCKER_USERNAME/streamlit-app:v1.0`
3. Push to the cloud: `docker push YOUR_DOCKER_USERNAME/streamlit-app:v1.0`
4. On Windows 11, simply run:
   `docker run -d -p 8501:8501 YOUR_DOCKER_USERNAME/streamlit-app:v1.0`

---

## 🧪 Error Handling & Stability
The app uses specific versions for all dependencies (e.g., `streamlit==1.32.0`) to prevent "it works on my machine" issues. The code includes error handling for data generation to ensure the dashboard never crashes.
