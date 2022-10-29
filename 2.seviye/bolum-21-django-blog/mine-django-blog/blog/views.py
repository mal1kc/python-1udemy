from django.shortcuts import redirect, render

# 404 PAGE  
def handler404(request, exception=None):
    return render(request, '404.html')
