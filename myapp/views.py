from django.shortcuts import render, redirect
from .forms import CommentForm

# Create your views here.

def home(request):
    return render(request, 'home.html')

def comment_view(request):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = CommentForm()
    
    return render(request, 'comment.html', {'form': form})