from peewee import *

from user_srv.settings import settings


class BaseModel(Model):
    class Meta:
        database = settings.DB


class User(BaseModel):
    # 用户模型
    GENDER_CHOICES = (("female", "女"), ("male", "男"))
    ROLE_CHOICES = (("1", "普通用户"), ("2", "管理员"))
    mobile = CharField(max_length=11, index=True, unique=True, verbose_name="手机号码")
    password = CharField(max_length=100, verbose_name="密码")  # 1.密文 2.密文不可反解
    nick_name = CharField(max_length=20, null=True, verbose_name="昵称")
    head_url = CharField(max_length=200, null=True, verbose_name="头像")
    birthday = DateField(null=True, verbose_name="生日")
    address = CharField(max_length=200, null=True, verbose_name="地址")
    desc = TextField(null=True, verbose_name="个人简介")
    gender = CharField(max_length=6, choices=GENDER_CHOICES, verbose_name="性别")
    role = IntegerField(default=1, choices=ROLE_CHOICES, verbose_name="角色")


if __name__ == "__main__":
    settings.DB.create_tables([User])
# import hashlib
# m=hashlib.md5()
# salt="gwoow"
# password="123456"
# m.update((salt+password).encode("utf8"))
# print(m.hexdigest())
# from passlib.hash import pbkdf2_sha256
# hash = pbkdf2_sha256.hash("123456")
# print(hash)
# print(pbkdf2_sha256.verify("123456", hash))
# print(pbkdf2_sha256.verify("12346", hash))

# for i in range(10):
#     user = User()
#     user.nick_name = f"zhao{i}"
#     user.mobile = f"187102190{i}0"
#     user.password = pbkdf2_sha256.hash("123456")
#     user.save()
