from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.db.models import Q
from .models import Message
from .forms import MessageForm

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
    messages = Message.objects.filter( Q(sender=request.user), 
                                       Q(receiver=another_user))
    messages.update(seen=True)

    if not users:
        users = User.objects.all()
    
    form = MessageForm()
    
    context = {
        "another_user": another_user,
        "messages": messages,
        "users": users,
        "form": form
    }

    return render(request, "privatechat.html", context)


def search_user(request):
    return load_messages_home(request)

@login_required
def send_message(request):
    if request.method == "POST":
        print("hello")
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
