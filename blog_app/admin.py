from django.contrib import admin
from .models import Post, Image
from django.utils.html import format_html

class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('images',)
    list_display = [
        'title',
        'content',
        'created_at',
        'updated_at',
    ]

    def images(self, obj):
        imgs = obj.images.all()
        if imgs.exists():
            return format_html(" ".join(
                f'<a href="{img.image.url}" target="_blank">Imagen {i+1}</a>'
                for i, img in enumerate(imgs)
            ))
        return "No images"

class ImageAdmin(admin.ModelAdmin):
    list_display = ('image', 'post')

admin.site.register(Post, PostAdmin)
admin.site.register(Image, ImageAdmin)
