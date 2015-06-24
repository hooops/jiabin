#! -*- coding:utf-8 -*-
import urllib2
import json
from django.shortcuts import render
from django.shortcuts import render_to_response, RequestContext
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from new_event.models import NewVenue
#import datetime
from django.contrib.sessions.models import Session
from django.utils import timezone
import json
from PIL import Image
from django.views.decorators.csrf import csrf_exempt
#加这个post提交不会403
from django.core.cache import cache
from admin_self.common import  newly_event
import re
from new_event.models import NewDistrict
from django.http import HttpResponseRedirect
from admin_self.common import NewformatEvent,NewCatUrl
import models
from django.db import transaction
import base64
from django.shortcuts import render_to_response,render
from django.template import loader,Context
from django.core.urlresolvers import reverse
from django.shortcuts import redirect
from django.http import HttpResponseRedirect
from new_event.models import NewEventTable
from django.views.decorators.cache import cache_page
from django.db.models import Q
import fenci
import sys
import pagination
import datetime
import models

reload(sys)
sys.setdefaultencoding("utf-8")
def homes(request,page):
    k=[0]*20

    s=models.NewEventParagraph.objects.all().using('jiabin')[int(page)*20-20:int(page)*20]
    s1=[]

    for x in s:

        s1.append(fenci(x))
    global  s2
    s2=[0]*70
    s2={}.fromkeys(s1).keys()
    sk=[0]*int(len(s2))
    t=0
    while t<int(len(s2)):

        sk[t]={'sid':s2[t]}
        if int(len(str(s2[t])))>0 and int(len(str(s2[t])))<=9 and s2[t] is not None:
            models.jiabin.objects.using('jiabin').create(
            name=s2[t]
    )
        t+=1

    # t = loader.get_template('userfor.html')
    # c=Context({'k':sk })
    # return HttpResponse(t.render(c))

def runs(request,t):

    ss=int(t)
    while ss<100:
        homes(request,ss)
        ss+=1
    if ss==99:
            ts = loader.get_template('userfor.html')
            c=Context()
            return HttpResponse(ts.render(c))






def homess(request,page):
    st=models.jiabin_m.objects.all()
    cont=int(len(st))
    nextPage=int(page)+1
    stn_event=models.jiabin_event.objects.get(id=1)
    stn=models.NewEventParagraph.objects.filter(id__gt=stn_event.all_event)
    all_event=int(len(stn))
    global new_add_event
    new_add_event=[]
    if all_event>0:
        t=1
        while t<all_event+1:

            new_add_event.append(int(stn_event.all_event+t))
            t+=1

    all_event_now_cont=all_event
    if page>1:
        lastPage=int(page)-1
    else:
        lastPage=1
    endPage=int(len(st))/20
    if len(str(page))<11:


        if int(page)>0 and int(page)<int(cont)/20:
            ass=[0]*20
            s=st[int(page)*20-20:int(page)*20]

            ts=0
            while ts<20:

                ass[ts]={'username':s[ts].username,'id':s[ts].id,'homeurl':s[ts].homeurl,'cat_id':s[ts].cat_event_id,'page':page}
                ts+=1
            t = loader.get_template('userfor.html')
            c=Context({'kk':ass,'nextPage':nextPage,'lastPage':lastPage,'endPage':endPage,'page':page,

                        'all_event_now_cont':all_event_now_cont,
                        'cont':cont,
                        'all_event':all_event})
            return HttpResponse(t.render(c))
        elif int(page)<=0:
            return  HttpResponseRedirect("/jiabin/home/"+str(1)+"")
        elif int(page)>=int(cont)/20:
            return  HttpResponseRedirect("/jiabin/home/"+str(int(cont)/20)+"")
    else:
        return  HttpResponseRedirect("/jiabin/home/"+str(int(cont)/20)+"")

def deletec(request):
    t=request.GET.get('delete')
    page=request.GET.get('page')
    try:
        st=models.jiabin_m.objects.get(id=t)
        st.delete()
    except:
        transaction.rollback()



    return  HttpResponseRedirect("/jiabin/home/"+str(int(page))+"")

def saves(request):
    usernames=request.GET.get('username')
    cat_id=request.GET.get('cat_id')
    ids=request.GET.get('id')
    page=request.GET.get('page')
    # class A():
    #  def s(self):
    #    jiabin.save_s()
    # a=A()
    # a.s()
    try:
        up=models.jiabin_m.objects.filter(id=ids)
        up.update(username=usernames,cat_event_id=cat_id)


    except:
        transaction.rollback()

    return  HttpResponseRedirect("/jiabin/home/"+str(int(page))+"")
def homex(request):
    xpage=request.GET.get('xpage')
    return  HttpResponseRedirect("/jiabin/home/"+str(xpage)+"")

def update_event(request):
    count=int(len(new_add_event))
    if count>0:
        t=0
        while t<count:
          try:
            event_c=models.NewEventParagraph.objects.get(id=new_add_event[t])
            event_id=event_c.cat_name_id
            event_username=[]
            event_username.extend(fenci.fenci(str(event_c.txt)))
            x=0
            while x<int(len(event_username)):
                models.jiabin_m.objects.create(
                    username=event_username[x],
                    cat_event_id=event_id,
                    baikeURL='http://baike.baidu.com/search/word?word='+str(event_username[x])+'',
                    homeurl='http://www.huodongjia.com/event-'+str(event_id)+'.html'

                )
                x+=1

            t+=1
            models.jiabin_event.objects.filter(id=1).update(all_event=new_add_event[t-1])
          except:
              pass
              return HttpResponse('更新错误')
    else:
        return HttpResponse('没有更新')
    return HttpResponse('成功')

