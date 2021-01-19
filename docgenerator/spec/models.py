from django.db import models
from django.urls import reverse

class DataType(models.Model):
    name = models.CharField(max_length=80)
    slug = models.CharField(max_length=80, unique=True)
    description = models.TextField(blank=True)
    is_featured = models.BooleanField(default=False)

    class Meta:
        db_table = 'data_types'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('data_type_detail', args=(self.slug,))

class Concept(models.Model):
    name = models.CharField(max_length=100)
    slug = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    is_featured = models.BooleanField(default=False)

    class Meta:
        db_table = 'concepts'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('concept_detail', args=(self.slug,))

class XMLElement(models.Model):
    name = models.CharField(max_length=80)
    slug = models.CharField(max_length=80, unique=True)
    description = models.TextField(blank=True)
    is_featured = models.BooleanField(default=False)

    class Meta:
        db_table = 'xml_elements'
        verbose_name = 'XML element'
        verbose_name_plural = 'XML elements'

    def __str__(self):
        return self.slug

    def get_absolute_url(self):
        return reverse('element_detail', args=(self.slug,))

    def name_with_brackets(self):
        return f'<{self.name}>'

    def get_child_elements(self):
        return XMLElement.objects.filter(child_rel__parent=self).order_by('child_rel__child__name')

class XMLAttribute(models.Model):
    element = models.ForeignKey(XMLElement, on_delete=models.CASCADE)
    name = models.CharField(max_length=80)
    is_required = models.BooleanField()
    description = models.TextField(blank=True)
    data_type = models.ForeignKey(DataType, on_delete=models.PROTECT)

    class Meta:
        db_table = 'xml_attributes'
        verbose_name = 'XML attribute'
        verbose_name_plural = 'XML attributes'

    def __str__(self):
        return self.name

class XMLRelationship(models.Model):
    parent = models.ForeignKey(XMLElement, on_delete=models.CASCADE, related_name='parent_rel')
    child = models.ForeignKey(XMLElement, on_delete=models.CASCADE, related_name='child_rel')
    min_amount = models.IntegerField(null=True, blank=True)
    max_amount = models.IntegerField(null=True, blank=True)

    class Meta:
        db_table = 'xml_relationships'

class ExampleDocument(models.Model):
    name = models.CharField(max_length=300)
    slug = models.CharField(max_length=100, unique=True)
    blurb = models.TextField(blank=True)
    document = models.TextField()
    image_url = models.CharField(max_length=300, blank=True)
    is_featured = models.BooleanField(default=False)

    class Meta:
        db_table = 'example_documents'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('example_detail', args=(self.slug,))

class ExampleDocumentConcept(models.Model):
    example = models.ForeignKey(ExampleDocument, on_delete=models.CASCADE)
    concept = models.ForeignKey(Concept, on_delete=models.CASCADE)

    class Meta:
        db_table = 'example_concepts'

class ElementConcept(models.Model):
    element = models.ForeignKey(XMLElement, on_delete=models.CASCADE)
    concept = models.ForeignKey(Concept, on_delete=models.CASCADE)

    class Meta:
        db_table = 'element_concepts'
