# -*- coding: utf-8 -*-
from django import forms

from validator.mail import validate_mail, extra_validate_mail_rules


class MailValidatorFormMixin(object):
    """An mixin to validate """
    field_name = 'email'
    extra_validate = False

    def clean(self):
        """Check the mail and extra validate rules"""
        cleaned_data = super(MailValidatorFormMixin, self).clean()
        mail = cleaned_data.get(self.field_name)

        if mail:
            mail = mail.lower()
            message = u"Cette adresse email n'est pas valide"

            if not validate_mail(mail):
                raise forms.ValidationError({self.field_name: message})

            if self.extra_validate:
                if not extra_validate_mail_rules(mail):
                    raise forms.ValidationError({self.field_name: message})

        return cleaned_data