def shaomiao(request):
    count=int(1192337-935285)
    if count>0:
        t=935285
        while t<count+t:
          try:
            event_c=models.NewEventParagraph.objects.get(id=t)
            event_id=event_c.cat_name_id
            event_username=[]
            event_username.extend(fenci.fenci(str(event_c.txt)))
            x=0
            while x<int(len(event_username)):
                models.jiabinc.objects.create(
                    username=event_username[x],
                    cat_event_id=event_id,
                    baikeURL='http://baike.baidu.com/search/word?word='+str(event_username[x])+'',
                    homeurl='http://www.huodongjia.com/event-'+str(event_id)+'.html'

                )
                x+=1
          except:
              pass

              t+=1

    else:
        return HttpResponse('没有更新')
    return HttpResponse('成功')

def add_event(request):
  try:
    username=request.GET.get('username')
    event_id=request.GET.get('event_id')
    models.jiabin_m.objects.create(
        username=username,
        cat_event_id=event_id,
        homeurl='http://www.huodongjia.com/event-'+str(event_id)+'.html',
        baikeURL='http://baike.baidu.com/search/word?word='+str(username)+''

    )
  except:
      return HttpResponse('更新错误')
  return HttpResponse('更新成功')

def jiabin_list_index(request,page=1):
    offset = 12
    new = request.GET.get('new',False)
    try:
        ret = cache.get('jiabin_data_%s' % page)
    except:
        ret = None

    new = True
    if new or not ret:
        ret = {}
        lstJiabin = models.jiabin_m.objects.all()
        #获取所有嘉宾信息
        
        
        totalpage = lstJiabin.count()/offset
        page_obj = pagination.pagination(request.GET,totalpage,page,offset,request.get_full_path())
        (curpage,offset) = page_obj.getCurpageOffset()
        start = (curpage-1)*offset
        end = curpage*offset
        (firstPage,lastPage,prePage,nextPage,pageList) = page_obj.getPageInfo()

        ret['firstPage'] = firstPage
        ret['lastPage'] = lastPage
        ret['prePage'] = prePage
        ret['nextPage'] = nextPage
        ret['pageList'] = pageList


        lstInfo = []
        # return HttpResponse(json.dumps(ret),content_type='application/json')
        for ji in lstJiabin[start:end]:
            mid_dct = {}

            mid_dct['jiabin_name'] = ji.username
            mid_dct['jiabin_intro'] = ji.introduce
            mid_dct['jiabin_pic'] = ji.imgs if ji.imgs else None
            mid_dct['jiabin_company'] = ji.company
            mid_dct['jiabin_position'] = ji.position
            mid_dct['user_id'] = ji.id
            mid_dct['title'] = ji.title
            mid_dct['time_now'] = ji.begin_time
            mid_dct['picurl'] = ji.picurl
            try:
                mid_dct['old_event_guest'] = ji.jiabin_id if ji.jiabin_id else None
            except:
                mid_dct['old_event_guest'] =None

            mid_dct['guest_invitation_url'] ='/jiabin/index/guest_invitation/'+str(ji.id)+'/'
            lstInfo.append(mid_dct)

        ret['data'] = lstInfo

        cache.set('jiabin_data_%s' % page,ret,86400)



    #return HttpResponse(json.dumps(ret),content_type='application/json')
    return render_to_response('guest_list.html',ret,context_instance=RequestContext(request))

def jiabin_guest_invitation(request,page):

    all_value=models.jiabin_m.objects.get(id=int(page))
    lstInfo = []
    ret = {}

    mid_dct = {}

    mid_dct['jiabin_name'] = all_value.username
    mid_dct['jiabin_intro'] = all_value.introduce
    mid_dct['jiabin_pic'] = all_value.imgs if all_value.imgs else None
    mid_dct['jiabin_company'] = all_value.company
    mid_dct['jiabin_position'] = all_value.position
    mid_dct['user_id'] = all_value.id
    mid_dct['picurl'] = all_value.picurl
    lstInfo.append(mid_dct)

    ret['data'] = lstInfo

    cache.set('jiabin_data_%s' % page,ret,86400)
    return render_to_response('guest_info.html',ret,context_instance=RequestContext(request))

def Search_guest(request,page=1):
    keywords = request.GET.get('keyword','')
    jiabin_value = models.jiabin_m.objects.filter(username__icontains=keywords)
    ret = {}
    lstInfo = []

    offset = 12
    new = request.GET.get('new',False)
    try:
        ret = cache.get('jiabin_data_%s' % page)
    except:
        ret = None

    new = True
    if new or not ret:
        ret = {}
        lstJiabin = models.jiabin_m.objects.all()
        #获取所有嘉宾信息


        totalpage = lstJiabin.count()/offset
        page_obj = pagination.pagination(request.GET,totalpage,page,offset,request.get_full_path())
        (curpage,offset) = page_obj.getCurpageOffset()
        start = (curpage-1)*offset
        end = curpage*offset
        (firstPage,lastPage,prePage,nextPage,pageList) = page_obj.getPageInfo()

        ret['firstPage'] = firstPage
        ret['lastPage'] = lastPage
        ret['prePage'] = prePage
        ret['nextPage'] = nextPage
        ret['pageList'] = pageList


        lstInfo = []
    for ji in jiabin_value[start:end]:
            mid_dct = {}

            mid_dct['jiabin_name'] = ji.username
            mid_dct['jiabin_intro'] = ji.introduce
            mid_dct['jiabin_pic'] = ji.imgs if ji.imgs else None
            mid_dct['jiabin_company'] = ji.company
            mid_dct['jiabin_position'] = ji.position

            mid_dct['user_id'] = ji.id
            mid_dct['picurl'] = ji.picurl
            try:
                mid_dct['old_event_guest'] = ji.jiabin_id.event_name if ji.jiabin_id.event_name else None
            except:
                mid_dct['old_event_guest'] =None
            try:
                mid_dct['old_event_time'] = ji.jiabin_id.event_end_time if ji.jiabin_id.event_end_time else None
            except:
                mid_dct['old_event_time'] =None

            mid_dct['guest_invitation_url'] ='/jiabin/index/guest_invitation/'+str(ji.id)+'/'
            lstInfo.append(mid_dct)

    ret['data'] = lstInfo

    cache.set('jiabin_data_%s' % page,ret,86400)



    #return HttpResponse(json.dumps(ret),content_type='application/json')
    return render_to_response('search_guest.html',ret,context_instance=RequestContext(request))

