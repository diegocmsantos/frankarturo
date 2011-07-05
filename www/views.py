from django.http import HttpResponse
from annoying.decorators import render_to
from django.views.decorators.http import require_POST

from contact_form.forms import ContactForm
from www.forms import BMICalculateForm

@render_to('www/index.html')
def index(request):
    c = {}
    
    #section = Section.menu.filter(url_name='articles')
    #c['last_articles'] = Page.index.filter(section=section)[:5]
    
    return c

@render_to('www/bmi.html')
def calculate_bmi(request):
    c = {}
    if request.method == 'POST':
        form = BMICalculateForm(request.POST)
        if form.is_bound and form.is_valid():
            c['bmi'] = form.calculate()
    else:
        form = BMICalculateForm()
        
    c['form'] = form
    return c

@require_POST
def contact_form(request, form_class=ContactForm, fail_silently=False):
    form = form_class(data=request.POST, files=request.FILES, request=request)
    if form.is_valid():
        form.save(fail_silently=fail_silently)
        return HttpResponse('true')
    
    return HttpResponse('false')
