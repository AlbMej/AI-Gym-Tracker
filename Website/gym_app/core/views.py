from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import FormView, TemplateView
from gym_app.core.models import Exercise,User
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated  # <-- Here
from rest_framework.response import Response
from gym_app.core.serializers import UserSerializer
from .forms import CustomFieldForm
from rest_framework import permissions
from .api_auth import ApiAuth
# Create your views here.

def home(request):
    count = User.objects.count()
    return render(request, 'home.html', {
        'count': count
    })


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {
        'form': form
    })


class LoanForm(LoginRequiredMixin, FormView):
    form_class = CustomFieldForm
    success_url = reverse_lazy('success')
    template_name = 'form.html'


class SuccessView(TemplateView):
    template_name = 'success.html'


class DeniedView(TemplateView):
    template_name = 'denied.html'


class PreapprovedView(TemplateView):
    template_name = 'preapproved.html'


@login_required
def submit_form(request):
    form = CustomFieldForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            amount = form.cleaned_data['amount_required']
            years = form.cleaned_data['years_in_business']

            if amount > 50000 and years < 1:
                return redirect("denied")
            elif amount < 50000 and years >= 1:
                return redirect("preapproved")
            else:
                return redirect("success")

    else:
        form = CustomFieldForm()

    return render(request, "form.html", {
        'form': CustomFieldForm()
    })

"""
Default template for using djangorestframework.
Change permission_classes to reflect what type of authentiaction you want.
Use APIView to have the predrawn classes from djangorestframework
Return what you want in content.
I am still trying to figure out how to query djongo DB.
"""
class TestAuthView(APIView):
    permission_classes = [permissions.AllowAny]
    def get(self, request):
        try:
            # Do some query
            print(User.objects.get(username="test_gabe"))
        except Exception as e:
            # respond with error msg
            return Response(data = {'error': 'Invalid authorization token provided'}, status=403)

        # Content to respond with using the api
        content = {
            'user': request.user.id,  # `django.contrib.auth.User` instance.
            'auth': request.auth,  # None
        }
        return Response(content)
