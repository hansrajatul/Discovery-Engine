from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class LinuxAsset(Base):
    __tablename__ = "linux_assets"

    id = Column(Integer, primary_key=True)
    server = Column(String)
    username = Column(String)
    uid = Column(Integer)
    shell = Column(String)
    is_sudo = Column(Boolean)
