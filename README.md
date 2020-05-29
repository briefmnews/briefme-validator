Briefme Validator
==============
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Python 3.7](https://img.shields.io/badge/python-3.7-blue.svg)](https://www.python.org/downloads/release/python-370/)
[![Python CI](https://github.com/briefmnews/briefme-validator/workflows/Python%20CI/badge.svg)](https://github.com/briefmnews/briefme-validator/actions?query=workflow%3A%22Python+CI%22)
[![codecov](https://codecov.io/gh/briefmnews/briefme-validator/branch/master/graph/badge.svg)](https://codecov.io/gh/briefmnews/briefme-validator)

This is an email validator to avoid phishing and mistakes made by end-users while
typing in forms.

## Usage
Once installed, you need to import adn call the mixin `MailValidatorFormMixin` whenever 
you need to check for phishing and mistakes in email addresses.
Here is an usage example in a Django project:
```python
from validator.forms import MailValidatorFormMixin

class HighSchoolForm(MailValidatorFormMixin, forms.ModelForm):
    ...
```

## Settings
Here are the settings to set the maximum number of consonants, vowels and numbers in a row with their default values thah could 
be overriden:
```python
BRIEFME_VALIDATOR_MAX_CONSONANTS_IN_A_ROW = 5
BRIEFME_VALIDATOR_MAX_VOWELS_IN_A_ROW = 5
BRIEFME_VALIDATOR_MAX_NUMBERS_IN_A_ROW = 8
```