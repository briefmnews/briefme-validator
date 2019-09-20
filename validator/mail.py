# -*- coding: utf-8 -*-
import re

from dns.resolver import query, Timeout, NXDOMAIN, YXDOMAIN, NoAnswer, NoNameservers

from validator.constants import DISPOSABLE_EMAIL_DOMAINS, PHISHING_DOMAINS


class InvalidFormat(Exception):
    pass


class DisposableDomain(Exception):
    pass


class PhisingDomain(Exception):
    pass


class MailValidator(object):
    """To validate mail format"""

    def __init__(self, mail):
        """To validate the mail validator class.

        @param mail:  The mail
        @type mail: str

        @raise InvalidFormat: The mail is invalid or contain invalid word
        @raise DisposableDomain: The mail is disposable
        @raise PhisingDomain: The mail is a phising domain
        """
        self.name = mail.split("@")[0]
        self.domain = mail.split("@", 1)[-1]

        if "@" in self.domain:
            raise InvalidFormat("The format of the mail is not valid")

        if self.name in ("postmaster", "abuse"):
            raise InvalidFormat("A postmaster or an abuse mail is not valid")

        if self.domain in DISPOSABLE_EMAIL_DOMAINS:
            raise DisposableDomain("Disposable mail is not authorized")

        if self.domain in PHISHING_DOMAINS:
            raise PhisingDomain("Seems a phising domain")

    @staticmethod
    def _validate_more_consonne(word):
        return bool(re.search("[bcdfghjklmnpqrstvwxz]{5}", word, re.IGNORECASE))

    @staticmethod
    def _validate_more_vowel(word):
        return bool(re.search("[aeiouy]{5}", word, re.IGNORECASE))

    @staticmethod
    def _validate_more_number(word):
        return bool(re.search("[0-9]{8}", word))

    @staticmethod
    def _validate_special_char(word):
        if re.search(r"[*]{2}", word):
            return True
        if re.search(r"[+]{2}", word):
            return True

        return False

    def validate_mail(self):
        """To validate the mail if the mail is invalid the return value is none.

        @param mail: The mail
        @type mail: str

        @return: The mail
        @rtype : str
        """
        try:
            query(self.domain, "MX")
        except (Timeout, NXDOMAIN, YXDOMAIN, NoAnswer, NoNameservers):
            return False

        return True

    def extra_validate_mail_rules(self):
        """To validate the mail if the mail is invalid the return value is none.

        @param mail: The mail
        @type mail: str

        @return: The mail
        @rtype : str
        """
        if len(self.name) < 2 or "spam" in self.name:
            return False

        if self._validate_more_consonne(self.name) or self._validate_more_consonne(
            self.domain
        ):
            return False

        if self._validate_more_vowel(self.name) or self._validate_more_vowel(
            self.domain
        ):
            return False

        if self._validate_more_number(self.name) or self._validate_more_number(
            self.domain
        ):
            return False

        if self._validate_special_char(self.name) or self._validate_special_char(
            self.domain
        ):
            return False

        return True
