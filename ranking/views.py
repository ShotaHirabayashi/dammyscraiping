from django.shortcuts import render
from django.views.generic import TemplateView ,ListView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import barRank , BarRankCSV
import csv
from io import TextIOWrapper, StringIO
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.


class topView(TemplateView):
    template_name = "index.html"



class barRankListView(ListView):
    model = BarRankCSV
    template_name = "list.html"
    paginate_by = 5



def upload(request):
    if 'csv' in request.FILES:
        form_data = TextIOWrapper(request.FILES['csv'].file, encoding='utf-8')
        csv_file = csv.reader(form_data)
        for line in csv_file:
            #csvの読み込みとしてBarRankCSV()が必要
            barRankCSV = BarRankCSV()
            barRankCSV.title = line[0]
            barRankCSV.kanaTitle = line[1]
            barRankCSV.address = line[2]
            barRankCSV.promotion = line[3]
            barRankCSV.save()
    return render(request, 'upload.html')


def paginate_queryset(request, queryset, count):
    paginator = Paginator(queryset, count)
    page = request.GET.get('page')
    try:
        page_obj = paginator.page(page)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)
    return page_obj



def loginfunc(request):
    if request.method == 'POST':
        username2 = request.POST['username']
        password2 = request.POST['password']
        user = authenticate(request, username=username2, password=password2)
        if user is not None:
            login(request, user)
            return redirect('/list/')
        else:
            return redirect('/login/')
    return render(request, 'login.html')


def signupfunc(request):
    if request.method == 'POST':
        username2 = request.POST['username']
        password2 = request.POST['password']
        try:
            User.objects.get(username=username2)
            return render(request, 'signup.html', {'error':'このユーザーは登録されています'})
        except:
            user = User.objects.create_user(username2, '', password2)
            return render(request, 'login.html')
    return render(request, 'signup.html', {'some':100})


@login_required
def listfunc(request):
    object_list = BarRankCSV.objects.all()
    return render(request, 'list.html', {'object_list':object_list})


