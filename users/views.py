from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import Group,User
from django.contrib.auth import login ,logout
from django.contrib.auth.decorators import login_required,user_passes_test
from django.contrib import messages
from django.contrib.auth.tokens import default_token_generator
from event.models import *
from users.forms import(
    CustomRegistrationForm,
    Loginform,
    AssignRoleForm,
    CreateGroupForm
)
from users.decorators import is_admin
from django.db.models import Prefetch
import datetime
# from .utils import send_activation_email

# Create your views here.
def is_admin(user):
    return user.groups.filter(name='Admin').exists()
def is_organizer(user):
    return user.groups.filter(name='Organizer').exists()
def is_participant(user):
    return user.groups.filter(name='Participant').exists()



def sign_up(request):
    form=CustomRegistrationForm()
    
    if request.method=='POST':
        form=CustomRegistrationForm(request.POST)
        if form.is_valid():
            print("FORM VALID ✅")
            
            print("Password1:", form.cleaned_data['password1'])
            user=form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.is_active=False
            user.save()
            
            group,created=Group.objects.get_or_create(name='Participant')
            user.groups.add(group)
            
            messages.success(request,"Check email to active account")
            return redirect("sign_in")
        else:
            print("FORM NOT VALID ❌")
            print(form.errors) 
    return render(request,"signup.html",{"form":form})
    # return render(request,"dashboard/admin_dashboard.html")
            

def sign_in(request):
    form=Loginform()
    if request.method=="POST":
        form= Loginform(data=request.POST)
        if form.is_valid():
            user=form.get_user()
            login(request,user)
            
            if user.groups.filter(name='Admin').exists():
                return redirect('admin_dashboard')
            elif user.groups.filter(name='Organizer').exists():
                return redirect('organizer_dashboard')
            else:
                return redirect('participant_dashboard')
        
    return render(request,"login.html",{"form":form})
   
@login_required 
def sign_out(request):
    # if request.method=='POST':
    logout(request)
    return redirect("sign_in")
        

def activate_user(request,user_id,token):
    try:
        user=User.objects.get(id=user_id)
        if default_token_generator.check_token(user,token):
            user.is_active=True
            user.save()
            return redirect('sign_in')
        return HttpResponse("Invalid token")
    except User.DoesNotExist:
        return HttpResponse("user not found")

@user_passes_test(is_admin, login_url='no_permission')
def admin_dashboard(request):

    total_user = User.objects.count()
    total_event = Event.objects.count()

    today = datetime.date.today()

    upcoming_event = Event.objects.filter(date__gte=today).count()
    past_event = Event.objects.filter(date__lt=today).count()

    users = User.objects.prefetch_related('groups')

    context = {
        "total_user": total_user,
        "total_event": total_event,
        "upcoming_event": upcoming_event,
        "past_event": past_event,
        "users": users,
    }

    return render(request, "dashboard/admin_dashboard.html", context)



@user_passes_test(is_admin,login_url='no_permission')
def assign_role(request,user_id):
    user=User.objects.get(id=user_id)
    form=AssignRoleForm()
    
    if request.method=='POST':
        form=AssignRoleForm(request.POST)
        if form.is_valid():
            role=form.cleaned_data.get('role')
            user.groups.clear()
            user.groups.add(role)
            
            messages.success(request,f"User {user.username} assigned to {role.name} role")
            return redirect('admin_dashboard')
    return render(request,'assign_role.html',{'form':form})
 
@user_passes_test(is_admin, login_url='no_permission')
def create_group(request):
    form=CreateGroupForm()
    
    if request.method=='POST':
        form=CreateGroupForm(request.POST)
        
        if form.is_valid():
            group=form.save()
            messages.success(request,f"Group {group.name} cretaed successfully")
            return redirect('create_group')
    return render(request,'create_group.html',{"form":form})
 
@user_passes_test(is_admin, login_url='no_permission')
def group_list(request):
    groups=Group.objects.prefetch_related('permissions').all() 
    return render(request,'group_list.html',{'groups':groups})            

@user_passes_test(is_organizer, login_url='no_permission')
def organizer_dashboard(request):
    total_event = Event.objects.count()

    today = datetime.date.today()

    upcoming_event = Event.objects.filter(date__gte=today).count()
    past_event = Event.objects.filter(date__lt=today).count()

    users = User.objects.prefetch_related('groups')
    event=Event.objects.all()
    context = {
        "total_event": total_event,
        "upcoming_event": upcoming_event,
        "past_event": past_event,
        "users": users,
        "event":event
    }

    return render(request, "dashboard/organizer_dashboard.html", context)
   


@user_passes_test(is_participant, login_url='no_permission')
def participant_dashboard(request):
    return render(request,'dashboard/participant_dashboard.html')


def no_permission(request):
    return render(request, 'no_permission.html')