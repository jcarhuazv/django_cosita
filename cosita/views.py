""" Main Views for project."""

# Django
from django.shortcuts import render


# View home
def home(request):
    return render(
        request=request,
        template_name='home.html',
    )
