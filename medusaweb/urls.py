# coding: utf-8

from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns(
    '',
    # Examples:
    # url(r'^$', 'medusaweb.views.home', name='home'),
    # url(r'^medusaweb/', include('medusaweb.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)


from spider import views
urlpatterns += patterns(
    '',
    # Jinja2 模板
    url(r'^jinja2/$', views.Jinja2View.as_view(), name='jinja2'),
    # 豆瓣电影 TOP250
    url(r'^movie/$', views.MovieView.as_view(), name='movie'),
)
