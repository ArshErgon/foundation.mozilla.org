from django.apps import apps
from wagtail.core import models as wagtail_models

from networkapi.wagtailpages.pagemodels.mixin import foundation_metadata


class ResearchLibraryPage(foundation_metadata.FoundationMetadataPageMixin, wagtail_models.Page):
    max_count = 1
    parent_page_types = ['ResearchLandingPage']
    subpage_types = ['ResearchDetailPage']

    def get_context(self, request):
        context = super().get_context(request)
        context['research_detail_pages'] = self.get_research_detail_pages()
        return context

    def get_research_detail_pages(self):
        ResearchDetailPage = apps.get_model('wagtailpages', 'ResearchDetailPage')
        active_locale = wagtail_models.Locale.get_active()

        research_detail_pages = ResearchDetailPage.objects.all()
        research_detail_pages = research_detail_pages.filter(locale=active_locale)

        return research_detail_pages