def cat_guest1(request,page=1):
    offset = 12
    new = request.GET.get('new',False)
    try:
        ret = cache.get('jiabin_data_%s' % page)
    except:
        ret = None

    new = True
    if new or not ret:
        ret = {}
        lstJiabin = models.jiabin_m.objects.all()
        #获取所有嘉宾信息


        totalpage = lstJiabin.count()/offset
        page_obj = pagination.pagination(request.GET,totalpage,page,offset,request.get_full_path())
        (curpage,offset) = page_obj.getCurpageOffset()
        start = (curpage-1)*offset
        end = curpage*offset
        (firstPage,lastPage,prePage,nextPage,pageList) = page_obj.getPageInfo()

        ret['firstPage'] = firstPage
        ret['lastPage'] = lastPage
        ret['prePage'] = prePage
        ret['nextPage'] = nextPage
        ret['pageList'] = pageList


        lstInfo = []
        # return HttpResponse(json.dumps(ret),content_type='application/json')
        for ji in lstJiabin[start:end]:
            mid_dct = {}

            mid_dct['jiabin_name'] = ji.username
            mid_dct['jiabin_intro'] = ji.introduce
            mid_dct['jiabin_pic'] = ji.imgs if ji.imgs else None
            mid_dct['jiabin_company'] = ji.company
            mid_dct['jiabin_position'] = ji.position
            mid_dct['user_id'] = ji.id
            mid_dct['picurl'] = ji.picurl
            try:
                mid_dct['old_event_guest'] = ji.jiabin_id if ji.jiabin_id else None
            except:
                mid_dct['old_event_guest'] =None

            mid_dct['guest_invitation_url'] ='/guest_invitation/'+str(ji.id)+'/'
            lstInfo.append(mid_dct)

        ret['data'] = lstInfo

        cache.set('jiabin_data_%s' % page,ret,86400)



    #return HttpResponse(json.dumps(ret),content_type='application/json')
    return render_to_response('guest.html',ret,context_instance=RequestContext(request))

def jiabin_edit(request):
    user_id=request.GET.get('user_id')
    lstJiabin = models.jiabin_m.objects.get(id=user_id)
    ret = {}
    ret['user_id'] = user_id
    ret['imgs_u'] = lstJiabin.imgs
    ret['event_id'] = lstJiabin.cat_event_id
    ret['event_username'] = lstJiabin.username
    ret['event_name'] = lstJiabin.title
    ret['event_cat'] = lstJiabin.cat
    ret['event_bigentime'] = lstJiabin.begin_time
    ret['event_endtime'] = lstJiabin.end_time
    ret['event_baikeURL'] = lstJiabin.baikeURL
    ret['event_homeurl'] = lstJiabin.homeurl
    ret['event_introduce'] = lstJiabin.introduce


    return render_to_response('user_edit.html',ret,context_instance=RequestContext(request))


def event_user_save(request):
    user_file=request.GET.get('user_file')
    user_id=request.GET.get('user_id')
    event_username=request.GET.get('event_username')
    event_id=request.GET.get('event_id')
    event_name=request.GET.get('event_name')
    event_cat=request.GET.get('event_cat')
    event_baikeURL=request.GET.get('event_baikeURL')
    event_homeurl=request.GET.get('event_homeurl')
    event_introduce=request.GET.get('event_introduce')
    is_com=request.GET.get('is_com')
    models.jiabin_m.objects.filter(id=user_id).update(
    imgs=user_file,
    username=event_username,
    introduce=event_introduce,
    homeurl=event_homeurl,
    baikeURL=event_baikeURL,
    cat=event_cat,
    cat_event_id=event_id,
    title=event_name,
    recommend=is_com
    )
    return HttpResponse('成功')
@csrf_exempt
def img_user_save(request):
    try:

        reqfile = request.FILES['user_file']#picfile要和html里面一致

        img = Image.open(reqfile)

        img.thumbnail((500,500),Image.ANTIALIAS)#对图片进行等比缩放

        img.save("/data/web/ftptest/log_save/jiabin/static/images/a.png","png")#保存图片

    except Exception,e:

       return HttpResponse("Error %s"%e)#异常，查看报错信息


    return HttpResponse('成功')

