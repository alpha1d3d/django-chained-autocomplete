''' Mixins for the admin site for autocomplete chainged.

    IMPORTANT: The mixins needs to be inherited as most left parent.
    e.g.
        class MyAdmin(FilteredFieldMixin, admin.ModelAdmin)
'''
from .widgets import ChainedSelectWidget


class ChainedSelectFieldsMixin:
    '''
        Mixin to add to admin.ModelAdmin in order to make specific fields
        an autocomplete widget linked to another dropdown.

        The configuration should be in the format:
            chained_select_fields = {
                form_field_name: linked_field_name
            }

        e.g.
            chained_select_fields = {
                'user': 'group'
            }

        Which results in the 'user' dropdown being filtered
        based on the value of the 'group' dropdown.
    '''
    chained_select_fields = dict()

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        ''' Maps the formfields to widgets if they are in the configuration
        '''
        db = kwargs.get('using')
        if db_field.name in self.chained_select_fields.keys():
            kwargs['widget'] = ChainedSelectWidget(
                db_field.remote_field, self.admin_site, using=db,
                filter_key=self.chained_select_fields[db_field.name],
            )
        else:
            return super().formfield_for_foreignkey(db_field, request, **kwargs)

        return db_field.formfield(**kwargs)


class FilteredAdminMixin:
    '''
        Mixin to add to admin.ModelAdmin in order to make fields filterable
        on the admin view interface.

        e.g.
            filtered_fields = ('user', )

        Will make it possible to filter the url
        `admin/.../user/autocomplete/?user=XXX`
    '''
    filtered_fields = tuple()

    def get_queryset(self, request):
        ''' Returns the queryset for the admin view, and filters on specified
            filtered_fields.
        '''
        queryset = super().get_queryset(request)

        # apply filters if any
        for field in self.filtered_fields:
            value = request.GET.get(field)
            if value:
                queryset = queryset.filter(**{field: value})
        return queryset
