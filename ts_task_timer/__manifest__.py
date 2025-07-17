{
    "name": "Project Task Timer",
    "author": "Technians",
    "website": "https://www.technians.com",
    "support": "support@technians.com",
    "version": "16.0",
    "category": "Project",
    "summary": """task timer, manage task time app, countdown timer module, calculate task start time, calculate work stop time, manage work time duration, time report timer odoo""",
    "description": """This module useful to track the timing of tasks, It will auto-generate entry in timesheet once after you stop the timer, You can easily start/stop task timer anywhere from the top bar, It will help the employee to manage timesheet without remember time manually as its auto notes timing. Employees don't need to fill the timesheet at the end and the manager also can easily see on the spot whenever an employee stops the timer and submit a description of the task, It will definitely make your employee happy to manage task timesheet. Cheers!""",
    "depends": ['project', 'hr_timesheet', 'analytic', 'base', 'mail', 'sale', 'crm'],
    "data": [
        'security/ir.model.access.csv',
        'wizard/task_email_wizard_views.xml',
        'data/custom_task_templates.xml',
        'views/ts_task_time_account_line_views.xml',
        'views/project_task_views.xml',
        'views/res_config_settings.xml',
        'views/create_quickly_project_views.xml',
        'views/feedback_mailers.xml',
        'views/task_timer_description.xml',
        'views/ir_cron.xml',
        'views/ts_start_timesheet_views.xml',
    ],

    'assets': {
        'web.assets_backend': [
            'ts_task_timer/static/src/js/time_track.js',
            'ts_task_timer/static/src/scss/time_track.scss',
            'ts_task_timer/static/src/xml/time_track.xml',
            'ts_task_timer/static/src/js/task_notification.js',
        ],
    },

    "images": ["static/description/banner.png",],
    "installable": True,
    "auto_install": False,
    "application": True,
    "license": "OPL-1",
    "price": "45",
    "currency": "EUR"
}
