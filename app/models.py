from sqlalchemy import Column, Integer, String, Float, Boolean, Text, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from app.database import Base


Base = declarative_base()

class AdminUser(Base):
    __tablename__ = "admin_users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    hashed_password = Column(String)

class ProductVariant(Base):
    __tablename__ = "product_variants"
    
    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, ForeignKey("products.id", ondelete="CASCADE"))
    color_name = Column(String, index=True) # Ej: "Rojo", "Negro/Azul"
    stock = Column(Integer, default=0)
    image_url = Column(String, nullable=True) # Foto opcional para el color
    
    # Relación inversa
    product = relationship("Product", back_populates="variants")

class Product(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(Text)
    price = Column(Float)
    stock = Column(Integer) # Esto quedará para productos simples
    image_url = Column(String) 
    has_physical_stock = Column(Boolean, default=True) 
    
    category_id = Column(Integer, ForeignKey("categories.id"), nullable=True)
    category = relationship("Category", back_populates="products")
    
    # NUEVO: Un producto puede tener muchas variantes (colores)
    # cascade="all, delete-orphan" hace que si borrás el producto, se borren sus colores automáticamente
    variants = relationship("ProductVariant", back_populates="product", cascade="all, delete-orphan")

class Config(Base):
    __tablename__ = "config"
    id = Column(Integer, primary_key=True, index=True)
    whatsapp_number = Column(String) 
    
class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)

    products = relationship("Product", back_populates="category")