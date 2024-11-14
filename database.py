import streamlit as st
from sqlalchemy import create_engine, Column, Integer, String, Text, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker



# Database configuration
DATABASE_URL = "mysql+pymysql://root:.X4mD1ng@localhost:3306/crud"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

try:
    # Cek koneksi dengan menjalankan query sederhana
    with engine.connect() as connection:
        print("Koneksi ke database berhasil!")
except Exception as e:
    print(f"Terjadi kesalahan saat koneksi ke database: {e}")
# Base model
Base = declarative_base()

# Define product model
class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    price = Column(Float, nullable=False)
    description = Column(Text)

Base.metadata.create_all(bind=engine)


# CRUD Functions
def get_all_products():
    session = SessionLocal()
    products = session.query(Product).all()
    session.close()
    return products

def create_product(name, price, description):
    session = SessionLocal()
    new_product = Product(name=name, price=price, description=description)
    session.add(new_product)
    session.commit()
    session.close()

def update_product(product_id, name, price, description):
    session = SessionLocal()
    product = session.query(Product).filter(Product.id == product_id).first()
    product.name = name
    product.price = price
    product.description = description
    session.commit()
    session.close()

def delete_product(product_id):
    session = SessionLocal()
    product = session.query(Product).filter(Product.id == product_id).first()
    session.delete(product)
    session.commit()
    session.close()
