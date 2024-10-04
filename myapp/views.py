from django.shortcuts import render,redirect

# Create your views here.
from django.views.generic import View
from myapp.forms import EmployeeForm

from myapp.models import Employee

from django.contrib import messages

class EmployeeCreateView(View):
    def get(self,request,*args,**kwargs):
        form_instance=EmployeeForm()
        return render(request,"employee_create.html",{"form":form_instance})
    


    def post(self,request,*args,**kwargs):
        form_instance=EmployeeForm(request.POST)

        if form_instance.is_valid():
            data=form_instance.cleaned_data

            Employee.objects.create(
                name=data.get("name"),
                position=data.get("position"),
                office=data.get("office"),
                age=data.get("age"),
                start_date=data.get("start_date"),
                salary=data.get("salary"),
                
            )

            messages.success(request,"employee hasbeen added")
            return redirect("employee_list")
        else:
            messages.error(request,"failed to add")
            return render(request,"employee_create.html",{"form":form_instance})
        

class EmployeeListView(View):
    def get(self,request,*args,**kwargs):
        qs=Employee.objects.all()
        return render(request,"employee_list.html",{"employee":qs})
    


class EmployeeDetailView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        qs=Employee.objects.get(id=id)
        return render(request,"employee_details.html",{"employee":qs})
    


class EmployeeDeleteView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        Employee.objects.get(id=id).delete()

        messages.success(request,"employee deleted")

        return redirect("employee_list")
    

class EmployeeUpdateView(View):
    def get(self,request,*args,**kwargs):

        id=kwargs.get("pk")
        emp_object=Employee.objects.get(id=id)
        emp_dictionary={
            "name":emp_object.name,
            "position":emp_object.position,
            "office":emp_object.office,
            "age":emp_object.age,
            "start_date":emp_object.start_date,
            "salary":emp_object.salary,

        }
        form_instance=EmployeeForm(initial=emp_dictionary)
        
        return render(request,"emp_edit.html",{"form":form_instance})
    
    def post(self,request,*args,**kwargs):
        form_instance=EmployeeForm(request.POST)
        if form_instance.is_valid():
            data=form_instance.cleaned_data
            id=kwargs.get("pk")
            Employee.objects.filter(id=id).update(**data)
            messages.success(request,"employee hasbeen updated")

            return redirect("employee_list")
        else:
                        
            messages.error(request,"failed to updating employee")

            return render(request,"emp_edit.html",{"form":form_instance})
