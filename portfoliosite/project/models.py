"""Project Page (Like a Blog Post)"""
from django import forms
from django.db import models
from django.shortcuts import render

from modelcluster.fields import ParentalManyToManyField
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel, MultiFieldPanel, InlinePanel
from wagtail.snippets.edit_handlers import SnippetChooserPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.core.fields import StreamField
from wagtail.core.models import Page, Orderable
from wagtail.snippets.models import register_snippet
from wagtail.contrib.routable_page.models import RoutablePage

from streams import blocks

# Create your models here.


class ProjectDetailPage(Page):
    """Project Detail Page"""
    custom_title = models.CharField(max_length=100, blank=False, null=False, help_text='Overwrites the default content.')
    project_image = models.ForeignKey("wagtailimages.Image", blank=False, null=True, related_name="+", on_delete=models.SET_NULL)

    content = StreamField(
        [
            ("title_and_text", blocks.TitleAndTextBlock()),
            ("full_richtext", blocks.RichTextBlock()),
            ("cards", blocks.CardBlock()),
        ],
        null=True,
        blank=True,
    )

    categories = ParentalManyToManyField("project.ProjectCategory", blank=True)

    content_panels = Page.content_panels + [
        FieldPanel("custom_title"),
        ImageChooserPanel("project_image"),
        MultiFieldPanel(
            [
                FieldPanel("categories", widget=forms.CheckboxSelectMultiple)
            ],
            heading="Categories"
        ),
        StreamFieldPanel("content"),
    ]

class ProjectCategory(models.Model):
    """Category for Projects in Snippets."""
    
    name = models.CharField(max_length=255)
    slug = models.SlugField(
        verbose_name="slug",
        allow_unicode=True,
        max_length=255,
        help_text='A slug to identify projects by this category'
    )

    panels = {
        MultiFieldPanel(
            [
                FieldPanel("name"),
                FieldPanel("slug"),
            ]
        )
    }

    class Meta: #noqa
        verbose_name = "Project Category"
        verbose_name_plural = "Project Categories"
        ordering = ["name"]

    def __str__(self):
        return self.name

register_snippet(ProjectCategory)