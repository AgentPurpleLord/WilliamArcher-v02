"""Streamfields live in here."""

from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock


class TitleAndTextBlock(blocks.StructBlock):
    """Title and Text and nothing else."""

    title = blocks.CharBlock(required=True, help_text='Add your Title.')
    text = blocks.TextBlock(required=True, help_text='Add additional Text.')

    class Meta: # noqa
        template = "streams/title_and_text_block.html"
        icon = "edit"
        label = "Title & Text"


class CardBlock(blocks.StructBlock):
    """Cards with image and text and button(s)."""

    title = blocks.CharBlock(required=True, help_text='Add your Title.')

    cards = blocks.ListBlock(
        blocks.StructBlock(
            [
                ("image", ImageChooserBlock(required=True)),
                ("title", blocks.CharBlock(required=True, max_length=40)),
                ("text", blocks.TextBlock(required=True, max_length=200)),
                ("button_page", blocks.PageChooserBlock(required=False)),
                ("button_url", blocks.URLBlock(required=False, help_text="If button page select above, that will be used first.")),
            ]
        )
    )

    class Meta: # noqa
        template = "streams/card_block.html"
        icon = "doc-full"
        label = "Cards"


class RichTextBlock(blocks.RichTextBlock):
    """RichText with all the features."""

    class Meta: # noqa
        template = "streams/richtext_block.html"
        icon = "edit"
        label = "Full RichText"