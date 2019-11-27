import enum

from flaskr import db, ma
from sqlalchemy.orm import validates
from .Base import BaseModel



user_role = db.Table('user_role',
                     db.Column('user_id', db.String, db.ForeignKey('user.id')),
                     db.Column('role_id', db.String, db.ForeignKey('role.id'))
                     )


class User(db.Model, BaseModel):
    """ 用户模型
    """
    __tablename__ = "user"

    name = db.Column("name", db.String(32), nullable=False, comment="名字")
    nickname = db.Column("nickname", db.String(64), comment="昵称")
    gender = db.Column("gender", db.SmallInteger, comment="性别")
    avatar = db.Column("avatar", db.String, comment="头像")
    mobile = db.Column("mobile", db.String(16), comment="手机")
    email = db.Column("email", db.String, comment="邮箱")
    homepage = db.Column("homepage", db.String, comment="个人主页")
    birthday = db.Column("birthday", db.Date, comment="生日")
    height = db.Column("height", db.Float, comment="身高(cm)")
    bloodType = db.Column("blood_type", db.Enum(
        "A", "B", "AB", "O", "NULL"), comment="血型(ABO)")
    notice = db.Column("notice", db.Text, comment="备注")
    intro = db.Column("intro", db.Text, comment="简介")
    address = db.Column("address", db.JSON, comment="地址")
    lives = db.Column("lives", db.JSON, comment="生活轨迹")
    tags = db.Column("tags", db.JSON, comment="标签")
    luckyNumbers = db.Column("lucky_numbers", db.JSON, comment="幸运数字")
    score = db.Column("score", db.Integer, comment="积分")
    userNo = db.Column("user_no", db.Integer, autoincrement=True, comment="编号")
    roles = db.relationship('Role', secondary=user_role, backref="users")

    @validates('gender')
    def validate_gender(self, k, v):
        """验证性别"""
        assert v in [0, 1, 2], "性别参数错误，须为[0, 1, 2]之一"
        return v

    @validates('email')
    def validate_email(self, k, v):
        """验证邮箱"""
        assert '@' in v, "邮箱格式错误"
        return v


class UserSchema(ma.ModelSchema):
    """ 用户模式
    """
    class Meta:
        model = User
