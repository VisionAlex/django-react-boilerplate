from django import template
from django.conf import settings
from django.utils.safestring import mark_safe

register = template.Library()

@register.simple_tag
def load_react():
    css = load_css()
    js = load_js()
    return mark_safe(''.join( css + js ))


def load_css():
    return [
        f'<link rel="stylesheet" href="/static/{asset} />'
        for asset in load_files('.css')
    ]

def load_js():
    return [
        f'<script type="text/javascript" src="/static/{asset}" ></script>'
        for asset in load_files('.js')
    ]

def load_files(extension: str):
    files = []
    for path in settings.STATICFILES_DIRS:
        for filename in path.iterdir():
            if filename.name.endswith(extension):
                files.append(filename.name)
                
    return files

