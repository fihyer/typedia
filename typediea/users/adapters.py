from typing import Any

from allauth.account.adapter import DefaultAccountAdapter
from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from django.conf import settings
from django.http import HttpRequest


class accountadapter(defaultaccountadapter):
    def is_open_for_signup(self, request: httprequest):
        return getattr(settings, "account_allow_registration", true)


class socialaccountadapter(defaultsocialaccountadapter):
    def is_open_for_signup(self, request: HttpRequest, sociallogin: Any):
        return getattr(settings, "ACCOUNT_ALLOW_REGISTRATION", True)
