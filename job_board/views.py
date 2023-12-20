from django.shortcuts import render ,  HttpResponse , get_object_or_404

from .models import JobPosting
# Create your views here.
def index(request):
    active_postings = JobPosting.objects.filter(is_active =True)
    context = {
        'job_posting': active_postings
    }
    return render (request,'job_board/index.html', context)

def job_detail(request, pk):
    job_posting =get_object_or_404(JobPosting, pk=pk)
    context = {
        'posting': job_posting
    }
    return render (request,'job_board/detail.html', context)