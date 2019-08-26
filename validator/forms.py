# -*- coding: utf-8 -*-
from django import forms

from validator.mail import MailValidator, InvalidFormat, DisposableDomain, PhisingDomain


class MailValidatorFormMixin(object):
    """An mixin to validate """

    field_name = "email"
    extra_validate = False

    def clean(self):
        """Check the mail and extra validate rules"""
        cleaned_data = super(MailValidatorFormMixin, self).clean()
        mail = cleaned_data.get(self.field_name)

        if mail:
            message = "Cette adresse email n'est pas valide"

            try:
                mail = MailValidator(mail.lower())
            except (InvalidFormat, DisposableDomain, PhisingDomain):
                raise forms.ValidationError({self.field_name: message})

            if not mail.validate_mail():
                raise forms.ValidationError({self.field_name: message})

            if self.extra_validate:
                if not mail.extra_validate_mail_rules():
                    raise forms.ValidationError({self.field_name: message})

        return cleaned_data
