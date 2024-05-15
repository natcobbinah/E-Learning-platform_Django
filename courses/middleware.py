from django.urls import reverse 
from django.shortcuts import get_object_or_404, redirect 
from .models import Course 

def subdomain_course_middleware(get_response):
    """
    Subdomains for courses
    """
    def middleware(request):
        hosts_parts = request.get_host().split('.')
        if len(hosts_parts) > 2 and hosts_parts[0] != 'www':
            # get course for the given subdomain
            course = get_object_or_404(Course, slug=hosts_parts[0])
            course_url = reverse('course_detail', args=[course.slug])

            # redirect current request to the course detail view
            url = '{}://{}{}'.format(request.scheme, '.'.join(hosts_parts[1:]),
                                        course_url)
            return redirect(url)
        response = get_response(request)
        return response
    return middleware