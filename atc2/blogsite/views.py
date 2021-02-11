from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from .models import Post1
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserRegisterForm,PostForm
from django.views.generic import (ListView,TemplateView)
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
username1 = ""



def create(request):
    context = {}
    print("hiiiiiiiiiiiiiiiiiiiiiiiiii")
    if request.method == "POST":
        print("sdfsdfsdf")
        form = PostForm(request.POST, request.FILES)
        print(form)
        print(form.is_valid())
        if form.is_valid():
            print("ggggggg")
            name = form.cleaned_data.get("title")
            img = form.cleaned_data.get("image1")
            text = form.cleaned_data.get("text")
            ty = form.cleaned_data.get("is_public")
            print(name,"  ",ty," ",text," ",request.user," ",img)
            global username1
            username1 = request.user
            obj = Post1(
                title=name,
                image1=img,
                text=text,
                is_public= ty,
                username=request.user
            )
            obj.save()
            print(obj)
            return redirect("index")

    else:
        print("hiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii")
        form = PostForm()
    context['form'] = form
    return render(request, "blogsite/post_create.html", context)
#################### index#######################################
def index(request):
    model = Post1
    mo_pri = model.objects.filter(username=request.user,is_public=False)
    mo_pub = model.objects.filter(is_public=True)
    pri_ls = list(mo_pri.values())
    pub_ls = list(mo_pub.values())
    print(pri_ls)
    print("log")
    post_dict_private={}
    post_dict_public={}

    for i in range(len(pri_ls )):
        post_dict_private[pri_ls [i]['title']] = (pri_ls [i]['text'],pri_ls [i]['image1'].replace('blogsite',""))

    for i in range(len(pub_ls )):
        post_dict_public[pub_ls [i]['title']] = (pub_ls [i]['text'],pub_ls [i]['image1'].replace('blogsite',""))

    print(post_dict_private)
    print("log2")
    print(post_dict_private)


    return render(request,'blogsite/index.html',{'post_dict_private': post_dict_private,'post_dict_public':post_dict_public} )


########### register here #####################################
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            global username1
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            username1 = username
            ######################### mail system ####################################

            ##################################################################
            messages.success(request, f'Your account has been created ! You are now able to log in')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'blogsite/register.html', {'form': form, 'title': 'reqister here'})


################ login forms###################################################
def Login(request):
    if request.method == 'POST':

        # AuthenticationForm_can_also_be_used__

        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            form = login(request, user)
            messages.success(request, f' wecome {username} !!')
            return redirect('index')
        else:
            messages.info(request, f'account done de not exit plz sign in')
    form = AuthenticationForm()
    return render(request, 'blogsite/login.html', {'form': form, 'title': 'log in'})


def search_res(request):

    if request.method == 'POST':
        model = Post1
        search = request.POST['search_r']
        print(search)
        temp = model.objects.filter(is_public=True,title=search)
        search_li = list(temp.values())
        print("search_li :  ",search_li)
        fetch_dict = {}
        for i in range(len(search_li)):
            fetch_dict[search_li[i]['title']] = (search_li[i]['text'], search_li[i]['image1'].replace('blogsite', ""))

        print(fetch_dict)

        return render(request,'blogsite/search_results.html',{'fetch_dict': fetch_dict})

