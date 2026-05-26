import os

# Set before any module imports so db/connection.py's create_engine() gets a valid URL
os.environ.setdefault("DATABASE_URL", "sqlite:///:memory:")
