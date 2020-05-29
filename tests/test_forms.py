import pytest

from django import forms
from validator.forms import MailValidatorFormMixin
from validator.mail import DisposableDomain, InvalidFormat, PhisingDomain, BannedEmailAddress
from validator.constants import BANNED_EMAIL_ADDRESSES, DISPOSABLE_EMAIL_DOMAINS, PHISHING_DOMAINS

pytestmark = pytest.mark.django_db(transaction=True)


class TestMailValidatorFormMixin:

    VALID_EMAIL_LIST = [
        "john.doe@free.fr",
        "aaronddoe@outlook.com",
        "address+plus@dummy.fr",
        "stars*inemail@gmail.com",
        "damien.cirotteau@brief.me",
        "douanier.rousseau@yahoo.fr",
        "thomas.carbillet@brief.me",
        "dummy@ctrl-x.com",
        "ttttoto@gmail.com",
        "uuuuvoila@yahoo.fr",
        "tom75000@msn.com",
        "uai750000@msn.com",
        "john.doe@hotmail.co.uk",
        "test@gmail.com",
    ]

    DISPOSABLE_DOMAIN_EMAIL_LIST = [
        {"email": "john.doe" + domain, "exception": DisposableDomain}
        for domain in DISPOSABLE_EMAIL_DOMAINS
    ]
    INVALID_FORMAT_EMAIL_LIST = [
        {"email": "postmaster@dummy.com", "exception": InvalidFormat},
        {"email": "abuse@brief.me", "exception": InvalidFormat},
        {"email": "double@@gmail.com", "exception": InvalidFormat},
    ]
    PHISHING_DOMAIN_EMAIL_LIST = [
        {"email": "john.doe" + domain, "exception": PhisingDomain}
        for domain in PHISHING_DOMAINS
    ]
    BANNED_EMAIL_ADDRESSES_LIST = [
        {"email": email, "exception": BannedEmailAddress}
        for email in BANNED_EMAIL_ADDRESSES
    ]

    INVALID_DISPOSABLE_PHISHING_EMAIL_LIST = (
        INVALID_FORMAT_EMAIL_LIST
        + DISPOSABLE_DOMAIN_EMAIL_LIST
        + PHISHING_DOMAIN_EMAIL_LIST
        + BANNED_EMAIL_ADDRESSES_LIST
    )

    EXTRA_VALIDATE_EMAIL_LIST = [
        "two**starsinarow@gmail.com",
        "three***starsinarow@gmail.com",
        "iiiii@gmail.com",
        "spam@gmail.fr",
        "maya76543789@wanadoo.fr",
        "john++doe@gmail.com",
        "emailwith'apostrophe@gmail.com",
        "emailwith''apostrophe@gmail.com",
        "email'with'apostrophe@gmail.com",
    ]

    VALIDATION_ERROR_MESSAGE = "Cette adresse email n'est pas valide"

    class DummyFormView(MailValidatorFormMixin, forms.Form):
        email = forms.EmailField()

        @property
        def cleaned_data(self):
            return self.data

    @pytest.mark.parametrize("email", VALID_EMAIL_LIST)
    def test_clean_valid_email(self, email):
        data = {"email": email}
        form = self.DummyFormView()
        form.data = data
        cleaned_data = form.clean()

        assert cleaned_data["email"] == email

    @pytest.mark.parametrize("email_list", INVALID_DISPOSABLE_PHISHING_EMAIL_LIST)
    def test_clean_invalid_disposable_phishing(self, email_list):
        data = {"email": email_list["email"]}
        form = self.DummyFormView()
        form.data = data

        with pytest.raises(forms.ValidationError, match=self.VALIDATION_ERROR_MESSAGE):
            with pytest.raises(email_list["exception"]):
                form.clean()

    @pytest.mark.parametrize("email", EXTRA_VALIDATE_EMAIL_LIST)
    def test_clean_extra_validate_is_true(self, email):
        data = {"email": email}
        form = self.DummyFormView()
        form.data = data
        with pytest.raises(forms.ValidationError, match=self.VALIDATION_ERROR_MESSAGE):
            form.clean()
