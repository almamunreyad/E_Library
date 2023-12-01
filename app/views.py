from django.shortcuts import render, HttpResponse
from .models import *
from django.core.paginator import Paginator

# Create your views here.
def home(request):
    missionDetails = Mission.objects.all()
    teamDetails = Team.objects.all()
    libraryDetails = Library.objects.all()
    data = {
        'missionDetails' : missionDetails,
        'teamDetails' : teamDetails,
        'libraryDetails': libraryDetails
    }
    return render(request, 'home.html', data)


def signup(request):
    if request.method == 'POST':
        image = request.FILES['image']
        name = request.POST['name']
        student_id = request.POST['student_id']
        email = request.POST['email']
        password = request.POST['password']
        c_password = request.POST['c_password']
        phone = request.POST['phone']
        semester = request.POST['semester']
        gender = request.POST['gender']
        maritalStatus = request.POST['maritalStatus']
        birth_date = request.POST['birth_date']
        blood_group = request.POST['blood_group']
        comment = request.POST['comment']
        
        # user already exist or not
        user = SignUp.objects.filter(email = email)
        
        if user:
            message = "User Already Exist !!"
            return render(request, 'signup.html', {'msg':message})
        else:
            if password == c_password:
                newuser = SignUp.objects.create(image = image, name = name, student_id = student_id, email = email, password = password, phone = phone, semester = semester, gender = gender, maritalStatus = maritalStatus, birth_date = birth_date, blood_group = blood_group, comment = comment)
                
                message = "User Registration Successfully !!"
                return render(request, 'login.html', {'msg':message})   
            else:
                message = "Password and Confirm Password are not matched !!"
                return render(request, 'signup.html', {'msg':message})

    return render(request, 'signup.html' )


def login(request):
    if request.method == 'POST':
        student_id = request.POST['student_id']
        password = request.POST['password']
        
        user = SignUp.objects.get(student_id=student_id)
        
        if user:
            if user.password == password:
                request.session['name']=user.name
                request.session['student_id']=user.student_id
                request.session['email']=user.email
                
                return render(request, 'home.html')
            else:
                message = "Password not match !!"
                return render(request, 'login.html', {'msg':message})
        else:
            message="User Does not exist !!"
            return render(request, 'signup.html', {'msg':message})
                
    return render(request, 'login.html')          


def logout(request):
    try:
        del request.session['student_id']
    except:
        return render(request, 'home.html')
    return render(request, 'home.html')


def about(request):
    aboutDetails = About.objects.all()
    data = {
        'aboutDetails' : aboutDetails
    }
    return render(request, 'about.html', data)
    

def contact(request):
    if request.method == 'POST':
        contact_name = request.POST['contact_name']
        contact_id = request.POST['contact_id']
        contact_email = request.POST['contact_email']
        contact_message = request.POST['contact_message']
        
        user = Contact.objects.filter(contact_email=contact_email)
        
        if user:
            message = " Message Already Send !!"
            return render(request, 'contact.html', {'msg':message})
        else:
            userMessage = Contact.objects.create(contact_name=contact_name, contact_id=contact_id, contact_email=contact_email, contact_message=contact_message )
        
            message = "We Got Your Message !!  Thank You !!"
            
            return render(request, 'contact.html', {'msg':message})
        
    return render(request, 'contact.html')


def cse(request):
    cseData = Cse.objects.all()#.order_by('-cse_book')
    category = Category_Cse.objects.all()
    # for search 
    info = request.GET.get('sub_search')
    # for id wise catagories
    categoryId = request.GET.get('category')
    
    
    if categoryId:
        cseData = Cse.objects.filter(cse_category=categoryId)
    else:
        cseData = Cse.objects.all()
        if info != None: # for search 
            cseData = Cse.objects.filter(cse_book__icontains = info)
   
    
    
    paginator = Paginator(cseData, 12)
    page_number = request.GET.get('page', 1)
    cseData = paginator.page(page_number)
    
    data = {
        'cseData': cseData, 
        'category' : category,
        
    }
    return render(request, 'cse.html', data)


