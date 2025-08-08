from django import template

register = template.Library()


# 给表单字段添加CSS类
@register.filter(name='add_class')
def add_class(field, css_class):
    # 确保操作的是表单字段对象（BoundField）
    if hasattr(field, 'field'):
        # 获取已有class属性，避免覆盖
        existing_classes = field.field.widget.attrs.get('class', '')
        # 合并新的class
        new_classes = f"{existing_classes} {css_class}".strip()
        # 更新widget的属性
        field.field.widget.attrs['class'] = new_classes
    return field


# 给表单字段添加自定义属性（如placeholder）
@register.filter(name='attr')
def attr(field, name_value):
    # 分割属性名和值（格式："name:value"）
    try:
        name, value = name_value.split(':', 1)
    except ValueError:
        return field  # 格式错误时返回原始字段

    # 确保操作的是表单字段对象（BoundField）
    if hasattr(field, 'field'):
        field.field.widget.attrs[name.strip()] = value.strip()
    return field