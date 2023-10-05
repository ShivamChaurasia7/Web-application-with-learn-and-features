from django.shortcuts import render
from django.contrib import messages
from datetime import datetime
from .models import Contact, Full_stack_developer,UI_UX_Designer,Front_End_Developer,Technical_Lead
from .models import Feedback
from .models import Engineering_Manager

def index(request):
    return render(request,'index.html')

def base(request):
    return render(request,'base.html')

def tutorials(request):
    return render(request,'tutorials.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, phone=phone, desc=desc, date = datetime.today())
        contact.save()
        messages.success(request, 'Your response has been submitted.')
    return render(request,'contact.html')

def django(request):
    return render(request,'django.html')

def feedback(request):
    if request.method == "POST":
        name = request.POST.get('name')
        desc = request.POST.get('desc')
        feedback = Feedback(name=name,desc=desc)
        feedback.save()
        messages.success(request, 'Your feedback has been submitted.')
    return render(request,'feedback.html')

def flask(request):
    return render(request,'flask.html')

def html(request):
    return render(request,'html.html')    

def php(request):
    return render(request,'php.html')

def python(request):
    return render(request,'python.html')

def web(request):
    return render(request,'web.html')

def jobs(request):
    return render(request,'jobs.html')

def fs(request):
    if request.method == "POST":
        gender = request.POST.get('gender')
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        file = request.POST.get('file')
        Qualification=request.POST.get('Qualification')
        competence = request.POST.get('competence')
        city=request.POST.get('city')
        desc = request.POST.get('desc')       
        fs = Full_stack_developer(name=name,email=email, phone=phone,desc=desc,Qualification=Qualification,city=city,gender=gender,competence=competence,file=file)
        fs.save()
        messages.success(request, 'Your Application has been submitted, We will contact you soon...')
    return render(request,'fs.html')

def Ux(request):
    if request.method == "POST":
        gender = request.POST.get('gender')
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        file = request.POST.get('file')
        Qualification=request.POST.get('Qualification')
        competence = request.POST.get('competence')
        city=request.POST.get('city')
        desc = request.POST.get('desc')       
        Ux = UI_UX_Designer(name=name,email=email, phone=phone,desc=desc,Qualification=Qualification,city=city,gender=gender,competence=competence,file=file)
        Ux.save()
        messages.success(request, 'Your Application has been submitted, We will contact you soon...')
    return render(request,'Ux.html')

def technical(request):
    if request.method == "POST":
        gender = request.POST.get('gender')
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        file = request.POST.get('file')
        Qualification=request.POST.get('Qualification')
        competence = request.POST.get('competence')
        city=request.POST.get('city')
        desc = request.POST.get('desc')       
        technical =Technical_Lead (name=name,email=email, phone=phone,desc=desc,Qualification=Qualification,city=city,gender=gender,competence=competence,file=file)
        technical.save()
        messages.success(request, 'Your Application has been submitted, We will contact you soon...')
    return render(request,'technical.html')

def engineering(request):
    if request.method == "POST":
        gender = request.POST.get('gender')
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        file = request.POST.get('file')
        Qualification=request.POST.get('Qualification')
        competence = request.POST.get('competence')
        city=request.POST.get('city')
        desc = request.POST.get('desc')       
        engineering = Engineering_Manager(name=name,email=email, phone=phone,desc=desc,Qualification=Qualification,city=city,gender=gender,competence=competence,file=file)
        engineering.save()
        messages.success(request, 'Your Application has been submitted, We will contact you soon...')
    return render(request,'engineering.html')

def front(request):
    if request.method == "POST":
        gender = request.POST.get('gender')
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        file = request.POST.get('file')
        Qualification=request.POST.get('Qualification')
        competence = request.POST.get('competence')
        city=request.POST.get('city')
        desc = request.POST.get('desc')       
        front =Front_End_Developer(name=name,email=email, phone=phone,desc=desc,Qualification=Qualification,city=city,gender=gender,competence=competence,file=file)
        front.save()
        messages.success(request, 'Your Application has been submitted, We will contact you soon...')
    return render(request,'front.html')