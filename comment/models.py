from django.db import models
from blog.models import Post
from django.utils.translation import ugettext_lazy as _

class Comment(models.Model):
    STATUS_NORMAL = 1
    STATUS_DELETE = 0
    STATUS_ITEMS = (
        (STATUS_NORMAL, '正常'),
        (STATUS_DELETE, '删除'),
    )

    target = models.ForeignKey(Post, verbose_name=_("评论目标"), on_delete=models.CASCADE)
    content = models.CharField(_("内容"), max_length=2000)
    nickname = models.CharField(_("昵称"), max_length=50)
    website = models.URLField(_("网站"), max_length=200)
    email = models.EmailField(_("邮箱"), max_length=254)
    status = models.PositiveIntegerField(_("状态"), default=STATUS_NORMAL, choices=STATUS_ITEMS)
    created_time = models.DateTimeField(_("创建时间"), auto_now_add=True)

    class Meta:
        verbose_name = verbose_name_plural = '评论'

