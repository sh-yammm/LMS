from django.shortcuts import render

from django.views import View

from .forms import InstructorForm

from students.forms import ProfileForm

# Create your views here.

class InstructorRegisterView(View):

    def get(self,request,*args,**kwargs):

        profile_form = ProfileForm()

        instructor_form = InstructorForm()

        data = {
            'profile_form' : profile_form,
            'instructor_form' : instructor_form
        }

        return render(request,'instructors/instructor-register.html', context = data)
