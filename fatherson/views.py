from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
import math


@csrf_exempt
def show(request):
    error = False
    if request.method == "POST":

        father_name = request.POST['father_name']
        father_year = int(request.POST['father_year'])

        son_name = request.POST['son_name']
        son_year = int(request.POST['son_year'])

        if father_name and father_year and son_name and son_year:

            delta = int(math.fabs(father_year - son_year))
            return render(request, 'fatherson/calc.html', {
                'father_name': father_name,
                'son_name': son_name,
                'father_age': delta*2,
                'son_age': delta
            })

        error = True

    return render(request, 'fatherson/show.html', {
        'error': error,
    })
