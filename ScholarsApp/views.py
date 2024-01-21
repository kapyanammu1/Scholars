from django.shortcuts import render, get_object_or_404, redirect
from .models import Municipality, Brgy, School, Course, Student
from .forms import MunicipalityForm, BrgyForm, SchoolForm, CourseForm, StudentForm
from django.http import JsonResponse, Http404, HttpResponse

# Create your views here.
def index(request):
    mun = Municipality.objects.all()
    return render(request, 'index.html')

def MunList(request):
    mun = Municipality.objects.all()
    return render(request, 'MunList.html', {'mun': mun})

def AdEdMun(request, pk):
    # has_admin_permission = request.user.has_perm('BrgyApp.can_access_admin_features') 
    try:
        mun = get_object_or_404(Municipality, pk=pk)
        
        if request.method == 'POST':
            form = MunicipalityForm(request.POST, request.FILES, instance=mun)
            if form.is_valid():
                form.save()
                # pdf_buffer = generate_pdf_report()
                # return pdf_report_view(pdf_buffer)
                return redirect('MunList')
        else:
            form = MunicipalityForm(instance=mun)
        return render(request, 'AdEdMun.html', {'form': form, 'mun': mun})
    except Http404:  
        mun = Municipality.objects.all()
        if request.method == 'POST':
            form = MunicipalityForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()                
                return redirect('MunList')               
        else:
            form = MunicipalityForm()
        return render(request, 'AdEdMun.html', {'form': form, 'mun': mun})
    
def DelMun(request, pk):
    if request.method == 'POST':
        mun = get_object_or_404(Municipality, pk=pk)
        mun.delete()
        return JsonResponse({'message': 'Item deleted successfully.'})
    return JsonResponse({'message': 'Invalid request method.'}, status=400)