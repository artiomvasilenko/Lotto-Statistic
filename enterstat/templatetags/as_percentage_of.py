from django import template

register = template.Library()

@register.filter
def as_percentage_of(part, whole):
    try:
        return "%d%%" % (float(part) / whole * 100)
    except (ValueError, ZeroDivisionError):
        return ""

@register.filter
def percent_win(part, whole):
    try:
        return float(part) / whole
    except (ValueError, ZeroDivisionError):
        return 0.0

@register.filter
def ratio(result, percent):
    try:
        return f'{int(result * percent)}'
    except (ValueError, ZeroDivisionError, TypeError):
        return 0