from django.shortcuts import render, HttpResponse
from django.conf import settings
from applications import sql

from obspy.imaging.beachball import beachball
import matplotlib
matplotlib.use('agg')


# Create your views here.
def focal(request):
    # if request.method == 'POST':

    context = {
        'title': 'Focal Mechanism'
    }
    return render(request, 'focal/focal.html', context)


def get_focal(request):
    start_date = request.POST['startdate']
    end_date = request.POST['enddate']
    min_mag = request.POST['minmag']
    max_mag = request.POST['maxmag']
    min_depth = request.POST['mindepth']
    max_depth = request.POST['maxdepth']
    north = request.POST['north']
    south = request.POST['south']
    east = request.POST['east']
    west = request.POST['west']

    events = sql.list_moment_tensor(start_time=start_date, end_time=end_date)
    for event in events:
        mt = [event['st1'], event['d1'], event['r1']]
        color = None
        if event['depth'] <= 60:
            color = 'r'
        elif 60 < event['depth'] <= 300:
            color = 'y'
        else:
            color = 'b'

        beachball(mt,
                  size=200,
                  linewidth=2,
                  facecolor=color,
                  outfile=f"{settings.MEDIA_ROOT}/focal/{event['publicID']}.png")

    context = {
        'events': events,
        'title': 'Focal Mechanism'
    }

    return render(request, 'focal/GetFocal.html', context=context)
