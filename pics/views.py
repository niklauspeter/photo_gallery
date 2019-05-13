from django.shortcuts import render, redirect
from django.http  import HttpResponse, Http404

import datetime as dt
from .models import Image

# Create your views here.
def welcome(request):
    return render(request, 'welcome.html')


def past_days_pics(request, past_date):

    try:
        # Converts data from the string Url
        date = dt.datetime.strptime(past_date, '%Y-%m-%d').date()

    except ValueError:
        # Raise 404 error when ValueError is thrown
        raise Http404()
        assert False

    if date == dt.date.today():
        return redirect(pics_of_day)

    pics = Image.days_pics(date)
    

    return render(request, 'all-pics/past-pics.html', {"date": date,"pics":pics})

def pics_of_day(request):
    date = dt.date.today()
    pics = Image.todays_pics()
    return render(request, 'all-pics/today-pics.html', {"date": date,"pics":pics})


def search_results(request):

    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        searched_images_by_category = Image.search_by_category(search_term)
        searched_images_by_location = Image.search_by_location(search_term)
        results = [*searched_images_by_category, *searched_images_by_location]
        message = f"{search_term}"

        return render(request, 'all-pics/search.html',{"message":message,"images": results})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all-pics/search.html',{"message":message})