from django.shortcuts import render
from logs.models import Topic, Entry
from django.urls import reverse
from django.http import HttpResponseRedirect

from .forms import TopicForm, EntryForm

# Create your views here.


def topic_overview(requests):
    context = {}

    my_dict = {}
    for topic in Topic.objects.all():
        my_dict[topic] = []

    for entry in Entry.objects.all():
        my_dict[entry.topic].append(entry.__str__())

    context["input"] = my_dict

    return render(requests, "topics_overview.html", context)


def topic(request, topic):

    context = {}
    entries = []

    for entry in Entry.objects.all():
        if entry.topic.text.lower() == topic.lower():
            entries.append(entry.text)

    if entries is False:
        entries.append("No entries for this class")

    if request.method != 'POST':
        form = EntryForm()
    else:
        form = EntryForm(request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = Topic.objects.get(text=topic)
            new_entry.save()
            return HttpResponseRedirect(reverse("logs:topic", args=[topic]))

    context["form"] = form
    context["URL"] = request.path
    context["entries"] = entries
    context["topic"] = topic

    return render(request, "topic_specific_overview.html", context)


def new_topic(request):
    message = "Enter your new topic here."
    if request.method != 'POST':
        form = TopicForm()
    else:
        form = TopicForm(request.POST)

        # collect all topic to later check if the new entered topic does not already exist.
        topic_list = []
        for topic in Topic.objects.all():
            topic_list.append(topic.text.lower())

        # check if form is valid and if topic does not already exists, make the new topic.
        if form.is_valid() and form.data["text"].lower() not in topic_list:
            form.save()
            return HttpResponseRedirect(reverse("logs:index"))
        # if it does exist, inform the user.
        elif form.is_valid():
            message = "The entered topic already exists. Enter your new topic here."

    context = {'form': form, "message": message}

    return render(request, 'new_topic.html', context)
