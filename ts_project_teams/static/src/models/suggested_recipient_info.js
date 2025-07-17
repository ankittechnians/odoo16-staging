odoo.define('ts_project_teams.suggested_recipient_info_custom', function (require) {
    "use strict";

    var models = require('@mail/model/model_core');

    var SuggestedRecipientInfo = require('SuggestedRecipientInfo');

    SuggestedRecipientInfo.extend({
        isSelected: attr({
            /**
             * Prevents selecting a recipient that does not have a partner.
             */
            compute() {
                return this.partner ? this.isChecked : false;
            },
            default: false,
        }),
    });

});
