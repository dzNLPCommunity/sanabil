(function (window, document, undefined) {

    var factory = function ($, DataTable) {
        "use strict";
        $.extend(true, DataTable.defaults, {
            dom:
                "<'left aligned eight wide column'l><'right aligned eight wide column'f>" +
                "<'sixteen wide column'tr>" +
                "<'left aligned four wide column'i><'right aligned twelve wide column'p>",
            renderer: 'semantic'
        });

        $.extend(DataTable.ext.pager, {
            full_numbers_icon: DataTable.ext.pager.full_numbers
        });

        $.extend(DataTable.ext.classes, {
            sWrapper: "ui grid dataTables_wrapper ",
            sFilterInput: "",
            sLengthSelect: ""
        });

        DataTable.ext.renderer.pageButton.semantic = function (settings, host, idx, buttons, page, pages) {
            var api = new DataTable.Api(settings);
            var classes = settings.oClasses;
            var lang = settings.oLanguage.oPaginate;
            var btnDisplay, btnClass, btnIcon, counter = 0;
            var addIcons = ((!api.init().pagingType ? '' : api.init().pagingType.toLowerCase()).indexOf('icon') !== -1);

            var attach = function (container, buttons) {
                var i, ien, node, button;
                var clickHandler = function (e) {
                    e.preventDefault();
                    if (!$(e.currentTarget).hasClass('disabled')) {
                        api.page(e.data.action).draw('page');
                    }
                };

                for (i = 0, ien = buttons.length; i < ien; i++) {
                    button = buttons[i];

                    if ($.isArray(button)) {
                        attach(container, button);
                    }
                    else {
                        btnDisplay = '';
                        btnClass = '';
                        btnIcon = '';
                        switch (button) {
                            case 'ellipsis':
                                btnDisplay = (addIcons ? '<i class="mini ellipsis horizontal icon"></i>' : '&hellip;');
                                btnClass = 'disabled';
                                break;

                            case 'first':
                                btnIcon = (addIcons ? '<i class="angle single left icon"></i>' : '');
                                btnDisplay = btnIcon + lang.sFirst;
                                btnClass = button + (page > 0 ?
                                    '' : ' disabled');
                                break;

                            case 'previous':
                                btnIcon = (addIcons ? '<i class="angle double left icon"></i>' : '');
                                btnDisplay = btnIcon + lang.sPrevious;
                                btnClass = button + (page > 0 ?
                                    '' : ' disabled');
                                break;

                            case 'next':
                                btnIcon = (addIcons ? '<i class="angle double right icon"></i>' : '');
                                btnDisplay = lang.sNext + btnIcon;
                                btnClass = button + (page < pages - 1 ?
                                    '' : ' disabled');
                                break;

                            case 'last':
                                btnIcon = (addIcons ? '<i class="angle single right icon"></i>' : '');
                                btnDisplay = lang.sLast + btnIcon;
                                btnClass = button + (page < pages - 1 ?
                                    '' : ' disabled');
                                break;

                            default:
                                btnDisplay = button + 1;
                                btnClass = page === button ?
                                    'active' : '';
                                break;
                        }


                        if (btnDisplay) {
                            node = $('<a>', {
                                'class': classes.sPageButton + ' ' + btnClass + ' item ',
                                'id': idx === 0 && typeof button === 'string' ?
                                    settings.sTableId + '_' + button :
                                    null
                            }).html(btnDisplay).appendTo(container);

                            settings.oApi._fnBindAction(
                                node, {action: button}, clickHandler
                            );

                            counter++;
                        }
                    }
                }
            };
            var activeEl;

            try {
                activeEl = $(host).find(document.activeElement).data('dt-idx');
            }
            catch (e) {
            }

            attach(
                $(host).empty().html('<div class="ui stackable small pagination menu"/>').children('div'),
                buttons
            );

            if (activeEl) {
                $(host).find('[data-dt-idx=' + activeEl + ']').focus();
            }
        };

    }; // /factory


// Define as an AMD module if possible
    if (typeof define === 'function' && define.amd) {
        define(['jquery', 'datatables'], factory);
    }
    else if (typeof exports === 'object') {
        // Node/CommonJS
        factory(require('jquery'), require('datatables'));
    }
    else if (jQuery) {
        // Otherwise simply initialise as normal, stopping multiple evaluation
        factory(jQuery, jQuery.fn.dataTable);
    }
})(window, document);
$(document).ready(function () {
    $('#needs-table').DataTable();
    var dtable_associations = $('#associations-table').DataTable({
        "pagingType": "full_numbers_icon",
        lengthChange: false,
        order: [1, 'desc'],
        buttons: ['copy', 'excel', 'pdf']
    });
    dtable_associations.buttons().container()
        .appendTo($('div.eight.column:eq(0)', dtable_associations.table().container()));

});