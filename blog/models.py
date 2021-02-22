from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import ugettext_lazy as _

User = get_user_model()

class Category(models.Model):
    STATUS_NORMAL = 1
    STATUS_DELETE = 0
    STATUS_ITEMS = (
        (STATUS_NORMAL, '正常'),
        (STATUS_DELETE, '删除'),
    )

    name = models.CharField(_("名称"), max_length=50)
    status = models.PositiveIntegerField(_("状态"), default=STATUS_NORMAL, choices=STATUS_ITEMS)
    is_nav = models.BooleanField(_("是否为导航"), default=False)
    owner = models.ForeignKey(User, verbose_name=_("作者"), on_delete=models.CASCADE)
    created_time = models.DateTimeField(_("创建时间"), auto_now_add=True)
    
    class Meta:
        verbose_name = verbose_name_plural = '分类'
    
    def __str__(self):
        return self.name


class Tag(models.Model):
    STATUS_NORMAL = 1
    STATUS_DELETE = 0
    STATUS_ITEMS = (
        (STATUS_NORMAL, '正常'),
        (STATUS_DELETE, '删除'),
    )

    name = models.CharField(_("名称"), max_length=10)
    status = models.PositiveIntegerField(_("状态"), default=STATUS_NORMAL, choices=STATUS_ITEMS)
    owner = models.ForeignKey(User, verbose_name=_("作者"), on_delete=models.CASCADE)
    created_time = models.DateTimeField(_("创建时间"), auto_now_add=True)

    class Meta:
        verbose_name = verbose_name_plural = '标签'
        
    def __str__(self):
        return self.name
        

class Post(models.Model):
    STATUS_NORMAL = 1
    STATUS_DELETE = 0
    STATUS_DRAFT = 2
    STATUS_ITEMS = (
        (STATUS_NORMAL, '正常'),
        (STATUS_DELETE, '删除'),
        (STATUS_DRAFT, '草稿'),
    )

    title = models.CharField(_("标题"), max_length=255)
    desc = models.CharField(_("摘要"), max_length=1024)
    content = models.TextField(_("正文"), help_text="正文必须为Markdown格式")
    status = models.PositiveIntegerField(_("状态"), default=STATUS_NORMAL, choices=STATUS_ITEMS)
    category = models.ForeignKey(Category, verbose_name=_("分类"), on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, verbose_name=_("标签"), on_delete=models.CASCADE)
    owner = models.ForeignKey(User, verbose_name=_("作者"), on_delete=models.CASCADE)
    created_time = models.DateTimeField(_("创建时间"), auto_now_add=True)

    class Meta:
        verbose_name = verbose_name_plural = '文章'
        ordering= ['-id']
        
    def __str__(self):
        return self.name