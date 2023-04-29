from django.core import validators
from django.utils.deconstruct import deconstructible


@deconstructible
class PhoneValidator(validators.RegexValidator):
    regex = r'^09\d{9}$'
    message = (
            'لطفا شماره معتبر وارد کنید!'
        '  شماره باید با"09" آغاز شود '

    )
    flags = 0


phone_validator = PhoneValidator()
