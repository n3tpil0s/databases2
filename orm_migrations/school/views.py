from django.views.generic import ListView

from .models import Student


class StudentListView(ListView):
    model = Student
    ordering = 'group'
    queryset = Student.objects.all().prefetch_related('teachers')