def cat_guest(request,page=1):
    offset = 24
    new = request.GET.get('new',False)
    try:
        ret = cache.get('jiabin_data_%s' % page)
    except:
        ret = None

    new = True
    if new or not ret:
        ret = {}
        try:
            lstJiabin = models.jiabin_m.objects.filter(recommend=1)
        except:
            lstJiabin=None
        lstJiabin_it=[]
        lstJiabin_energy=[]
        lstJiabin_medica=[]
        lstJiabin_academic=[]
        lstJiabin_financial=[]
        lstJiabin_retail=[]
        lstJiabin_commed=[]
        lstJiabin_agro=[]
        lstJiabin_other=[]
        lstJiabin_bus=[]
        lstJiabin_it.extend(models.jiabin_m.objects.filter(cat=7))
        lstJiabin_energy.extend(models.jiabin_m.objects.filter(cat=8))
        lstJiabin_medica.extend( models.jiabin_m.objects.filter(cat=9))
        lstJiabin_academic.extend( models.jiabin_m.objects.filter(cat=10))
        lstJiabin_financial.extend(models.jiabin_m.objects.filter(cat=13))
        lstJiabin_retail.extend(models.jiabin_m.objects.filter(cat=14))
        lstJiabin_commed.extend(models.jiabin_m.objects.filter(cat=15))
        lstJiabin_agro.extend(models.jiabin_m.objects.filter(cat=18))
        lstJiabin_other.extend(models.jiabin_m.objects.filter(cat=84))
        lstJiabin_bus.extend(models.jiabin_m.objects.filter(cat=10000))
        #获取所有嘉宾信息

        list1=[]
        list2=[]
        list3=[]
        list4=[]
        list5=[]
        list6=[]
        list7=[]

        totalpage = lstJiabin.count()/offset
        page_obj = pagination.pagination(request.GET,totalpage,page,offset,request.get_full_path())
        (curpage,offset) = page_obj.getCurpageOffset()
        start = (curpage-1)*offset
        end = curpage*offset
        (firstPage,lastPage,prePage,nextPage,pageList) = page_obj.getPageInfo()

        ret['firstPage'] = firstPage
        ret['lastPage'] = lastPage
        ret['prePage'] = prePage
        ret['nextPage'] = nextPage
        ret['pageList'] = pageList

        mid_dct_m = {}
        lstInfo = [0]*7
        # return HttpResponse(json.dumps(ret),content_type='application/json')
        for ji in lstJiabin[0:9]:
            mid_dct = {}
            mid_dct['cat_name'] = '推荐'
            mid_dct['jiabin_name'] = ji.username
            mid_dct['jiabin_intro'] = ji.introduce
            mid_dct['jiabin_pic'] = ji.imgs if ji.imgs else None
            mid_dct['jiabin_company'] = ji.company
            mid_dct['jiabin_position'] = ji.position
            mid_dct['user_id'] = ji.id
            mid_dct['title'] = ji.title
            mid_dct['time_now'] = ji.begin_time
            mid_dct['picurl'] = ji.picurl
            mid_dct['jiabin_more'] ='/jiabin/index/jiabin_cat_list_index/'+str(ji.cat)+'/'+str(1)+'/'
            if ji.begin_time>datetime.datetime.now() and ji.begin_time>datetime.date.today()+datetime.timedelta(-7):
                mid_dct['time_now']='有档期'
            elif ji.begin_time>datetime.datetime.now() and ji.end_time<ji.begin_time:
                mid_dct['time_now']='正在演讲'
            elif ji.begin_time>datetime.datetime.now() and ji.begin_time<datetime.date.today()+datetime.timedelta(-7):
                mid_dct['time_now']='即将演讲'
            else:
                mid_dct['time_now']='无档期'
            try:
                mid_dct['old_event_guest'] = ji.jiabin_id if ji.jiabin_id else None
            except:
                mid_dct['old_event_guest'] =None

            mid_dct['guest_invitation_url'] ='/jiabin/index/guest_invitation/'+str(ji.id)+'/'
            list7.append(mid_dct)
        lstInfo[0]=list7
        for ji in lstJiabin_it[0:6]:
            mid_dct = {}
            mid_dct['cat_name'] = '互联网IT'
            mid_dct['jiabin_name'] = ji.username
            mid_dct['jiabin_intro'] = ji.introduce
            mid_dct['jiabin_pic'] = ji.imgs if ji.imgs else None
            mid_dct['jiabin_company'] = ji.company
            mid_dct['jiabin_position'] = ji.position
            mid_dct['time_now'] = ji.begin_time
            mid_dct['title'] = ji.title
            mid_dct['picurl'] = ji.picurl
            mid_dct['jiabin_more'] ='/jiabin/index/jiabin_cat_list_index/'+str(ji.cat)+"/"+str(1)+'/'
            if ji.begin_time>datetime.datetime.now() and ji.begin_time>datetime.date.today()+datetime.timedelta(-7):
                mid_dct['time_now']='有档期'
            elif ji.begin_time>datetime.datetime.now() and ji.end_time<ji.begin_time:
                mid_dct['time_now']='正在演讲'
            elif ji.begin_time>datetime.datetime.now() and ji.begin_time<datetime.date.today()+datetime.timedelta(-7):
                mid_dct['time_now']='即将演讲'
            else:
                mid_dct['time_now']='无档期'
            try:
                mid_dct['old_event_guest'] = ji.jiabin_id.id if ji.jiabin_id else None
            except:
                mid_dct['old_event_guest'] =None

            mid_dct['guest_invitation_url'] ='/jiabin/index/guest_invitation/'+str(ji.id)+'/'
            list1.append(mid_dct)
        lstInfo[1]=list1



        for ji in lstJiabin_energy[0:6]:
            mid_dct = {}
            mid_dct['cat_name'] = '能源行业'
            mid_dct['jiabin_name'] = ji.username
            mid_dct['jiabin_intro'] = ji.introduce
            mid_dct['jiabin_pic'] = ji.imgs if ji.imgs else None
            mid_dct['jiabin_company'] = ji.company
            mid_dct['jiabin_position'] = ji.position
            mid_dct['user_id'] = ji.id
            mid_dct['title'] = ji.title
            mid_dct['time_now'] = ji.begin_time
            mid_dct['picurl'] = ji.picurl
            mid_dct['jiabin_more'] ='/jiabin/index/jiabin_cat_list_index/'+str(ji.cat)+"/"+str(1)+'/'
            if ji.begin_time>datetime.datetime.now() and ji.begin_time>datetime.date.today()+datetime.timedelta(-7):
                mid_dct['time_now']='有档期'
            elif ji.begin_time>datetime.datetime.now() and ji.end_time<ji.begin_time:
                mid_dct['time_now']='正在演讲'
            elif ji.begin_time>datetime.datetime.now() and ji.begin_time<datetime.date.today()+datetime.timedelta(-7):
                mid_dct['time_now']='即将演讲'
            else:
                mid_dct['time_now']='无档期'
            try:
                mid_dct['old_event_guest'] = ji.jiabin_id.id if ji.jiabin_id else None
            except:
                mid_dct['old_event_guest'] =None

            mid_dct['guest_invitation_url'] ='/jiabin/index/guest_invitation/'+str(ji.id)+'/'
            list2.append(mid_dct)
        lstInfo[4]=list2

        for ji in lstJiabin_medica[0:6]:
            mid_dct = {}
            mid_dct['cat_name'] = '医疗行业'
            mid_dct['jiabin_name'] = ji.username
            mid_dct['jiabin_intro'] = ji.introduce
            mid_dct['jiabin_pic'] = ji.imgs if ji.imgs else None
            mid_dct['jiabin_company'] = ji.company
            mid_dct['jiabin_position'] = ji.position
            mid_dct['user_id'] = ji.id
            mid_dct['title'] = ji.title
            mid_dct['time_now'] = ji.begin_time
            mid_dct['picurl'] = ji.picurl
            mid_dct['jiabin_more'] ='/jiabin/index/jiabin_cat_list_index/'+str(ji.cat)+''
            if ji.begin_time>datetime.datetime.now() and ji.begin_time>datetime.date.today()+datetime.timedelta(-7):
                mid_dct['time_now']='有档期'
            elif ji.begin_time>datetime.datetime.now() and ji.end_time<ji.begin_time:
                mid_dct['time_now']='正在演讲'
            elif ji.begin_time>datetime.datetime.now() and ji.begin_time<datetime.date.today()+datetime.timedelta(-7):
                mid_dct['time_now']='即将演讲'
            else:
                mid_dct['time_now']='无档期'
            try:
                mid_dct['old_event_guest'] = ji.jiabin_id.id if ji.jiabin_id else None
            except:
                mid_dct['old_event_guest'] =None


            list3.append(mid_dct)
        lstInfo[3]=list3


        for ji in lstJiabin_academic[0:6]:

            mid_dct_m['cat_name'] = '学术'
            mid_dct_m['jiabin_name'] = ji.username
            mid_dct_m['jiabin_intro'] = ji.introduce
            mid_dct_m['jiabin_pic'] = ji.imgs if ji.imgs else None
            mid_dct_m['jiabin_company'] = ji.company
            mid_dct_m['jiabin_position'] = ji.position
            mid_dct_m['user_id'] = ji.id
            mid_dct_m['title'] = ji.title
            mid_dct_m['time_now'] = ji.begin_time
            mid_dct_m['picurl'] = ji.picurl
            mid_dct_m['jiabin_more'] ='/jiabin/index/jiabin_cat_list_index/'+str(ji.cat)+"/"+str(1)+'/'
            if ji.begin_time>datetime.datetime.now() and ji.begin_time>datetime.date.today()+datetime.timedelta(-7):
                mid_dct_m['time_now']='有档期'
            elif ji.begin_time>datetime.datetime.now() and ji.end_time<ji.begin_time:
                mid_dct_m['time_now']='正在演讲'
            elif ji.begin_time>datetime.datetime.now() and ji.begin_time<datetime.date.today()+datetime.timedelta(-7):
                mid_dct_m['time_now']='即将演讲'
            else:
                mid_dct_m['time_now']='无档期'
            try:
                mid_dct_m['old_event_guest'] = ji.jiabin_id.id if ji.jiabin_id else None
            except:
                mid_dct_m['old_event_guest'] =None

            mid_dct['guest_invitation_url'] ='/jiabin/index/guest_invitation/'+str(ji.id)+'/'
            # lstInfo[6]=mid_dct_m


        for ji in lstJiabin_financial[0:6]:
            mid_dct = {}
            mid_dct['cat_name'] = '金融财经'
            mid_dct['jiabin_name'] = ji.username
            mid_dct['jiabin_intro'] = ji.introduce
            mid_dct['jiabin_pic'] = ji.imgs if ji.imgs else None
            mid_dct['jiabin_company'] = ji.company
            mid_dct['jiabin_position'] = ji.position
            mid_dct['user_id'] = ji.id
            mid_dct['title'] = ji.title
            mid_dct['time_now'] = ji.begin_time
            mid_dct['picurl'] = ji.picurl
            mid_dct['jiabin_more'] ='/jiabin/index/jiabin_cat_list_index/'+str(ji.cat)+"/"+str(1)+'/'
            if ji.begin_time>datetime.datetime.now() and ji.begin_time>datetime.date.today()+datetime.timedelta(-7):
                mid_dct['time_now']='有档期'
            elif ji.begin_time>datetime.datetime.now() and ji.end_time<ji.begin_time:
                mid_dct['time_now']='正在演讲'
            elif ji.begin_time>datetime.datetime.now() and ji.begin_time<datetime.date.today()+datetime.timedelta(-7):
                mid_dct['time_now']='即将演讲'
            else:
                mid_dct['time_now']='无档期'
            try:
                mid_dct['old_event_guest'] = ji.jiabin_id.id if ji.jiabin_id else None
            except:
                mid_dct['old_event_guest'] =None

            mid_dct['guest_invitation_url'] ='/jiabin/index/guest_invitation/'+str(ji.id)+'/'
            list4.append(mid_dct)
        lstInfo[2]=list4



        for ji in lstJiabin_retail[0:6]:

            mid_dct_m['cat_name'] ='零售'
            mid_dct_m['jiabin_name'] = ji.username
            mid_dct_m['jiabin_intro'] = ji.introduce
            mid_dct_m['jiabin_pic'] = ji.imgs if ji.imgs else None
            mid_dct_m['jiabin_company'] = ji.company
            mid_dct_m['jiabin_position'] = ji.position
            mid_dct_m['user_id'] = ji.id
            mid_dct_m['title'] = ji.title
            mid_dct_m['time_now'] = ji.begin_time
            mid_dct['picurl'] = ji.picurl
            if ji.begin_time>datetime.datetime.now() and ji.begin_time>datetime.date.today()+datetime.timedelta(-7):
                mid_dct_m['time_now']='有档期'
            elif ji.begin_time>datetime.datetime.now() and ji.end_time<ji.begin_time:
                mid_dct_m['time_now']='正在演讲'
            elif ji.begin_time>datetime.datetime.now() and ji.begin_time<datetime.date.today()+datetime.timedelta(-7):
                mid_dct_m['time_now']='即将演讲'
            else:
                mid_dct_m['time_now']='无档期'
            try:
                mid_dct_m['old_event_guest'] = ji.jiabin_id.id if ji.jiabin_id else None
            except:
                mid_dct_m['old_event_guest'] =None

            mid_dct_m['guest_invitation_url'] ='/jiabin/index/guest_invitation/'+str(ji.id)+'/'
            # lstInfo[6]=mid_dct_m


        for ji in lstJiabin_commed[0:6]:

            mid_dct_m['cat_name'] = '公共服务'
            mid_dct_m['jiabin_name'] = ji.username
            mid_dct_m['jiabin_intro'] = ji.introduce
            mid_dct_m['jiabin_pic'] = ji.imgs if ji.imgs else None
            mid_dct_m['jiabin_company'] = ji.company
            mid_dct_m['jiabin_position'] = ji.position
            mid_dct_m['user_id'] = ji.id
            mid_dct['title'] = ji.title
            mid_dct['picurl'] = ji.picurl
            mid_dct_m['time_now'] = ji.begin_time
            if ji.begin_time>datetime.datetime.now() and ji.begin_time>datetime.date.today()+datetime.timedelta(-7):
                mid_dct_m['time_now']='有档期'
            elif ji.begin_time>datetime.datetime.now() and ji.end_time<ji.begin_time:
                mid_dct_m['time_now']='正在演讲'
            elif ji.begin_time>datetime.datetime.now() and ji.begin_time<datetime.date.today()+datetime.timedelta(-7):
                mid_dct_m['time_now']='即将演讲'
            else:
                mid_dct_m['time_now']='无档期'
            try:
                mid_dct_m['old_event_guest'] = ji.jiabin_id.id if ji.jiabin_id else None
            except:
                mid_dct_m['old_event_guest'] =None

            mid_dct_m['guest_invitation_url'] ='/jiabin/index/guest_invitation/'+str(ji.id)+'/'
            # lstInfo[7]=mid_dct



        for ji in lstJiabin_agro[0:6]:
            mid_dct = {}
            mid_dct['cat_name'] = '农业农林'
            mid_dct['jiabin_name'] = ji.username
            mid_dct['jiabin_intro'] = ji.introduce
            mid_dct['jiabin_pic'] = ji.imgs if ji.imgs else None
            mid_dct['jiabin_company'] = ji.company
            mid_dct['jiabin_position'] = ji.position
            mid_dct['user_id'] = ji.id
            mid_dct['title'] = ji.title
            mid_dct['picurl'] = ji.picurl
            mid_dct['time_now'] = ji.begin_time
            mid_dct['jiabin_more'] ='/jiabin/index/jiabin_cat_list_index/'+str(ji.cat)+"/"+str(1)+'/'
            if ji.begin_time>datetime.datetime.now() and ji.begin_time>datetime.date.today()+datetime.timedelta(-7):
                mid_dct['time_now']='有档期'
            elif ji.begin_time>datetime.datetime.now() and ji.end_time<ji.begin_time:
                mid_dct['time_now']='正在演讲'
            elif ji.begin_time>datetime.datetime.now() and ji.begin_time<datetime.date.today()+datetime.timedelta(-7):
                mid_dct['time_now']='即将演讲'
            else:
                mid_dct['time_now']='无档期'
            try:
                mid_dct['old_event_guest'] = ji.jiabin_id.id if ji.jiabin_id else None
            except:
                mid_dct['old_event_guest'] =None

            mid_dct['guest_invitation_url'] ='/jiabin/index/guest_invitation/'+str(ji.id)+'/'
            list5.append(mid_dct)
        lstInfo[5]=list5

        for ji in lstJiabin_bus[0:6]:
            # mid_dct = {}
            mid_dct_m['cat_name'] = '商业'
            mid_dct_m['jiabin_name'] = ji.username
            mid_dct_m['jiabin_intro'] = ji.introduce
            mid_dct_m['jiabin_pic'] = ji.imgs if ji.imgs else None
            mid_dct_m['jiabin_company'] = ji.company
            mid_dct_m['jiabin_position'] = ji.position
            mid_dct_m['user_id'] = ji.id
            mid_dct_m['title'] = ji.title
            mid_dct_m['picurl'] = ji.picurl
            mid_dct_m['time_now'] = ji.begin_time
            try:
                if ji.begin_time>datetime.datetime.now() and ji.begin_time>datetime.date.today()+datetime.timedelta(-7):
                    mid_dct_m['time_now']='有档期'
                elif ji.begin_time>datetime.datetime.now() and ji.end_time<ji.begin_time:
                    mid_dct_m['time_now']='正在演讲'
                elif ji.begin_time>datetime.datetime.now() and ji.begin_time<datetime.date.today()+datetime.timedelta(-7):
                    mid_dct_m['time_now']='即将演讲'
                else:
                    mid_dct_m['time_now']='无档期'
            except:
                pass
            try:
                mid_dct_m['old_event_guest'] = ji.jiabin_id.id if ji.jiabin_id else None
            except:
                mid_dct_m['old_event_guest'] =None

            mid_dct_m['guest_invitation_url'] ='/jiabin/index/guest_invitation/'+str(ji.id)+'/'
            # lstInfo[9]=mid_dct

        for ji in lstJiabin_other[0:3]:
            # mid_dct = {}
            mid_dct_m['cat_name'] = '其他行业'
            mid_dct_m['jiabin_name'] = ji.username
            mid_dct_m['jiabin_intro'] = ji.introduce
            mid_dct_m['jiabin_pic'] = ji.imgs if ji.imgs else None
            mid_dct_m['jiabin_company'] = ji.company
            mid_dct_m['jiabin_position'] = ji.position
            mid_dct_m['user_id'] = ji.id
            mid_dct_m['title'] = ji.title
            mid_dct_m['picurl'] = ji.picurl
            mid_dct_m['time_now'] = ji.begin_time
            mid_dct_m['jiabin_more'] ='/jiabin/index/jiabin_cat_list_index/'+str(8340)+"/"+str(1)+'/'
            if ji.begin_time>datetime.datetime.now() and ji.begin_time>datetime.date.today()+datetime.timedelta(-7):
                mid_dct_m['time_now']='有档期'
            elif ji.begin_time>datetime.datetime.now() and ji.end_time<ji.begin_time:
                mid_dct_m['time_now']='正在演讲'
            elif ji.begin_time>datetime.datetime.now() and ji.begin_time<datetime.date.today()+datetime.timedelta(-7):
                mid_dct_m['time_now']='即将演讲'
            else:
                mid_dct_m['time_now']='无档期'
            try:
                mid_dct_m['other_old_event_guest'] = ji.jiabin_id.id if ji.jiabin_id else None
            except:
                mid_dct_m['other_old_event_guest'] =None

            mid_dct_m['other_guest_invitation_url'] ='/jiabin/index/guest_invitation/'+str(ji.id)+'/'

            list6.append(mid_dct_m)
        lstInfo[6]=list6
            # lstInfo[6]=lstInfo[6]+lstInfo[9]+lstInfo[7]+lstInfo[6]








        ret['data'] = lstInfo

        cache.set('jiabin_data_%s' % page,ret,86400)




    # return HttpResponse(json.dumps(ret),content_type='application/json')
    # return render_to_response('guest_list.html',ret,context_instance=RequestContext(request))
    return render_to_response('guest_cat.html',ret,context_instance=RequestContext(request))

