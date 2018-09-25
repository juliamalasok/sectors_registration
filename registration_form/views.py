from django.shortcuts import render

from .models import User, SectorAnswer
from .forms import NameForm


# Create your views here.
def index(request):
    print("Yayyyy!")
    form = NameForm()

    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            print(form)
            print("CLEANED SHIT:")
            print(form.cleaned_data.get("user_name"))
            user = User(name=form.cleaned_data.get("user_name"))
            print("NEW USER:")
            print(user)
            user.save()

    return render(request, 'registration_form/index.html', {'form': form})
