from urls_short.models import URL
from urls_short.forms import UrlForm
from django.shortcuts import redirect, get_object_or_404, render
import random 
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import string
import datetime


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
                url_new.url_short = 'domain.com/'+url_generator()
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


    return render(request, 'index.html', {'urls': urls, 'form': form})



def remove(request, pk):
    app = URL.objects.get(id=pk)
    if request.method == "POST":
        app.delete()
        return redirect('urls_short:index')
    else:
        return render(request, 'delete.html')


def detail(request, pk):
    url = URL.objects.get(id=pk)
    return render(request, 'detail.html', {'url': url})

def edit(request, pk):
    url = get_object_or_404(URL, pk=pk)
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
    return render(request, 'edit.html', {'form': form})