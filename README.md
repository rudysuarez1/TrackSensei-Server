# 🏎️ TrackSensei Server 🏎️

This is the backend server for the TrackSensei system. It is built using FastAPI and PostgreSQL to handle user lap uploads, session management, and telemetry analysis.

## 🚀 Setup

### 1. Clone the repository and install dependencies with Poetry
```bash
git clone https://github.com/your-username/TrackSensei-Server.git
cd TrackSensei-Server
```

#### Running on macOS:
```bash
brew install python
# Intel Macs:
curl -sSL https://install.python-poetry.org | /usr/local/bin/python3
# Apple Silicon (M1/M2):
curl -sSL https://install.python-poetry.org | /opt/homebrew/bin/python3
```

Then install project dependencies:
```bash
poetry install
```

### 2. Setup PostgreSQL locally
Start PostgreSQL and create the development DB and user:
```sql
CREATE DATABASE tracksensei_dev;
CREATE USER tracksensei_user WITH PASSWORD 'devpass123';
GRANT ALL PRIVILEGES ON DATABASE tracksensei_dev TO tracksensei_user;
```

### 3. Environment Configuration
Copy and edit the environment file:
```bash
cp .env.example .env
```
Update your `.env` file:
```env
DATABASE_URL=postgresql://tracksensei_user:devpass123@localhost/tracksensei_dev
```

---

## ✅ Pre-commit and Code Quality
Install pre-commit hooks:
```bash
poetry run pre-commit install
```

To run all code quality checks manually:
```bash
poetry run pre-commit run --all-files
poetry run pyright
poetry run pytest
poetry run pytest --cov
```

Or all together:
```bash
poetry run pre-commit run --all-files && poetry run pyright && poetry run pytest
```

---

## 🌐 Running the Server
Start the development server:
```bash
poetry run uvicorn backend.main:app --reload
```

Visit [http://localhost:8000/docs](http://localhost:8000/docs) to view the interactive API documentation.

---

## 🧪 Running Tests
```bash
poetry run pytest
```

---

## 🧪 First-Time Dev Quickstart
```bash
poetry shell
poetry run uvicorn backend.main:app --reload
```

## 💧 Tech Stack
- Python 3.10+
- FastAPI
- PostgreSQL
- SQLAlchemy
- Poetry
- Pyright
- Pre-commit
- Pytest
