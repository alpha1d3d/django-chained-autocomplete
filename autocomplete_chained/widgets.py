''' Widgets for autocomplete chained
'''

from django import forms
from django.contrib.admin import widgets


class ChainedSelectWidget(widgets.AutocompleteSelect):
    ''' Custom widget which passes the class, css and js to the
        autocomplete filtered fields.
    '''
    def __init__(self, *args, filter_key=None, **kwargs):
        ''' Sets the class and dataset on the widget. '''
        super().__init__(*args, **kwargs)
        self.attrs['class'] = 'autocomplete-chained'
        self.attrs['data-filter-key'] = filter_key

    @property
    def media(self):
        ''' Returns the media required. '''
        return forms.Media(
            js=(
                'admin/js/vendor/jquery/jquery.js',
                'admin/js/vendor/select2/select2.full.js',
                'admin/js/jquery.init.js',
                'js/autocomplete-chained.js',
            ),
            css={
                'screen': (
                    'admin/css/vendor/select2/select2.css',
                    'admin/css/autocomplete.css',
                ),
            },
        )
