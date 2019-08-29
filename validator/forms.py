# -*- coding: utf-8 -*-
from django import forms

from validator.mail import MailValidator, InvalidFormat, DisposableDomain, PhisingDomain


class MailValidatorFormMixin(object):
    """An mixin to validate """

    field_name = "email"
    extra_validate = True

    def clean(self):
        """Check the mail and extra validate rules"""
        cleaned_data = super(MailValidatorFormMixin, self).clean()
        email = cleaned_data.get(self.field_name)

        if email:
            message = "Cette adresse email n'est pas valide"

            try:
                email = MailValidator(email)
            except (InvalidFormat, DisposableDomain, PhisingDomain):
                raise forms.ValidationError({self.field_name: message})

            if not email.validate_mail():
                raise forms.ValidationError({self.field_name: message})

            if self.extra_validate:
                if not email.extra_validate_mail_rules():
                    raise forms.ValidationError({self.field_name: message})

        return cleaned_data
