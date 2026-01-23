from django.shortcuts import render,redirect
from .forms import EventModelForm,ParticipantModelForm,CategoryModelForm
from django.contrib import messages
from .models import Event,Category,Participant
import datetime
# Create your views here.

def home(request):
    events=Event.objects.all()
    return render(request,'base.html',{"events":events})

def dashboard(request):
    total_participant=Participant.objects.count()
    total_event=Event.objects.count()
    today=datetime.datetime.now().date()
    upcomming_event=Event.objects.filter(date__gte=today).count()
    past_event=Event.objects.filter(date__lt=today).count()
    today_event=Event.objects.filter(date=today)
    
    context={
        'total_participant':total_participant,
        'total_event':total_event,
        'upcomming_event':upcomming_event,
        'past_event':past_event,
        'today_event':today_event
    }
    return render(request,'dashboard.html',context)

def event_list(request):
    event=Event.objects.all()
    return render(request,"event_list.html",{'event':event})

def create_event(request):
    event_form=EventModelForm()
    if request.method=='POST':
        event_form=EventModelForm(request.POST)
        if event_form.is_valid():
            event_form.save()
            messages.success(request,'Create event successfully')
            return redirect('create-event')
    context={
        'event_form':event_form,
        'heading':'Create Event'
    }
    return render(request,'event_form.html',context)

def update_event(request,id):
    event_form=Event.objects.get(id=id)
    up_form=EventModelForm(instance=event_form)
    if request.method=='POST':
        up_form=EventModelForm(request.POST,instance=event_form)
        if up_form.is_valid():
            up_form.save()
            messages.success(request,"Update Event successfully")
            return redirect("event-list")
    context={
        'up_form':up_form,
        'heading':'Update Event' 
    }
    return render(request,"event_form.html",context)

def delete_event(request,id):
    del_event=Event.objects.get(id=id)
    del_event.delete()
    messages.success(request,'Delete Event')
    return redirect('event-list')


def category_list(request):
    category=Category.objects.all()
    
    return render(request,'category.html',{"category":category})
    
    

def create_category(request):
    category_form=CategoryModelForm()
    if request.method=='POST':
        category_form=CategoryModelForm(request.POST)
        if category_form.is_valid():
            category_form.save()
            messages.success(request,"Create category successfully")
            return redirect("create-category")
     
    context={
        'category_form':category_form,
        'heading':'Create Category'
    }   
    return render(request,'event_form.html',context)

def update_category(request,id):
    up_category=Category.objects.get(id=id)
    category_form=CategoryModelForm(instance=up_category)
    if request.method=='POST':
        category_form=CategoryModelForm(request.POST, instance=up_category)
        if category_form.is_valid():
            category_form.save()
            messages.success(request,"Update category successfully")
            return redirect("category-list")
        
    context={
        "category_form":category_form,
        "heading":"Update Category"
    }
    return render(request,"event_form.html",context)

def delete_category(request,id):
    category=Category.objects.get(id=id)
    category.delete()
    messages.success(request,"Category Delete Successfully")
    return redirect("category-list")


def participant_list(request):
    participant=Participant.objects.all()
    
    return render(request,"participant_list.html",{'participant':participant})

def create_participant(request):
    participant=ParticipantModelForm()
    if request.method=="POST":
        participant=ParticipantModelForm(request.POST)
        if participant.is_valid():
            participant.save()
            messages.success(request,"Participant create successfully")
            return redirect('create-participant')
            
    context={
        "participant":participant,
        'heading':"Create Participant"
    }
    return render(request,"event_form.html",context)

def update_participant(request,id):
    participant=Participant.objects.get(id=id)
    up_participant=ParticipantModelForm(instance=participant)
    if request.method=="POST":
        up_participant=ParticipantModelForm(request.POST,instance=participant)
        if up_participant.is_valid():
            up_participant.save()
            messages.success(request,"Update Participant Successfully")
            return redirect('participant-list')
    context={
        "up_participant":up_participant,
        "heading":"Update Participant"
    } 
    return render(request,"event_form.html",context)  

def delete_participant(request,id):
    participant=Participant.objects.get(id=id)
    participant.delete()
    messages.success(request,"Delete Participant Successfully")
    return redirect('participant-list')


def category_event(request,id):
    category=Category.objects.get(id=id)
    cevent=Event.objects.filter(category=category)
    return render(request,"category.html",{"cevent":cevent})




