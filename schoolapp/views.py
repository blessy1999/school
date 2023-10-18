from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages, auth
from .models import Department,Course,FormSubmission

# Create your views here.
def school(request):
    return render(request,'index.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('home')
        else:
            messages.info(request,"invalid credentials")
            return redirect('login')
    return render(request,'login.html')

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        cpassword = request.POST['cpassword']

        if password == cpassword:
            # Check if the username is already taken
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username is already taken.')
            else:
                user = User.objects.create_user(username=username, password=password)
                user.save()
                messages.success(request, 'Registration successful.')
                return redirect('login')
        else:
            messages.error(request, 'Passwords do not match.')

        return redirect('register')  # Redirect to the registration page
    else:
        return render(request, 'register.html')

def logout(request):
    auth.logout(request)
    return redirect('/')


def home(request):
    departments = Department.objects.all()
    courses=Course.objects.all()

    if request.method == 'POST':
        name = request.POST['name']
        dob = request.POST['dob']
        age = request.POST['age']
        gender = request.POST['gender']
        phone = request.POST['phone']
        email = request.POST['email']
        address = request.POST['address']
        department_id = request.POST['department']
        course_id = request.POST['course']  # Assuming 'course' is a foreign key
        purpose = request.POST['purpose']
        materials = request.POST.getlist('materials')

        department = Department.objects.get(pk=department_id)
        # You should also retrieve the course object based on 'course_id'
        course = Course.objects.get(pk=course_id)

        form_submission = FormSubmission(
            name=name,
            dob=dob,
            age=age,
            gender=gender,
            phone_number=phone,
            email=email,
            address=address,
            department=department,
            course=course,  # Assign the course object
            purpose=purpose
        )
        form_submission.save()

        # form_submission.materials.set(materials)

        return redirect('success_page')  # Redirect to a success page

    context = {
        'departments': departments,
        'courses':courses,
    }

    return render(request, 'home.html', context)


def success_page(request):
    return render(request, 'success.html')