def jiabin_cat_list_index(request,cat_n,page=1):
    offset = 12
    new = request.GET.get('new',False)
    try:
        ret = cache.get('jiabin_data_%s' % page)
    except:
        ret = None
    global  cat_names
    cat_names={}

    if cat_n==7:

        cat_name='互联网IT'
        cat_names['cat_name']=cat_name
    elif cat_n==8:

        cat_name='能源行业'
        cat_names['cat_name']=cat_name
    elif cat_n==9:

        cat_name='医疗行业'
        cat_names['cat_name']=cat_name
    elif cat_n==13:

        cat_name='金融财经'
        cat_names['cat_name']=cat_name
    elif cat_n==18:

        cat_name='农业农林'
        cat_names['cat_name']=cat_name
    elif cat_n==8340:

        cat_name='其它行业'
        cat_names['cat_name']=cat_name



    new = True
    global  lstJiabin
    if new or not ret:
        ret = {}
        if int(cat_n)==8340:
            lstJiabin = models.jiabin_m.objects.filter(Q(cat=1 )| Q(cat=10)| Q(cat=14)| Q(cat=15)| Q(cat=84)| Q(cat=10000))
            totalpage = lstJiabin.count()/offset
            page_obj = pagination.pagination(request.GET,totalpage,page,offset,request.get_full_path())
            (curpage,offset) = page_obj.getCurpageOffset()
            start = (curpage-1)*offset
            end = curpage*offset
            (firstPage,lastPage,prePage,nextPage,pageList) = page_obj.getPageInfo()

            ret['firstPage'] = firstPage
            ret['lastPage'] = lastPage
            ret['prePage'] = prePage
            ret['nextPage'] = nextPage
            ret['pageList'] = pageList


            lstInfo = []
            # return HttpResponse(json.dumps(ret),content_type='application/json')
            for ji in lstJiabin[start:end]:
                mid_dct = {}

                mid_dct['jiabin_name'] = ji.username
                mid_dct['jiabin_intro'] = ji.introduce
                mid_dct['jiabin_pic'] = ji.imgs if ji.imgs else None
                mid_dct['jiabin_company'] = ji.company
                mid_dct['jiabin_position'] = ji.position
                mid_dct['user_id'] = ji.id
                mid_dct['title'] = ji.title
                mid_dct['time_now'] = ji.begin_time
                mid_dct['picurl'] = ji.picurl


                try:
                    mid_dct['old_event_guest'] = ji.jiabin_id.id if ji.jiabin_id else None
                except:
                    mid_dct['old_event_guest'] =None

                mid_dct['guest_invitation_url'] ='/jiabin/index/guest_invitation/'+str(ji.id)+'/'

                if ji.begin_time>datetime.datetime.now() and ji.begin_time>datetime.date.today()+datetime.timedelta(-7):
                    mid_dct['time_now']='有档期'
                elif ji.begin_time>datetime.datetime.now() and ji.end_time<ji.begin_time:
                    mid_dct['time_now']='正在演讲'
                elif ji.begin_time>datetime.datetime.now() and ji.begin_time<datetime.date.today()+datetime.timedelta(-7):
                    mid_dct['time_now']='即将演讲'
                else:
                    mid_dct['time_now']='无档期'
                lstInfo.append(mid_dct)

            ret['data'] = lstInfo

            cache.set('jiabin_data_%s' % page,ret,86400)
            #return HttpResponse(json.dumps(ret),content_type='application/json')
            return render_to_response('guest_list.html',ret,context_instance=RequestContext(request))

        else:


            lstJiabin = models.jiabin_m.objects.filter(cat=cat_n)
            #获取所有嘉宾信息


            totalpage = lstJiabin.count()/offset
            page_obj = pagination.pagination(request.GET,totalpage,page,offset,request.get_full_path())
            (curpage,offset) = page_obj.getCurpageOffset()
            start = (curpage-1)*offset
            end = curpage*offset
            (firstPage,lastPage,prePage,nextPage,pageList) = page_obj.getPageInfo()

            ret['firstPage'] = firstPage
            ret['lastPage'] = lastPage
            ret['prePage'] = prePage
            ret['nextPage'] = nextPage
            ret['pageList'] = pageList


            lstInfo = []
            # return HttpResponse(json.dumps(ret),content_type='application/json')
            for ji in lstJiabin[start:end]:
                mid_dct = {}

                mid_dct['jiabin_name'] = ji.username
                mid_dct['jiabin_intro'] = ji.introduce
                mid_dct['jiabin_pic'] = ji.imgs if ji.imgs else None
                mid_dct['jiabin_company'] = ji.company
                mid_dct['jiabin_position'] = ji.position
                mid_dct['user_id'] = ji.id
                mid_dct['title'] = ji.title
                mid_dct['picurl'] = ji.picurl
                mid_dct['time_now'] = ji.begin_time
                if ji.begin_time>datetime.datetime.now() and ji.begin_time>datetime.date.today()+datetime.timedelta(-7):
                    mid_dct['time_now']='有档期'
                elif ji.begin_time>datetime.datetime.now() and ji.end_time<ji.begin_time:
                    mid_dct['time_now']='正在演讲'
                elif ji.begin_time>datetime.datetime.now() and ji.begin_time<datetime.date.today()+datetime.timedelta(-7):
                    mid_dct['time_now']='即将演讲'
                else:
                    mid_dct['time_now']='无档期'
                try:
                    mid_dct['old_event_guest'] = ji.jiabin_id.id if ji.jiabin_id else None
                except:
                    mid_dct['old_event_guest'] =None

                mid_dct['guest_invitation_url'] ='/jiabin/index/guest_invitation/'+str(ji.id)+'/'
                lstInfo.append(mid_dct)
                # lstInfo.append(cat_names)

            ret['data'] = lstInfo

            cache.set('jiabin_data_%s' % page,ret,86400)
            # return HttpResponse(json.dumps(ret),content_type='application/json')
            return render_to_response('guest_list.html',ret,context_instance=RequestContext(request))






