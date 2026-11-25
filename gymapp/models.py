import hashlib

from flask_login import UserMixin
from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime, Double, Enum
from sqlalchemy.orm import relationship
from enum import Enum as RoleEnum
from gymapp import db, app


class VaiTroEnum(RoleEnum):
    ADMIN = 1
    THUNGAN = 2
    LETAN = 3
    HLV = 4
    KHACHHANG = 5

class BaseModel(db.Model):
    __abstract__ = True
    id = Column(Integer, autoincrement=True, primary_key=True)

class TaiKhoan(BaseModel,UserMixin):
    ten_dang_nhap = Column(String(50), nullable=False)
    mat_khau = Column(String(100), nullable=False)
    vai_tro = Column(Enum(VaiTroEnum), default=VaiTroEnum.KHACHHANG)
    nguoi_dung = relationship("NguoiDung", backref="tai_khoan", lazy=True, uselist=False)

class NguoiDung(BaseModel):
    ho_ten = Column(String(50), nullable=False)
    gioi_tinh = Column(String(10), nullable=False)
    nam_sinh = Column(Integer, nullable=False)
    sdt = Column(String(10), nullable=False)
    email = Column(String(100), nullable=False)
    tai_khoan_id = Column(Integer, ForeignKey(TaiKhoan.id), nullable=False)

class GoiTap(BaseModel):
    ten = Column(String(20), nullable=False)
    thoi_han = Column(Integer, nullable=False)
    gia = Column(Double, nullable=False)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        db.session.add(TaiKhoan(ten_dang_nhap='admin', mat_khau=str(hashlib.md5('1'.encode('utf-8')).hexdigest()), vai_tro=VaiTroEnum.ADMIN))
        db.session.commit()
