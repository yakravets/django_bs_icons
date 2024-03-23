import os
import platform
from django import template
from django.utils.html import format_html

register = template.Library()


@register.simple_tag
def bs_icon(icon_name):
    if platform.system() == 'Windows':
        cur_folder = os.path.abspath(__file__).replace('\\bs_icons.py', '')
        icon_dir = os.path.join(cur_folder, 'icons\\')
    else:
        cur_folder = os.path.abspath(__file__).replace('/bs_icons.py', '')
        icon_dir = os.path.join(cur_folder, 'icons/')
            
    icon = open(icon_dir + icon_name + '.svg', 'r')
    return format_html(icon.read())