@csrf_exempt
def send_guest_invitation(request):
    s=request.POST.get('company')
    s1=request.POST.get('meeting')
    s2=request.POST.get('id')
    s3=request.POST.get('name')
    s4=request.POST.get('mobilphone')
    s5=request.POST.get('message')
    s6=request.POST.get('guestName')
    # return HttpResponse(json.dumps({'data':in_companys,'success':1}),content_type='application/json')
    
    # in_meetings=request.POST.get('in_meeting')
    # event_ids=request.POST.get('event_id')
    # in_names=request.POST.get('in_name')
    # in_mobilphones=request.POST.get('in_mobilphone')
    # in_guests=request.POST.get('in_guest')
    # in_messages=request.POST.get('in_message')
    # s_1 = json.loads({'company':s})
    # s_2 = json.loads({'meeting':s1})
    # s_3 = json.loads({'id':s2})
    # s_4 = json.loads({'name':s3})
    # s_5 = json.loads({'mobilphone':s4})
    # s_6 = json.loads({'message':s5})
    # s_7 = json.loads({'guestName':s6})
    models.send_guest_invitation.objects.create(

        in_company=s,
        in_meeting=s1,
        event_id=s2,
        in_name=s3,
        in_mobilphone=s4,
        in_guest=s6,
        in_message=s5
        )

    return HttpResponse(json.dumps({'msg':'','success':1}),content_type='application/json')

    return HttpResponse('0')