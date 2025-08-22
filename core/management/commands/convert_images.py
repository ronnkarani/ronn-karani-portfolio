from django.core.management.base import BaseCommand
from django.conf import settings
from PIL import Image
import os

class Command(BaseCommand):
    help = 'Convert all images in media folder to WebP format'

    def handle(self, *args, **kwargs):
        media_folder = settings.MEDIA_ROOT
        converted_count = 0

        for root, dirs, files in os.walk(media_folder):
            for file in files:
                if file.lower().endswith(('.png', '.jpg', '.jpeg')):
                    full_path = os.path.join(root, file)
                    webp_path = os.path.splitext(full_path)[0] + '.webp'
                    try:
                        img = Image.open(full_path)
                        img.save(webp_path, 'WEBP', quality=85)
                        converted_count += 1
                        self.stdout.write(self.style.SUCCESS(f'Converted: {file} → {os.path.basename(webp_path)}'))
                    except Exception as e:
                        self.stdout.write(self.style.ERROR(f'Failed: {file} | {e}'))

        self.stdout.write(self.style.SUCCESS(f'Total images converted: {converted_count}'))
