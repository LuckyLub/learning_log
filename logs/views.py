from django.shortcuts import render
from logs.models import Topic, Entry
# Create your views here.


def topic_overview(requests):
    context = {}

    my_dict = {}
    for entry in Entry.objects.all():
        if entry.topic not in my_dict:
            my_dict[entry.topic] = [entry.__str__()]
        else:
            my_dict[entry.topic].append(entry.__str__())

    context["input"] = my_dict

    return render(requests, "topic_overview.html", context)


def topic(requests, topic):
    context = {}
    context["topic"] = topic
    context["entries"] = []

    for entry in Entry.objects.all():
        if entry.topic.text.lower() == topic.lower():
            context["entries"].append(entry.text)

    if context["entries"] == []:
        context["entries"].append("No entries for this class")

    return render(requests, "topic.html", context)
