from django.db import models


# 角色
role_choices = (
    (1, "学生"),
    (2, "辅导员"),
    (3, "管理员"),
)
# 性别
gender_choices = (
    (1, "男"),
    (2, "女"),
)
# 请假条状态
leave_state_choices = (
    (1, "待审批"),
    (2, "已撤回"),
    (3, "审批中"),
    (4, "已驳回"),
    (5, "待销假"),
    (6, "销假中"),
    (7, "已完成"),
)
# 请假条类型
leave_category_choices = (
    (1, "事假"),
    (2, "公假"),
    (3, "病假"),
    (4, "出校申请"),
)


class User(models.Model):
    """用户表"""
    username   = models.CharField(verbose_name="用户名", max_length=32)
    password   = models.CharField(verbose_name="密码", max_length=255)
    role       = models.CharField(verbose_name="角色", max_length=8, choices=role_choices)
    create_datetime = models.DateTimeField(verbose_name="创建日期", auto_now_add=True)


class Admin(models.Model):
    """管理员表"""
    user       = models.ForeignKey(User, on_delete=models.CASCADE)
    name       = models.CharField(verbose_name="姓名", max_length=32)
    gender     = models.SmallIntegerField(verbose_name="性别", choices=gender_choices)


class Teacher(models.Model):
    """教师表"""
    user       = models.ForeignKey(User, on_delete=models.CASCADE)
    name       = models.CharField(verbose_name="姓名", max_length=32)
    gender     = models.SmallIntegerField(verbose_name="性别", choices=gender_choices)
    telephone  = models.CharField(verbose_name="电话号码", max_length=11)


class Student(models.Model):
    """学生表"""
    user       = models.ForeignKey(User, on_delete=models.CASCADE)
    teacher    = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    name       = models.CharField(verbose_name="姓名", max_length=32)
    gender     = models.SmallIntegerField(verbose_name="性别", choices=gender_choices)
    department = models.CharField(verbose_name="学部", max_length=38)
    faculty    = models.CharField(verbose_name="学院", max_length=38)
    major      = models.CharField(verbose_name="专业", max_length=38)
    grade      = models.CharField(verbose_name="年级", max_length=4)
    _class     = models.CharField(verbose_name="班级", max_length=2)


class Leave(models.Model):
    """请假条表"""
    user       = models.ForeignKey(User, on_delete=models.CASCADE)
    state      = models.CharField(verbose_name="请假条状态", max_length=8, choices=leave_state_choices)
    category   = models.CharField(verbose_name="请假类型", max_length=8, choices=leave_category_choices)
    apply_timestamp = models.DateTimeField(verbose_name="申请时间")
    start_timestamp = models.DateTimeField(verbose_name="开始时间")
    end_timestamp   = models.DateTimeField(verbose_name="结束时间")
    annex_url     = models.CharField(verbose_name="附件地址（图片/文件）", max_length=255)
    leave_reason  = models.TextField(verbose_name="请假原因")
    reject_reason = models.TextField(verbose_name="驳回原因")
    approver1_id  = models.BigIntegerField(verbose_name="审批人 1 id")
    a1_timestamp  = models.DateTimeField(verbose_name="审批人 1 审批时间")
    approver2_id  = models.BigIntegerField(verbose_name="审批人 2 id")
    a2_timestamp  = models.DateTimeField(verbose_name="审批人 2 审批时间")
    revoke_id     = models.BigIntegerField(verbose_name="销假人 id")
    revoke_timestamp = models.DateTimeField(verbose_name="销假时间")
