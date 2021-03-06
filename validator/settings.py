from django.conf import settings

MAX_CONSONANTS_IN_A_ROW = getattr(
    settings, "BRIEFME_VALIDATOR_MAX_CONSONANTS_IN_A_ROW", 6
)
MAX_VOWELS_IN_A_ROW = getattr(settings, "BRIEFME_VALIDATOR_MAX_VOWELS_IN_A_ROW", 5)
MAX_NUMBERS_IN_A_ROW = getattr(settings, "BRIEFME_VALIDATOR_MAX_NUMBERS_IN_A_ROW", 8)
