# coding: utf-8
from django.http import HttpResponse,Http404,HttpResponseRedirect;
from django.shortcuts import render_to_response;
from photos.models import *;
from photos.forms import PhotoForm;
import json;
import time;
import hashlib;
from django.views.decorators.csrf import csrf_exempt;
import os;

def index(request):
    start = request.GET.get("start", 0);
    limit = request.GET.get("limit", 20);

    photos_list = Photo.objects.all().order_by('-create_time')[start:limit];
    res = [];
    for item in photos_list:
        photo = {
            "title" : item.title,
            "desc" : item.desc,
            "uname" : item.uname,
            "typeface" : item.typeface.name,
        };
        res.append(photo);
    res_str = json.dumps(res);
    return HttpResponse(res_str, content_type="application/json");

def detail(request, pid):
    try:
        pid = int(pid);
    except ValueError:
        raise Http404;
    try:
        photo = Photo.objects.get(id=pid);
    except Photo.DoesNotExist:
       return HttpResponse("No data.");
    res = {
        "title": photo.title,
        "desc": photo.desc,
        "uname": photo.uname,
        "typeface": photo.typeface.name,
    };
    return HttpResponse(json.dumps(res), content_type="application/json");

def process_photo(request, file):
    #原始图存储
    new_photo = Photo(title=request.POST["title"], desc=request.POST["desc"], img_origin=file);
    img_fullname = str(new_photo.img_origin.name);
    img_loc = str(img_fullname).find(".");
    img_ext = img_fullname[img_loc:];
    img_name = img_fullname[:img_loc];
    img_name = img_name+str(time.time());
    md5 = hashlib.md5(img_name.encode("utf-8")).hexdigest();
    new_photo.img_origin.name = md5[:10] + img_ext;
    #临时
    new_photo.uid = 1;
    new_photo.uname = "暗夜枫雪";
    new_photo.create_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime());
    new_photo.typeface_id = 1;
    new_photo.save();

def commit(request):
    if request.method == "POST":
        photo_form = PhotoForm(request.POST, request.FILES);
        if photo_form.is_valid():
            process_photo(request, request.FILES.get("photo"));
        return HttpResponseRedirect("/index/");
    else:
        photo_form = PhotoForm();
    return render_to_response('ct_photo.html', {"form":photo_form});