import hashlib

from flask_login import UserMixin
from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime, Double, Enum as SQLEnum, Boolean
from sqlalchemy.orm import relationship
from enum import Enum as Enum
from gymapp import db, app


class VaiTroEnum(Enum):
    ADMIN = 1
    THU_NGAN = 2
    LE_TAN = 3
    HLV = 4
    KHAC_HHANG = 5
    
class DangKyEnum(Enum):
    CHO_DUYET = 1
    DANG_HOAT_DONG = 2
    DA_HUY = 3
    HET_HAN = 4

class HoaDonEnum(Enum):
    CHUA_THANH_TOAN = 1
    DA_THANH_TOAN = 2

class BaseModel(db.Model):
    __abstract__ = True
    id = Column(Integer, autoincrement=True, primary_key=True)

class TaiKhoan(BaseModel,UserMixin):
    ten_dang_nhap = Column(String(50), nullable=False)
    mat_khau = Column(String(100), nullable=False)
    vai_tro = Column(SQLEnum(VaiTroEnum), default=VaiTroEnum.KHAC_HHANG)
    nguoi_dung = relationship("NguoiDung", backref="tai_khoan", lazy=True, uselist=False)

class NguoiDung(BaseModel):
    ho_ten = Column(String(50), nullable=False)
    gioi_tinh = Column(String(10), nullable=False)
    nam_sinh = Column(Integer, nullable=False)
    sdt = Column(String(10), nullable=False)
    email = Column(String(100), nullable=False)
    tai_khoan_id = Column(Integer, ForeignKey(TaiKhoan.id), nullable=False)
    khach_hang = relationship("KhachHang", backref="nguoi_dung", lazy=True)
    hlv = relationship("HuanLuyenVien", backref="nguoi_dung", lazy=True)

class GoiTap(BaseModel):
    ten = Column(String(20), nullable=False)
    thoi_han = Column(Integer, nullable=False)
    gia = Column(Double, nullable=False)
    noi_dung = Column(Text)
    dang_ky = relationship("DangKy", backref="goi_tap", lazy=True)

class KhachHang(db.Model):
    id = Column(Integer, ForeignKey(NguoiDung.id), primary_key=True, unique=True)
    is_hoi_vien = Column(Boolean, default=False)
    dang_ky = relationship("DangKy", backref="khach_hang", lazy=True)

class DangKy(BaseModel):
    trang_thai = Column(SQLEnum(DangKyEnum), nullable=False)
    ngay_dang_ky = Column(DateTime)
    ngay_het_hang = Column(DateTime)
    khach_hang_id = Column(Integer, ForeignKey(KhachHang.id), nullable=False)
    goi_tap_id = Column(Integer, ForeignKey(GoiTap.id), nullable=False)
    hoa_don = relationship("HoaDon", backref="dang_ky", lazy=True)

class HoaDon(BaseModel):
    so_tien = Column(Double, nullable=False)
    ngay_tao = Column(DateTime, nullable=False)
    trang_thai = Column(SQLEnum(HoaDonEnum), nullable=False)
    dang_ky_id = Column(Integer, ForeignKey(DangKy.id), nullable=False, unique=True)

class HuanLuyenVien(db.Model):
    id = Column(Integer, ForeignKey(NguoiDung.id), primary_key=True, unique=True)

class KeHoachLuyenTap(BaseModel):
    ngay_tao = Column(DateTime, nullable=False)
    hlv_id = Column(Integer, ForeignKey(HuanLuyenVien.id), nullable=False)
    khach_hang_id = Column(Integer, ForeignKey(KhachHang.id), nullable=False)
    chi_tiet = relationship("ChiTietKeHoach", backref="ke_hoach", lazy=True)

class DanhMucBaiTap(BaseModel):
    ten = Column(String(50), nullable=False)

class BaiTap(BaseModel):
    ten = Column(String(50), nullable=False)
    mo_ta = Column(Text)
    danh_muc_bai_tap_id = Column(Integer, ForeignKey(DanhMucBaiTap.id), nullable=False)

class ChiTietKeHoach(BaseModel):
    tuan_thu = Column(Integer, nullable=False)
    so_hiep = Column(Integer, nullable=False)
    so_lan_mot_hiep = Column(Integer, nullable=False)
    bai_tap_id = Column(Integer, ForeignKey(BaiTap.id), nullable=False)
    ke_hoach_tap_luyen_id = Column(Integer, ForeignKey(KeHoachLuyenTap.id), nullable=False)

class NgayTap(db.Model):
    id = Column(Integer, ForeignKey(KeHoachLuyenTap.id), primary_key=True, unique=True)
    thu = Column(Integer)

class QuyDinh(BaseModel):
    ten = Column(String(50), nullable=False)
    gia_tri = Column(String(50), nullable=False)
    mo_ta = Column(Text)


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        db.session.add(TaiKhoan(ten_dang_nhap='admin', mat_khau=str(hashlib.md5('1'.encode('utf-8')).hexdigest()), vai_tro=VaiTroEnum.ADMIN))
        db.session.commit()
