from django.conf.urls.defaults import *

from mylovelymontreal.forms import TicketSubmissionForm

urlpatterns = patterns('mylovelymontreal.views',
    url(r'^form/$',  'form', name="mylovelymontreal_form"),
    url(r'^submit/$',  'submit', name="mylovelymontreal_submit"),
)

urlpatterns += patterns('ajax_validation.views',
    url(r'^form/contact/validate/$', 'validate', {'form_class': TicketSubmissionForm}, name='mylovelymontreal_ticket_validate'),
)
