from django.shortcuts import get_object_or_404, render
from django.db.models import Q
from .models import Student

def student_list(request):
    query = request.GET.get("q", "").strip()
    students = Student.objects.all()
    if query:
        students = students.filter(
            Q(student_id__icontains=query)
            | Q(first_name__icontains=query)
            | Q(last_name__icontains=query)
            | Q(course__icontains=query)
            | Q(section__icontains=query)
        )
    return render(request, "students/student_list.html", {
        "students": students,
        "query": query,
    })

def student_detail(request, pk):
    student = get_object_or_404(Student, pk=pk)
    return render(request, "students/student_detail.html", {"student": student})
