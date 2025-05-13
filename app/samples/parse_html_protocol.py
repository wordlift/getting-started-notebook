from wordlift_client import EntityPatchRequest
from wordlift_sdk.wordlift.sitemap_import.protocol import (
    ParseHtmlProtocolInterface,
    ParseHtmlInput,
)


class ParseHtmlProtocol(ParseHtmlProtocolInterface):
    async def parse_html(
        self, parse_html_input: ParseHtmlInput
    ) -> list[EntityPatchRequest]:
        return list()
