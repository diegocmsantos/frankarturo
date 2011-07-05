from django import forms
from django.utils.translation import ugettext as _

from mylovelymontreal.tracrpc import TracXmlRpc

TICKET_TYPES = (
    ('task', _('Request')),
    ('bug', _('Bug')),
)

TICKET_PRIORITIES = (
    ('', _('Please, select a priority')),
    ('blocker', _('I can\'t access my website!')),
    ('critical', _('Han.. there is something wrong with X')),
    ('major', _('Something is missing!')),
    ('minor', _('I need to change some things.')),
    ('trivial' , _('Can I change only this paragraph to red ?')),
)

PRIORITY_I18N = (
    ('blocker', _('Blocker')),
    ('critical', _('Critical')),
    ('major', _('Major')),
    ('minor', _('Minor')),
    ('trivial', _('Trivial')),
)

def pretty_choice(key, choices):
    for c in choices:
        if key == c[0]:
            return c[1]
    
    return None

class TicketSubmissionForm(forms.Form):
    type = forms.ChoiceField(label=_('Type:'), choices=TICKET_TYPES)
    priority = forms.ChoiceField(label=_('Priority:'), choices=TICKET_PRIORITIES)
    summary = forms.CharField(label=_('Summary:'))
    message = forms.CharField(label=_('Your message:'), widget=forms.Textarea)
    attachment = forms.FileField(label=_('Attachment (optional):'), required=False)
    
    def mail(self, user, ticket_id):
        data = self.cleaned_data
        subject = _('Montreal - Request Ticket #%s' % (ticket_id, ))
        type = pretty_choice(data['type'], TICKET_TYPES)
        priority = pretty_choice(data['priority'], TICKET_PRIORITIES)
        real_priority = pretty_choice(data['priority'], PRIORITY_I18N)
        
        message = _("""
            You have submitted us a ticket request. Below is a copy of all the information you provided us:
            
            Type: %(type)s
            Priority: %(priority)s (%(real_priority)s)
            Summary: %(summary)s
            Message: %(message)s
            
            Thank you.
            Montreal.
            
        """) % {
            'type' : type,
            'priority' : priority,
            'real_priority' : real_priority,
            'summary': data['summary'],
            'message': data['message'],
        }
        
        user.email_user(subject, message)
    
    def save(self, user):
        data = self.cleaned_data
        attrs = {
            'type' : data['type'],
            'priority' : data['priority'],
        }
        rpc = TracXmlRpc()
        ticket_id = rpc.ticket_create(data['summary'], data['message'], attrs)
        self.mail(user, ticket_id)
        return ticket_id
