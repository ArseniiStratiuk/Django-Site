import json
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.db.models import Q
from django.http.response import JsonResponse
from django.contrib.humanize.templatetags.humanize import naturaltime
from .models import Message
from .forms import MessageForm


def unread_msgs(request, sender):
    msgs = Message.objects.filter(Q(seen=False) & Q(receiver=request.user, sender=sender))
    return msgs.count()

@login_required
def load_messages_home(request):
    users = None
    if request.method=="POST":
        search = request.POST.get("searchuser")
        users = User.objects.filter(username__icontains=search)
        if users.count()>0:
            return load_messages(request, users[0].pk, users)
    return load_messages(request, request.user.pk, users)

@login_required
def load_messages(request, pk, users=None):
    another_user = get_object_or_404(User, pk=pk)
    messages = Message.objects.filter(Q(sender=request.user), 
                                      Q(receiver=another_user))
    messages.update(seen=True)

    messages = messages | Message.objects.filter(Q(sender=another_user), 
                                                 Q(receiver=request.user))

    if not users:
        users = User.objects.all()

    unread_num_dict = {}  # {"other_user": 19, ...}
    for user in users:
        unread_num_dict[user.username] = unread_msgs(request, user)
    
    context = {
        "another_user": another_user,
        "messages": messages,
        "users": users,
        "unread_msg": unread_num_dict
    }

    return render(request, "privatechat.html", context)

@login_required
def load_msgAJAX(request, pk):
    another_user = get_object_or_404(User, pk=pk)
    messages = Message.objects.filter(seen=False, receiver=request.user, sender=another_user)

    message_list = []
    for msg in messages:
        message_list.append({
            "sender": msg.sender.username, 
            "message": msg.text,
            "date_created": naturaltime(msg.date_created)
        })
        msg.seen = True
    messages.update(seen=True)

    if request.method == "POST":
        inMessage = json.loads(request.body)["message"]
        if inMessage:
            m = Message.objects.create(sender=request.user, receiver=another_user, text=inMessage)
            m.save()
            message_list.append({
                "sender": m.sender.username, 
                "message": m.text,
                "date_created": naturaltime(m.date_created)
            })
    return JsonResponse(message_list, safe=False)

def search_user(request):
    return load_messages_home(request)

@login_required
def send_message(request):
    if request.method == "POST":
        form = MessageForm(request.POST)
        if form.is_valid():
            recipient = User.objects.get(pk=request.POST['recipient'])
            text = form.cleaned_data["text"]
            message = Message(sender=request.user, receiver=recipient, text=text)
            message.save()
            return redirect("load_messages", pk=recipient.pk)
    else:
        form = MessageForm()
    return redirect("load_messages_home")
