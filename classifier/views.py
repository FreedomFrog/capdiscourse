from django.shortcuts import render, get_object_or_404, redirect, render_to_response
from classifier.models import UserText, Topic
from django.utils import timezone

from bokeh.plotting import figure, output_file, show
from bokeh.embed import components

def history_list(request):
    corpus = UserText.objects.filter(user=request.user, date__lte=timezone.now()).order_by('-date',)
    return render(request, 'classifier/history.html', {'corpus': corpus})


def about(request):
    return render(request, 'classifier/about.html')


def pos(request):
    if request.method == 'POST':
        corp = UserText()
        corp.text = request.POST.get('get_text')
        if request.user.is_authenticated:
            corp.user = request.user
        corp.save()
        corp.id_topics()
        if request.user.is_authenticated:
            return render(request, 'classifier/history.html')
        return render(request, 'classifier/pos.html', {'corp': corp})
    return render(request, 'classifier\home.html')


def live(request):
    data = Topic.objects.filter(user=request.user)
    if request.method == 'POST':
        topic = Topic()
        topic.topic = request.POST.get('get_text')
        topic.entity = request.POST.get('get_entity')
        topic.user = request.user
        topic.save()

        return render(request, 'classifier/live.html', {'data': data})

    return render(request, 'classifier/live.html', {'data': data})


def topics_list(request):
    topics = Topic.objects.all()
    return render(request, 'classifier/topics.html', {'topics': topics})


def usertext_detail(request, pk):
    usertext = get_object_or_404(UserText, pk=pk)
    return render(request, 'classifier/corpus_detail.html', {'usertext': usertext})
