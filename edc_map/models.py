from django.db import models
import json

from edc_base.model.models import BaseUuidModel
from edc_map.model_mixins import MapperDataModelMixin, LandmarkMixin, MapperModelMixin
from django.contrib.auth.models import User


class Landmark(LandmarkMixin, BaseUuidModel):

    class Meta:
        app_label = 'edc_map'


class MapperData(MapperDataModelMixin, BaseUuidModel):

    map_code = models.CharField(
        max_length=10)

    pair = models.IntegerField()

    intervention = models.BooleanField(default=False)

    class Meta:
        app_label = 'edc_map'


class MapDivision(BaseUuidModel):

    label = models.CharField(
        verbose_name='Label',
        max_length=25,
        unique=True,
        editable=False,
        null=True,)

    section_name = models.CharField(
        max_length=10,
        null=True)

    user = models.ForeignKey(User, null=True)

    sub_section_name = models.CharField(
        max_length=10,
        null=True)

    map_area = models.CharField(
        max_length=25,
        null=True)

    section_polygon = models.TextField(null=True)

    sub_section_polygon = models.TextField(null=True)

    def __str__(self):
        return '{0} {1} {2}'.format(
            self.label,
            self.section_name,
            self.sub_section_name)

    def save(self, *args, **kwargs):
        self.section_polygon = json.dumps(self.section_polygon)
        self.sub_section_polygon = json.dumps(self.sub_section_polygon)
        super().save(*args, **kwargs)

    @property
    def section_polygon_list(self):
        """Return a polygon python list."""
        return json.loads(self.section_polygon)

    @property
    def sub_section_polygon_list(self):
        """Return a polygon python list."""
        return json.loads(self.sub_section_polygon)

    class Meta:
        app_label = 'edc_map'
