from urls_short.models import URL
from urls_short.forms import UrlForm
from django.shortcuts import redirect, get_object_or_404, render
import random 
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import string
import datetime
from django.conf import settings
from django.contrib.auth.models import User



def url_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def update_bd():
    date_del = datetime.date.today() - datetime.timedelta(days=14)
    URL.objects.filter(date_of_create__lte=date_del).delete()
    return URL.objects.all()


def urls_list(request, pk=0):
    urls = update_bd()
    #urls = URL.objects.all()

    if request.method == "POST":
        form = UrlForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            url_new = URL()
            url_new.url_max = data['url_max']

            if data['url_short'] == '':
                url_new.url_short = settings.SITE_URL + "/" + url_generator()
            else:
                url_new.url_short = data['url_short']
            url_new.save()

            return redirect('urls_short:index')
    else:
        form = UrlForm()

    
    if pk != 0:
        app = URL.objects.get(id=pk)  
        app.click += 1
        app.save()
        return redirect(app.url_max)

    paginator = Paginator(urls, 5)
    page = request.GET.get('page')

    try:
        urls = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        urls = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        urls = paginator.page(paginator.num_pages)

    user = request.user

    return render(request, 'index.html', {'urls': urls, 'form': form, 'user':user})



def remove(request, pk):
    user = request.user
    app = URL.objects.get(id=pk)
    if request.method == "POST":
        app.delete()
        return redirect('urls_short:index')
    else:
        return render(request, 'delete.html', {'user': user})



def detail(request, pk):
    url = URL.objects.get(id=pk)
    user = request.user
    return render(request, 'detail.html', {'url': url, 'user':user})



def edit(request, pk):
    url = get_object_or_404(URL, pk=pk)
    user = request.user
    if request.method == "POST":
        form = UrlForm(request.POST, instance=url)
        if form.is_valid():
            url = form.save(commit=False)
            data = form.cleaned_data
            url.url_max = data['url_max']
            url.url_short = data['url_short']
            url.save()
            return redirect('urls_short:index')
    else:
        form = UrlForm(instance=url)
    return render(request, 'edit.html', {'form': form, 'user':user})


def share(request, pk):
    user = request.user
    users = User.objects.exclude(id=user.id)
    if request.method == "GET":
        app = URL.objects.get(id=pk) 
        app.click += 1
        app.save()

    return render(request, 'share.html', {'user':user, 'users': users})
