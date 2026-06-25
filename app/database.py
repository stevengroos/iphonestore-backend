from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Usamos la DIRECT_URL (Puerto 5432)
# ¡RECUERDA CAMBIAR [YOUR-PASSWORD] POR TU CONTRASEÑA REAL SIN LOS CORCHETES!
SQLALCHEMY_DATABASE_URL = "postgresql://postgres.ztywhqqmiksxzouakbwe:lucandy2026steven@aws-1-sa-east-1.pooler.supabase.com:5432/postgres"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()