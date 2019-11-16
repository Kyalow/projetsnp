"""Projet_web URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url
from SNP_site.views import home_direct, snp_search_redirect, list_phenotype_redirection, snp_search_entry, snp_detail_entry_search, phenotype_detail, direct
urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^home_page/$', home_direct),
    url(r'^snp_search/$', snp_search_redirect, name="snp_search"),
    url(r'^list_pheonotype_home_page/$', list_phenotype_redirection, name = "list_pheonotype"),
    url(r'^SNP_search_result_page/$', snp_search_entry, name = "SNP_search_result_page"),
    url(r'^SNP_search_detail_page/$', snp_detail_entry_search, name = "SNP_detail"),
    url(r'^phenotype_detail_page/$', phenotype_detail, name = 'phenotype_detail'),
    url(r'^$', direct)
]
