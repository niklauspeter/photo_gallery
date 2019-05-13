from django.shortcuts import render, redirect
from django.http  import HttpResponse, Http404


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

    return render(request, 'all-pics/past-pics.html', {"date": date})

def pics_of_day(request):
    date = dt.date.today()
    return render(request, 'all-pics/today-pics.html', {"date": date,})