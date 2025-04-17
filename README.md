# 🏎️ TrackSensei Server 🏎️

This is the backend server for the TrackSensei system. It is built using FastAPI and PostgreSQL to handle user lap uploads, session management, and telemetry analysis.

## 🚀 Setup

### 1. Clone the repository and install dependencies with Poetry

```bash
git clone https://github.com/your-username/TrackSensei-Server.git
cd TrackSensei-Server
```

#### Running on macOS:

Install Python and Poetry:

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

### 2. Setup PostgreSQL locally using Homebrew

Install and start PostgreSQL:

```bash
brew install postgresql
brew services start postgresql
```

Create the development database and user:

```bash
createdb tracksensei_dev
createuser -P tracksensei_user
```

Then, connect to PostgreSQL shell and grant privileges:

```sql
psql tracksensei_dev

GRANT ALL PRIVILEGES ON DATABASE tracksensei_dev TO tracksensei_user;
```

### 3. Environment Configuration

Copy and edit the environment file:

```bash
cp .env.example .env
```

Update your `.env` file with your PostgreSQL credentials:

```env
DATABASE_URL=postgresql://tracksensei_user:yourpassword@localhost/tracksensei_dev
```

---

## ✅ Pre-commit and Code Quality

Install pre-commit hooks:

```bash
poetry run pre-commit install
```

Run all code quality checks manually:

```bash
poetry run pre-commit run --all-files
poetry run pyright
poetry run pytest
poetry run pytest --cov
```

Or run them all together:

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

---

## 💧 Tech Stack

- Python 3.10+
- FastAPI
- PostgreSQL
- SQLAlchemy
- Poetry
- Pyright
- Pre-commit
- Pytest

## Security Roadmap
For details on our security roadmap, please see [SECURITY.md](SECURITY.md).
