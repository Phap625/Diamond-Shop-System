from django import template

register = template.Library()

@register.filter
def currency_format(value):
    try:
        return f"{int(value):,}".replace(",", ".")  # Định dạng số với dấu chấm ngăn cách hàng nghìn
    except (ValueError, TypeError):
        return value  # Nếu lỗi, trả về giá trị gốc
