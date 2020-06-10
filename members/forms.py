from django import forms
from .models import Members

class MemberUpdateForm(forms.ModelForm):
    class Meta:
        model = Members
        fields = [
            'memberNum',
            'memberLink',
            'memberLevel',
            'memberBegins',
            'firstName',
            'lastName',
            'gender',
            'birthDate',
            'emailAddress',
            'street',
            'city',
            'province',
            'postalCode',
            'country',
            'homePhone',
            'cellPhone',
            'workPhone',
            'tennisRank',
            'squashRank',
            'badmintonRank',
            'platformRank'
        ]