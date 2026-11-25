from flask import redirect
from flask_admin import Admin, BaseView, expose
from flask_admin.contrib.sqla import ModelView
from flask_login import current_user, logout_user

from gymapp import app, db
from gymapp.models import VaiTroEnum, GoiTap

admin = Admin(app, name="Quản lý gym")

class BaseAdminView(BaseView):
    def is_accessible(self):
        return current_user.is_authenticated

class AdminView(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated and current_user.vai_tro == VaiTroEnum.ADMIN


class LogoutView(BaseAdminView):
    @expose("/")
    def index(self):
        logout_user()
        return redirect('/admin')

admin.add_view(AdminView(GoiTap, db.session, name="Gói Tập"))
admin.add_view(LogoutView(name='Đăng xuất'))
