from django.shortcuts import render_to_response
from django.template import RequestContext

from ..classes import Mapper, site_mappers
from ..exceptions import MapperError


def map_index(request, **kwargs):
    """Display filter options to chose what to display on the map

    Select the ward, section of the ward to use on the map
    """
    template = 'map_index.html'
    mapper_name = kwargs.get('mapper_name', '')
    mapper_names = []
    mapper = None
    if not mapper_name:
        mapper_names = [mname for mname in site_mappers.map_areas]
    else:
        mapper = site_mappers.get_mapper(mapper_name)
    if mapper:
        mapper = site_mappers.get_mapper('test_area')
        cart_size = 0
        identifiers = []
        icon = request.session.get('icon', None)
        if 'identifiers' in request.session:
            cart_size = len(request.session['identifiers'])
            identifiers = request.session['identifiers']
        return render_to_response(
            template, {
                'mapper_name': 'test_area',
                'item_label': mapper.item_label,
                'region_field_attr': mapper.region_field_attr,
                'region_label': mapper.region_label,
                'section_field_attr': mapper.section_field_attr,
                'section_label': mapper.section_label,
                'regions': mapper.regions,
                'sections': mapper.sections,
                'icons': mapper.icons,
                'session_icon': icon,
                'cart_size': cart_size,
                'identifiers': identifiers
            },
            context_instance=RequestContext(request)
        )
    return render_to_response(
        template, {
            'mapper_names': mapper_names,
        },
        context_instance=RequestContext(request)
    )
