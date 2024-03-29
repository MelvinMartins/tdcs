"""tdcs URL Configuration
"""

from django.urls import re_path

from tdcs_home import views

urlpatterns = [
    re_path(r"^tiles", views.tiles, name="tdcs_home_tiles"),
    re_path(r"^templates", views.template_list, name="tdcs_home_templates"),
]
