from django import forms
from .models import StudentDetails, stdInsert,Receipt,AccountDetails  # Import your models

class StudentDetailsForm(forms.ModelForm):
    class Meta:
        model = StudentDetails
        fields = '__all__'
        
class AccountDetailsForm(forms.ModelForm):
    class Meta:
        model = AccountDetails
        fields = '__all__'        

class StdInsertForm(forms.ModelForm):
    class Meta:
        model = stdInsert
        fields = '__all__'


from django import forms

class ReceiptForm(forms.ModelForm):
    class Meta:
        model = Receipt
        fields = '__all__'
        widgets = {
            'date': forms.DateInput(attrs={'placeholder': 'YYYY-MM-DD'}),
        }


from .models import CommonStudent, Table1, Table2  

def create_dynamic_form(model_class):
    class DynamicForm(forms.ModelForm):
        class Meta:
            model = model_class
            fields = '__all__'
    return DynamicForm

# Now, you can dynamically create forms for any model
Table1Form = create_dynamic_form(Table1)
Table2Form = create_dynamic_form(Table2)
CommonStudentForm = create_dynamic_form(CommonStudent)

