from Acquisition import aq_inner
from DateTime import DateTime
from plone.app.event.portlets.portlet_events import Renderer
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone.app.event.portlets.portlet_calendar import ICollection
from plone.app.querystring import queryparser
from plone.app.event.base import expand_events
from plone.app.event.base import _prepare_range
from plone.app.event.base import start_end_query
from plone.app.event.base import RET_MODE_ACCESSORS
from plone.app.event.base import get_events
from plone.app.event.base import localized_now
from plone.app.event.base import DT


class CustomRenderer(Renderer):

    _template = ViewPageTemplateFile("portlet_events.pt")

    _search_base = None

    @property
    def events(self):
        context = aq_inner(self.context)
        data = self.data

        query = {}
        if data.state:
            query["review_state"] = data.state

        events = []
        query.update(self.request.get("contentFilter", {}))
        search_base = self.search_base
        if ICollection and ICollection.providedBy(search_base):
            # Whatever sorting is defined, we're overriding it.
            query = queryparser.parseFormquery(
                search_base, search_base.query, sort_on="start", sort_order=None
            )

            start = None
            if "start" in query:
                start = query["start"]
            else:
                start = localized_now(context)

            end = None
            if "end" in query:
                end = query["end"]

            start, end = _prepare_range(search_base, start, end)
            query.update(start_end_query(start, end))
            events = search_base.results(
                batch=False, brains=True, custom_query=query, limit=data.count
            )
            events = expand_events(
                events,
                ret_mode=RET_MODE_ACCESSORS,
                start=start,
                end=end,
                sort="start",
                sort_reverse=False,
            )
            events = events[: data.count]  # limit expanded
        else:
            search_base_path = self.search_base_path
            if search_base_path:
                query["path"] = {"query": search_base_path}
            # example 4: https://docs.plone.org/develop/plone/searching_and_indexing/query.html#querying-by-date # noqa
            now = DT(localized_now(context))
            start = DateTime(now.year(), now.month(), now.day())
            end = now + 60
            events = get_events(
                context,
                start=start,
                end=end,
                # ret_mode=RET_MODE_ACCESSORS,
                expand=True,
                limit=data.count,
                **query
            )

        return events
