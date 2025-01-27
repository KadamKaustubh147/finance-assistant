from django.shortcuts import render
from .forms import PromptForm
from . import services
# loginrequired decorator

from django.views.decorators.http import require_POST, require_http_methods
from django.contrib.auth.decorators import login_required


# Create your views here.

@login_required
def chatbot(request):
    form = PromptForm()
    answer = None

    if request.method == "POST":
        form = PromptForm(request.POST)
        if form.is_valid():
            question = form.cleaned_data["prompt"]
            answer = services.response_ai(question)
            print(answer)
    
    context = {
        "response_ai": answer,
        "form": form
    }
    return render(request, 'chatbot.html', context)

