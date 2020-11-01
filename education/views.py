from django.shortcuts import get_object_or_404, get_list_or_404, redirect, render
from account.decorators import student_required,teacher_required
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

def home(request):
	if ((request.user.is_authenticated)and(request.user.is_student)):
		return redirect('student_home')
	elif ((request.user.is_authenticated)and(request.user.is_teacher)):
		return redirect('teacher_home')
	else:
		return render(request, 'home.html')

@login_required
@student_required
def student_home(request):
	return render(request, 'student_home.html')

@login_required
@teacher_required
def teacher_home(request):
	return render(request, 'teacher_home.html')
