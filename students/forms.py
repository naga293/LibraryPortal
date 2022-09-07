from django import forms
from.models import Book,School,Student


class AddStudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'gender', 'school','books','mail','no_of_pages_read']

class AddBookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['name','author']

class AddSchoolForm(forms.ModelForm):
    class Meta:
        model = School
        fields = ['name','phone_number']

class SearchStudentForm(forms.Form):
    INPUT_CHOICES = (
        ('Name', 'Name'),
        ("ID","ID")
        )
    input_type=forms.ChoiceField(label='Input Type',choices =INPUT_CHOICES, required=False)
    input = forms.CharField(label='Input', max_length=100)
