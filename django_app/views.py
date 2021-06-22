from django.shortcuts import render, HttpResponse, redirect

def index(request):
    return render(request, "dojo_survey.html")

def result(request):

    name_from_form = request.POST['name']
    location_from_form = request.POST['location']
    language_from_form = request.POST['language']
    learn_from_form = request.POST['learn']
    comment_from_form = request.POST['comment']

    context = {
        'name_on_template':name_from_form,
        'location_on_template':location_from_form,
        'language_on_template':language_from_form,
        'learn_on_template':learn_from_form,
        'comment_on_template':comment_from_form,
    }

    return render(request, "survey_results.html", context)
