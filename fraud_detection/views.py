from django.shortcuts import render

# Create your views here.
def review_analysis(request):
    return render(request,'review.html')