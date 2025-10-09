from django import forms
from django.conf import settings
from django.utils.safestring import mark_safe

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
            message = mark_safe(f"Cette adresse e-mail ne semble pas valide. Nous vous invitons à la corriger. Une question&nbsp;? <a href='{settings.BRIEFME_VALIDATOR_CONTACT_URL}'>Contactez-nous.</a>")

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
