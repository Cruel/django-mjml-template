from django import template
from mrml import to_html

register = template.Library()


class MJMLRenderNode(template.Node):
    def __init__(self, nodelist):
        self.nodelist = nodelist

    def render(self, context) -> str:
        mjml_source = self.nodelist.render(context)
        return to_html(mjml_source).content


@register.tag
def mjml(parser, token) -> MJMLRenderNode:
    """
    Compile MJML template after render django template.

    Usage:
        {% mjml %}
            .. MJML template code ..
        {% endmjml %}
    """
    nodelist = parser.parse(("endmjml",))
    parser.delete_first_token()
    tokens = token.split_contents()
    if len(tokens) != 1:
        raise template.TemplateSyntaxError(
            "'%r' tag doesn't receive any arguments." % tokens[0]
        )
    return MJMLRenderNode(nodelist)
