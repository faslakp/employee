from django import forms



class EmployeeForm(forms.Form):
    name=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))

    position=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))

    office=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))

    age=forms.IntegerField(widget=forms.NumberInput(attrs={"class":"form-control"}))

    start_date=forms.DateField(widget=forms.DateTimeInput(attrs={"class":"form-control"}))
    
    salary=forms.IntegerField(widget=forms.NumberInput(attrs={"class":"form-control"}))

    def clean(self):
      cleaned_data=super().clean()

      salary=cleaned_data.get("salary")

      if salary<15000 or salary>50000:
        
        error_message="salary shoul be in between 15000 and 50000"
        self.add_error("salary",error_message)
    
