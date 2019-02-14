/* JS for autocomplete chained, based on django-admin-autocomplete
 */
(function($) {
    'use strict';
    const init = function($element, options) {
        const getFilter = function () {
          // transform the specified filter key into parameters for the
          // select2 ajax query
          const filterKey = $element[0].dataset.filterKey;
          return {
            [`${filterKey}`]: $(`#id_${filterKey}`).val()
          };
        };

        const settings = $.extend({
            ajax: {
                data: function(params) {
                    return {
                        term: params.term,
                        page: params.page,
                        ...getFilter()
                    };
                }
            }
        }, options);
        $element.select2(settings);
    };

    $.fn.ChainedAutocompleteSelect = function(options) {
        var settings = $.extend({}, options);
        $.each(this, function(i, element) {
            var $element = $(element);
            init($element, settings);
        });
        return this;
    };

    $(function() {
        // Initialize all autocomplete widgets except the one in the template
        // form used when a new formset is added.
        $('.autocomplete-chained').not('[name*=__prefix__]').ChainedAutocompleteSelect();
    });

    $(document).on('formset:added', (function() {
        return function(event, $newFormset) {
            return $newFormset.find('.autocomplete-chained').ChainedAutocompleteSelect();
        };
    })(this));
}(django.jQuery));
