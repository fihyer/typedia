from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import ugettext_lazy as _

User = get_user_model()

class Link(models.Model):
    STATUS_NORMAL = 1
    STATUS_DELETE = 0
    STATUS_ITEMS = (
        (STATUS_NORMAL, '正常'),
        (STATUS_DELETE, '删除'),
    )

    title = models.CharField(_("标题"), max_length=50)
    href = models.URLField(_("连接"), max_length=200)
    status = models.PositiveIntegerField(_("状态"), default=STATUS_NORMAL, choices=STATUS_ITEMS)
    weight = models.PositiveIntegerField(_("权重"), help_text="权重高展示顺序靠前",default=1, choices=zip(range(1,6), range(1,6)))
    owner = models.ForeignKey(User, verbose_name=_("作者"), on_delete=models.CASCADE)
    created_time = models.DateTimeField(_("创建时间"), auto_now_add=True)

    class Meta:
        verbose_name = verbose_name_plural = '友链'

        
class SideBar(models.Model):
    STATUS_SHOW = 1
    STATUS_HIDE = 0
    STATUS_ITEMS = (
        (STATUS_SHOW, '显示'),
        (STATUS_HIDE, '隐藏'),
    )
    SIDE_TYPE = (
        (1, 'HTML'),
        (2, '最新文章'),
        (3, '最热文章'),
        (4, '最近评论'),
    )

    title = models.CharField(_("标题"), max_length=50)
    display_type = models.PositiveIntegerField(_("展示类型"), default=1, choices=SIDE_TYPE)
    content = models.CharField(_("内容"), max_length=500, blank=True, help_text="如果设置的不是HTML类型，可为空")
    status = models.PositiveIntegerField(_("状态"), default=STATUS_SHOW, choices=STATUS_ITEMS)
    owner = models.ForeignKey(User, verbose_name=_("作者"), on_delete=models.CASCADE)
    created_time = models.DateTimeField(_("创建时间"), auto_now_add=True)
    
    class Meta:
        verbose_name = verbose_name_plural = '侧边栏'