def eee(request):
    eeeData = Eee.objects.all()#.order_by('-cse_book')
    category = Category_Eee.objects.all()
    # for search 
    info = request.GET.get('sub_search')
    # for id wise catagories
    categoryId = request.GET.get('category')
    
    
    if categoryId:
        eeeData = Eee.objects.filter(eee_category=categoryId)
    else:
        eeeData = Eee.objects.all()
        if info != None: # for search 
            eeeData = Eee.objects.filter(eee_book__icontains = info)
   
    
    
    paginator = Paginator(eeeData, 12)
    page_number = request.GET.get('page', 1)
    eeeData = paginator.page(page_number)
    
    data = {
        'eeeData': eeeData, 
        'category' : category,
        
    }
    return render(request, 'eee.html', data)

def bba(request):
    bbaData = Bba.objects.all()#.order_by('-cse_book')
    category = Category_Bba.objects.all()
    # for search 
    info = request.GET.get('sub_search')
    # for id wise catagories
    categoryId = request.GET.get('category')
    
    
    if categoryId:
        bbaData = Bba.objects.filter(bba_category=categoryId)
    else:
        bbaData = Bba.objects.all()
        if info != None: # for search 
            bbaData = Bba.objects.filter(bba_book__icontains = info)
   
    
    
    paginator = Paginator(bbaData, 12)
    page_number = request.GET.get('page', 1)
    bbaData = paginator.page(page_number)
    
    data = {
        'bbaData': bbaData, 
        'category' : category,
        
    }
    return render(request, 'bba.html', data)

def eng(request):
    engData = Eng.objects.all()#.order_by('-cse_book')
    category = Category_Eng.objects.all()
    # for search 
    info = request.GET.get('sub_search')
    # for id wise catagories
    categoryId = request.GET.get('category')
    
    
    if categoryId:
        engData = Eng.objects.filter(eng_category=categoryId)
    else:
        engData = Eng.objects.all()
        if info != None: # for search 
            engData = Eng.objects.filter(eng_book__icontains = info)
   
    
    
    paginator = Paginator(engData, 12)
    page_number = request.GET.get('page', 1)
    engData = paginator.page(page_number)
    
    data = {
        'engData': engData, 
        'category' : category,
        
    }
    return render(request, 'eng.html', data)

def law(request):
    lawData = Law.objects.all()#.order_by('-cse_book')
    category = Category_Law.objects.all()
    # for search 
    info = request.GET.get('sub_search')
    # for id wise catagories
    categoryId = request.GET.get('category')
    
    
    if categoryId:
        lawData = Law.objects.filter(law_category=categoryId)
    else:
        lawData = Law.objects.all()
        if info != None: # for search 
            lawData = Law.objects.filter(law_book__icontains = info)
   
    
    
    paginator = Paginator(lawData, 12)
    page_number = request.GET.get('page', 1)
    lawData = paginator.page(page_number)
    
    data = {
        'lawData': lawData, 
        'category' : category,
        
    }
    return render(request, 'law.html', data)

def civil(request):
    civilData = Civil.objects.all()#.order_by('-cse_book')
    category = Category_Civil.objects.all()
    # for search 
    info = request.GET.get('sub_search')
    # for id wise catagories
    categoryId = request.GET.get('category')
    
    
    if categoryId:
        civilData = Civil.objects.filter(civil_category=categoryId)
    else:
        civilData = Civil.objects.all()
        if info != None: # for search 
            civilData = Civil.objects.filter(civil_book__icontains = info)
   
    
    
    paginator = Paginator(civilData, 12)
    page_number = request.GET.get('page', 1)
    civilData = paginator.page(page_number)
    
    data = {
        'civilData': civilData, 
        'category' : category,
        
    }
    return render(request, 'civil.html', data)

def pharmacy(request):
    pharmacyData = Pharmacy.objects.all()#.order_by('-cse_book')
    category = Category_Pharmacy.objects.all()
    # for search 
    info = request.GET.get('sub_search')
    # for id wise catagories
    categoryId = request.GET.get('category')
    
    
    if categoryId:
        pharmacyData = Pharmacy.objects.filter(pharmacy_category=categoryId)
    else:
        pharmacyData = Pharmacy.objects.all()
        if info != None: # for search 
            pharmacyData = Pharmacy.objects.filter(pharmacy_book__icontains = info)
   
    
    
    paginator = Paginator(pharmacyData, 12)
    page_number = request.GET.get('page', 1)
    pharmacyData = paginator.page(page_number)
    
    data = {
        'pharmacyData': pharmacyData, 
        'category' : category,
        
    }
    return render(request, 'pharmacy.html', data)




def library(request):
    return render(request, 'home.html')
