from django.views.decorators.http import require_POST
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from annoying.decorators import render_to

from mylovelymontreal.forms import TicketSubmissionForm
from mylovelymontreal.tracrpc import TracXmlRpc

@render_to('mylovelymontreal/form.html')
@login_required
def form(request, form_class=TicketSubmissionForm):
    c = {'form': form_class()}
    return c
    
@require_POST
@login_required
def submit(request, form_class=TicketSubmissionForm):
    ticket_id = ''
    form = form_class(request.POST)
    if form.is_valid():
        ticket_id = form.save(request.user)
    
    return HttpResponse(str(ticket_id))
    
