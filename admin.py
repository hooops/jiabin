#! -*- coding:utf-8 -*-
from jiabin import models
from django.contrib import admin
# class jiabin(admin.ModelAdmin):
class jiabin_admin(admin.ModelAdmin):
    list_display=('id','username','introduce','baikeURL','homeurl','cat_event_id','jiabin_id','cat','title','begin_time','end_time','recommend','company','position')

    search_fields =('username','id','cat_event_id')
    def id(self,obj):
        return obj.jiabin_m.id
    id.short_description  = 'id'

    def username(self,obj):
        return obj.jiabin_m.username
    username.short_description  = '名称'


    def introduce(self,obj):
        return obj.jiabin_m.introduce
    introduce.short_description  = '简介'
    def baikeURL(self,obj):
        baike=obj.username
        return u'<a href="http://baike.baidu.com/search/word?word=%s" target="_blank">%s</a>' \
            % (baike, baike)
    baikeURL.short_description  = '百度百科'
    def homeurl(self,obj):
        event=obj.cat_event_id
        return u'<a href="http://www.huodongjia.com/event-%s.html" target="_blank">%s</a>' \
            % (event, event)
    homeurl.short_description  = '活动家'
    def cat_event_id(self,obj):
        return  obj.jiabin_m.cat_event_id
    cat_event_id.short_description  = '活动id'
    def jiabin_id(self,obj):
        return obj.jiabin_m.jiabin_id
    jiabin_id.short_description  = '活动关联id'
    # def imgs(self,obj):
    #     return obj.jiabin.imgs
    # imgs.short_description  = '图片'
    def cat(self,obj):
        return obj.jiabin_m.cat
    cat.short_description  = '类别'
    def title(self,obj):
        return obj.jiabin_m.title
    title.short_description  = '活动名称'
    def begin_time(self,obj):
        return obj.jiabin_m.begin_time
    begin_time.short_description  = '开始时间'
    def end_time(self,obj):
        return obj.jiabin_m.end_time
    end_time.short_description  = '结束时间'
    def recommend(self,obj):
        return obj.jiabin_m.imgs
    recommend.short_description  = '是否推荐'
    def company(self,obj):
        return obj.jiabin_m.company
    company.short_description  = '公司'
    def position(self,obj):
        return obj.jiabin_m.position
    position.short_description  = '职位'
    raw_id_fields = ['jiabin_id'] 
    # ordering = ('id')
class send_guest_invitation_admin(admin.ModelAdmin):
    list_display=('id','in_guest','in_company','in_meeting','event_id','in_name','in_mobilphone','in_message')
    search_fields =('id','in_company','in_meeting','event_id','in_name','in_mobilphone','in_message','in_guest')
    def in_guest(self,obj):
        return obj.jiabin_m.in_guest
    in_guest.short_description  = 'in_guest'
    def id(self,obj):
        return obj.jiabin_m.id
    id.short_description  = 'id'
    def in_company(self,obj):
        return obj.jiabin_m.in_company
    in_company.short_description  = 'in_company'
    def in_meeting(self,obj):
        return obj.jiabin_m.in_meeting
    in_meeting.short_description  = 'in_meeting'
    def event_id(self,obj):
        return obj.jiabin_m.event_id
    event_id.short_description  = 'event_id'
    def in_name(self,obj):
        return obj.jiabin_m.in_name
    in_name.short_description  = 'in_name'
    def in_mobilphone(self,obj):
        return obj.jiabin_m.in_mobilphone
    in_mobilphone.short_description  = 'in_mobilphone'
    def in_message(self,obj):
        return obj.jiabin_m.in_message
    in_message.short_description  = 'in_message'

    # raw_id_fields = ['event_id']
admin.site.register(models.jiabin_m,jiabin_admin)
admin.site.register(models.send_guest_invitation,send_guest_invitation_admin)

