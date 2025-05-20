from bs4 import BeautifulSoup
from rdflib import URIRef, Literal
from wordlift_client import EntityPatchRequest
from wordlift_sdk.utils import create_entity_patch_request
from wordlift_sdk.wordlift.sitemap_import.protocol import (
    ParseHtmlProtocolInterface,
    ParseHtmlInput,
)


class ParseHtmlProtocol(ParseHtmlProtocolInterface):
    async def parse_html(
        self, parse_html_input: ParseHtmlInput
    ) -> list[EntityPatchRequest]:
        entity_id = parse_html_input.entity_id
        html = parse_html_input.html

        soup = BeautifulSoup(html, "html.parser")

        # Extract the text of all 'a' tags with class 'tag-cloud-link'
        tag_texts = [
            a.get_text(strip=True) for a in soup.find_all("a", class_="tag-cloud-link")
        ]

        resource = URIRef(entity_id)

        payloads = []

        for value in tag_texts:
            payloads.append(
                create_entity_patch_request(
                    resource, URIRef("http://schema.org/keywords"), Literal(value)
                )
            )

        return payloads
