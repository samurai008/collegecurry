from django.shortcuts import render
from django.views.generic import TemplateView
from django.views import View

# Create your views here.
class IndexView(TemplateView):
    template_name = "thewebapp/home/index.html"

class CollegeListView(TemplateView):
    template_name = "thewebapp/collegelist/results.html"

class CollegeDetailView(TemplateView):
    template_name = "thewebapp/collegelist/collegedetail.html"

# template for ajax modal in college detail page
class DetailParticularView(View):
    template_name = "thewebapp/partials/college-particulars.html"

    def get(self, request):

        return render(
            request, self.template_name
        )

class LoginView(View):
    template_name = "thewebapp/login.html"

    def get(self, request):
        return render(
            request, self.template_name
        )

class RegisterView(View):
    template_name = "thewebapp/register.html"

    def get(self, request):
        return render(
            request, self.template_name
        )
