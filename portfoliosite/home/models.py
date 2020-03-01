from django.db import models

from wagtail.core.models import Page
from wagtail.admin.edit_handlers import FieldPanel

from project.models import ProjectDetailPage, ProjectCategory


class HomePage(Page):
    """Home Page Model."""

    templates = "home/home_page.html"
    max_count = 1

    hero = models.CharField(max_length=100, blank=False, null=True)
    hero_subtitle = models.CharField(max_length=100, blank=False, null=True)

    def get_context(self, request, *args, **kwargs):
        """Adding custom stuff to our context"""
        context = super().get_context(request, *args, **kwargs)
        context["projects"] = ProjectDetailPage.objects.live().public()
        return context

    content_panels = Page.content_panels + [
        FieldPanel("hero"),
        FieldPanel("hero_subtitle"),
    ]

    class Meta:
        verbose_name = "Home Page"
        verbose_name_plural = "Home Pages"

