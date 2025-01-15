<a href="https://flask.palletsprojects.com/en/stable/"> <img alt="spring" src="https://img.shields.io/static/v1?style=for-the-badge&message=Budibase&color=000000&logo=Budibase&logoColor=FFFFFF&label="></a>
<a href="https://flask.palletsprojects.com/en/stable/"> <img alt="spring" src="https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white"></a>
<a href="https://flask.palletsprojects.com/en/stable/"> <img alt="spring" src="https://img.shields.io/badge/postgresql-4169e1?style=for-the-badge&logo=postgresql&logoColor=white"></a>
<a href="https://flask.palletsprojects.com/en/stable/"> <img alt="spring" src="https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white"></a>
<a href="https://flask.palletsprojects.com/en/stable/"> <img alt="spring" src="https://img.shields.io/badge/TensorFlow-FF3F06?style=for-the-badge&logo=tensorflow&logoColor=white"></a>
<a href="https://redis.io/"><img src="https://img.shields.io/badge/redis-%23DD0031.svg?style=for-the-badge&logo=redis&logoColor=white" alt="redis" > </a>
<a href="https://www.docker.com/"><img src="https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white" alt="docker" > </a>

# RebuildZone

RebuildZone is built to develop an emergency relief system, providing humanitarian aid during natural disasters (floods, landslides, etc.) and pandemics, especially in Vietnam, after experiencing COVID-19 and Typhoon YAGI.

The project was initiated for the [Vietnamese Open Source Software-Olympic IT Students Contest 2024](https://www.olp.vn/procon-pmmn/ph%E1%BA%A7n-m%E1%BB%81m-ngu%E1%BB%93n-m%E1%BB%9F). It is open-sourced under the [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0) license by the author team _Lazy Sunday Morning (LSM)_.

For more information about the contest, visit [vfossa.vn](https://vfossa.vn/tin-tuc/cong-bo-de-thi-noi-dung-phan-mem-nguon-mo-olympic-tin-hoc-sinh-vien-viet-nam-2024-727.html).

Canva presentation link at the competition: [link](https://www.canva.com/design/DAGYu2oIjn0/Z9J7rGkzynJUEw5MUv9A7w/edit?utm_content=DAGYu2oIjn0&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton)

---

## Table of Contents

1. [Introduction](#introduction)
2. [Core Features](#core-features)
3. [System Architecture](#system-architecture)
4. [Project Structure](#project-structure)
5. [Installation Guide](#installation-guide)
6. [Contributing](#contributing-to-the-project)
7. [License](#license)

---

### Introduction

RebuildZone focuses on supporting individuals during crises by leveraging technology, including AI, multilingual features, and efficient resource management.

---

### Core Features

The project highlights the following main features:

1. Personal status declaration (health, condition, and emergencies)
2. Image processing for damage predictions and statistics
3. Donation and humanitarian support management
4. Decision-making suggestions
5. Chatbot for health consultations and emergency guidance
6. Multilingual support for foreigners in Vietnam

---

### System Architecture

![image](docs/images/architech.svg)

---

### Project Structure

```plaintext
rebuild-zone/
├── chatbot-server/           # (Flask server) - AI Chatbot
│   ├── instance/             # SQLite database for saving chat history
│   ├── app.py                # Main application
│   ├── requirements.txt      # Python dependencies for the environment
│   └── Dockerfile
│
├── xray-server/              # (Flask server) - ChestXray
│   ├── imageutil/            # Implements GradCAM technique
│   ├── models/               # CNN models
│   ├── app.py
│   ├── requirements.txt
│   └── Dockerfile
│
├── budibase/                 # Budibase UI
│   ├── attachments/          # Image attachments
│   ├── budibase-client.js    # Budibase settings and configurations
│   ├── db.txt                # Budibase built-in database configuration & data
│   └── manifest.js
└── docker-compose.yml        # Docker Compose configuration
```

### Installation Guide

#### A. Installing Budibase

1. **Install Docker:**

   - Download Docker: [Get Docker](https://docs.docker.com/get-docker/).
   - Verify installation:
     ```bash
     docker --version
     docker info
     ```

2. **Run Budibase with Docker Compose:**

   - Start Budibase and MongoDB containers:
     ```bash
     docker-compose up -d
     ```

3. **Create Login Account:**
   Follow the prompts to set up your account.

   ![image](docs/images/images1.png)

4. **Add an empty app:**

   ![image](docs/images/images2.png)

5. **Add our app:**

   Import an app and access it via: <http://localhost:10000/builder/portal/{app-name}>.

   ![image](docs/images/images3.png)

---

#### B. Flask App Setup

1. **Install Python and Dependencies:**
   Ensure Python 3.6+ is installed:

   ```bash
   python --version
   python -m ensurepip --upgrade
   ```

2. **Install Requirements**

- Navigate to `chatbot-server` then `xray-server`:

  ```bash
  cd rebuild-zone/chatbot-server
  cd rebuild-zone/xray-server
  ```

- Install project dependencies from `requirements.txt`:

  ```bash
  pip install -r requirements.txt
  ```

3. **Run Flask App**: Set up environment variables and run

   ```bash
   python3 -m flask run
   ```

   You can contact us via [email](mailto://2151013029huy@ou.edu.vn) to have free access to our testing sandbox.

- Install project environment with provided example [/.env.example](https://github.com/anhtuan284/rebuild-zone/blob/developer/.env.example):

  ```bash
  # BACK-END ENV
  FLASK_APP=app.py
  # For xray-server
  CLOUDINARY_CLOUD_NAME=
  CLOUDINARY_API_KEY=
  CLOUDINARY_API_SECRET=
  SENTRY_DNS=

  # For chat server
  OPENAI_API_KEY=openAPIKey
  ...
  ```

- After finish setting up environment, you can run the following command:

  ```bash
  python3 -m flask run
  ```

  If the project is correctly set up, the terminal output will show this:

  ```bash
  Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
  ```

---

### Contributing to the Project

<a href="https://github.com/anhtuan284/rebuild-zone/issues/new?assignees=&labels=&projects=&template=bug_report.md&title=Bug+Report%3A+">Bug Report ⚠️
</a>

<a href="https://github.com/anhtuan284/rebuild-zone/issues/new?assignees=&labels=&projects=&template=feature_request.md&title=RequestFeature:">Request Feature 👩‍💻</a>

If you would like to contribute to the project, please refer to the [CONTRIBUTION.md](CONTRIBUTION.md) for more details.

All contributions are highly valued, so don't hesitate to submit a pull request to the project.

### Contact

- Trần An Tiến: 2151013099tien@ou.edu.vn
- Võ Quốc Huy: 2151013029huy@ou.edu.vn
- Trương Bùi Anh Tuấn: dev.atuan03@gmail.com

### License

This project is licensed under the terms of the [APACHE-2.0](LICENSE) license.
