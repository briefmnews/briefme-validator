# -*- coding: utf-8 -*-
import re

from dns.resolver import (
    query, Timeout, NXDOMAIN, YXDOMAIN, NoAnswer, NoNameservers)

from validator.constants import DISPOSABLE_EMAIL_DOMAINS, PHISHING_DOMAINS


def _validate_more_consonne(word):
    return bool(re.search('[bcdfghjklmnpqrstvwxyz]{5}', word, re.IGNORECASE))


def _validate_more_vowel(word):
    return bool(re.search('[aeiouy]{3}', word, re.IGNORECASE))


def _validate_more_number(word):
    return bool(re.search('[0-9]{5}', word))


def validate_mail(mail):
    """To validate the mail if the mail is invalid the return value is none.

    @param mail: The mail
    @type mail: str

    @return: The mail
    @rtype : str
    """
    name = mail.split('@')[0]
    domain = mail.split('@', 1)[-1]

    if '@' in domain:
        return None

    if name in ('postmaster', 'abuse'):
        return None

    if domain in DISPOSABLE_EMAIL_DOMAINS:
        return None

    if domain in PHISHING_DOMAINS:
        return None

    try:
        query(domain, 'MX')
    except (Timeout, NXDOMAIN, YXDOMAIN, NoAnswer, NoNameservers):
        return None

    return mail


def extra_validate_mail_rules(mail):
    """To validate the mail if the mail is invalid the return value is none.

    @param mail: The mail
    @type mail: str

    @return: The mail
    @rtype : str
    """
    name = mail.split('@')[0]
    domain = mail.split('@', 1)[-1]

    if len(name) < 5:
        return None

    if _validate_more_consonne(name) or _validate_more_consonne(domain):
        return None

    if _validate_more_vowel(name) or _validate_more_vowel(domain):
        return None

    if _validate_more_number(name) or _validate_more_number(domain):
        return None

    if 'spam' in name:
        return None

    if 'test' in name:
        return None

    return mail
