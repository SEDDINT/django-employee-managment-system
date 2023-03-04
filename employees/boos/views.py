from django.shortcuts import redirect, render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *

# Create your views here.


def home(request):
    # employee = Employee(name='salah', gander=Employee.male, email='text@gmail.com',
    #                     phonenum='040404040404', address='home', manager=None)
    # employee2 = Employee(name='hala', gander=Employee.female, email='text@gmail.com',
    #                      phonenum='040404040404', address='home', manager=None)
    # employee.save()
    # employee2.save()
    employees = Employee.objects.all()

    department = Department.objects.filter(pk=1)

    jobs = Department.get_jobs(department)

    context = {'employees': employees, 'jobs': jobs}
    return HttpResponse(context)
    # return render(request, 'show_employee.html', context)


def add_employee(request):
    submitted = False
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_employee?submitted=True')
    else:
        form = EmployeeForm
        if 'submitted' in request.GET:
            submitted = True
            messages.success(
                request, ('Employee was added successfully'))
            return redirect('home')

    context = {'form': form, 'submitted': submitted}
    return render(request, 'add_employee.html', context)


def update_employee(request, employee_id):

    employee = Employee.objects.get(pk=employee_id)
    form = EmployeeForm(request.POST or None, instance=employee)

    if form.is_valid():
        form.save()
        return redirect('home')

    context = {'employee': employee, 'form': form, 'employee_id': employee_id}
    return render(request, 'update_employee.html', context)


def delete_employee(request, employee_id):
    employee = Employee.objects.get(pk=employee_id)
    employee.delete()
    messages.success(
        request, (f'Employee: {employee}, recodrd was deleted'))
    return redirect('home')


def employee_info_table(request):
    employees = Employee.objects.all()
    context = {'employees': employees}
    return render(request, 'employee_info_table.html', context)


def search(request):
    context = {}
    if request.method == 'POST':
        searched = request.POST['searched']
        employees = Employee.objects.filter(name__contains=searched)
        context = {'searched': searched, 'employees': employees}
        return render(request, 'search.html', context)
    else:
        return render(request, 'search.html')
