from django.conf.urls import patterns, include, url
# from django.contrib import admin
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()
from django.contrib import admin
admin.autodiscover()
urlpatterns = patterns('',
    # Examples:
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^home/(?P<page>[\d]+)', 'jiabin.views.homess', name='home'),
    url(r'^homeall/(?P<t>[\d]+)', 'jiabin.views.run', name='home'),
    url(r'^home/delete', 'jiabin.views.deletec', name='homes'),
    url(r'^home/saves', 'jiabin.views.saves', name='homes'),
    url(r'^home/homex', 'jiabin.views.homex', name='homes'),
    url(r'^home/update_event', 'jiabin.views.update_event', name='home'),
    url(r'^home/shaomiao', 'jiabin.views.shaomiao', name='home'),
    url(r'^home/add_event', 'jiabin.views.add_event', name='home'),
    url(r'^index/$', 'jiabin.views.jiabin_list_index', name='home1'),
    url(r'^index/(?P<page>[\d]+)/$', 'jiabin.views.jiabin_list_index', name='home'),
    url(r'^index/guest/$', 'jiabin.views.jiabin_guest_index', name='home'),
    url(r'^index/guest_invitation/(?P<page>[\d]+)/$', 'jiabin.views.jiabin_guest_invitation', name='home'),
    url(r'^index/Search_guest/$', 'jiabin.views.Search_guest', name='home'),
    url(r'^index/cat_guest/$', 'jiabin.views.cat_guest', name='home'),
    url(r'^jiabin_edit', 'jiabin.views.jiabin_edit', name='home'),
    url(r'^event_user_save', 'jiabin.views.event_user_save', name='home'),
    url(r'^img_user_save', 'jiabin.views.img_user_save', name='home'),
    url(r'^event_cat', 'jiabin.views.event_cat', name='home'),
    url(r'^index/jiabin_cat_list_index/(?P<cat_n>[\d]+)/(?P<page>[\d]+)/', 'jiabin.views.jiabin_cat_list_index', name='home'),
    url(r'^send_guest_invitation', 'jiabin.views.send_guest_invitation', name='home'),
    url(r'^index/Search_guest/(?P<page>[\d]+)/', 'jiabin.views.Search_guest', name='home'),
    url(r'^site_media/(?P<path>.*)','django.views.static.serve',{'document_root':'/data/web/ftptest/log_save/jiabin/static/images/'},name='home')




    # url(r'^jiabing/', include('jiabing.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
