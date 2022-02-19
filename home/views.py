from email.mime import image
from xml.etree.ElementTree import PI
from django.shortcuts import redirect, render
from django.contrib.auth import logout

from .models import profile

from .form import *

def home(request):
    context = {'pictures' : pictureModel.objects.all()}
    return render(request,'home.html',context)

def picture_detail(request,slug):
    context = {}
    try:
        pic_object = pictureModel.objects.filter(slug=slug).first()
        context['pic_object'] = pic_object
    
    except Exception as e:
        print(e)
    return render(request,'picture_detail.html',context)

def post(request):
    context = {'form' : PictureForm}
    try:
        if request.method=="POST":
            form=PictureForm(request.POST)
            image=request.FILES['image']
            title=request.POST.get('title')
            user=request.user

            if form.is_valid() :
                content= form.cleaned_data['story']
            pictureModel.objects.create(user=user,title=title,image=image,story=content)
            return redirect('post')
    except Exception as e:
        print(e)

    return render(request,'post.html',context)

def login(request):
    return render(request,'login.html')

def logout_view(request):
    logout(request)
    return redirect('/')

def register(request):
    return render(request,'register.html')

def details(request):
    return render(request,'detail.html')

def see_pics(request):
    context = {}
    try:
        pic_objects = pictureModel.objects.filter(user = request.user)
        context['pic_objects'] = pic_objects
    except Exception as e:
        print(e)
    return render(request,'see_pics.html',context)

def pic_delete(request,id):
    try:
        pic_obj = pictureModel.objects.get(id=id)
        if pic_obj.user == request.user :
            pic_obj.delete()

    except Exception as e:
        print(e)
    return redirect('/see_pics/')




def verify(request,token):
    try:
        profile_obj = profile.objects.get(token = token)

        if profile_obj:
            profile_obj.is_verified = True
            profile_obj.save()
        
        return redirect('/success')
    
    except Exception as e:
        print(e)
    
    return redirect('/')


def success(request):
    return render(request,'success.html')