from django import template
import os

register = template.Library()

@register.filter
def webp(image_field):
    """
    Returns the URL of a WebP version of the image if it exists,
    otherwise returns the original URL.
    """
    if not image_field:
        return ""
    
    base, ext = os.path.splitext(image_field.url)
    webp_url = f"{base}.webp"
    
    # Check if WebP exists in MEDIA_ROOT
    media_path = image_field.storage.path(webp_url.replace(image_field.storage.base_url, ""))
    if os.path.exists(media_path):
        return webp_url
    return image_field.url
