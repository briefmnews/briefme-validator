Briefme Validator
==============
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Python 3.7](https://img.shields.io/badge/python-3.7-blue.svg)](https://www.python.org/downloads/release/python-370/)

This is an email validator to avoid phishing and mistakes made by end-users while
typing in forms.

##Usage
Once installed, you need to import adn call the mixin `MailValidatorFormMixin` whenever 
you need to check ofr phishing and mistakes in email addresses.
Here is an usage example in a Django project:
```python
from validator.forms import MailValidatorFormMixin

class HighSchoolForm(MailValidatorFormMixin, forms.ModelForm):
    ...
```