import hashlib

from gymapp.models import TaiKhoan

def authenticate(ten, mk):
    mk = str(hashlib.md5(mk.strip().encode('utf-8')).hexdigest())
    return TaiKhoan.query.filter(TaiKhoan.ten_dang_nhap==ten.strip(), TaiKhoan.mat_khau==mk).first()

def get_account_by_id(id):
    return TaiKhoan.query.get(id)