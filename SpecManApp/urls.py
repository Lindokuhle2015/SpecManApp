# -*- coding: utf-8 -*-
"""
Created on Mon Nov 14 09:40:37 2016

@author: lindo
"""

#urls.py ==> SpecManApp Directory


from django.conf.urls import patterns, url, include
from SpecManApp import views

urlpatterns = [
        url(r'^$', views.index, name='index'),
        url(r'^about/$', views.about, name='about'),
       
        #url(r'^register/$', views.register, name='register'),
        #url(r'^login/$',  views.user_login, name='login'),
       # url(r'^logout/$', views.user_logout, name = 'logout'),
]