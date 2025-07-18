TS Task Timer  
----------------

### Track time effortlessly and link work to actual output.

`TS Task Timer` is a powerful custom Odoo module that enhances task tracking with real-time timers, automatic timesheet entries, email customization, and CRM/Sales integration. It is built for organizations that need accurate time logging, billing, and team productivity measurement.

Designed for Real-Time Task Management  
---------------------------------------

Enable users to start/stop a timer for tasks, and record exact durations. Timers run in real-time and store data as timesheet entries—perfect for client billing or performance audits. Also includes support for task history and feedback tracking.

Easy Configuration  
------------------

### Set your rules, and the system follows.

With built-in configuration settings, admins can toggle auto email behaviors, enable project-specific templates, and decide how feedback is collected—all without writing any code.

Project Task Integration  
------------------------

### Timer controls right inside your task.

The project task form includes an intuitive start/stop timer button. Each session is logged in a dedicated **Timesheet/History** tab, and task durations are stored with timestamps and optional notes.

Custom Email Wizard  
-------------------

### Send emails without follower noise

Includes a custom `task.email.wizard` for sending emails directly to selected recipients—followers are bypassed unless explicitly included. Ideal for confidential or targeted updates.

Suggested Recipient Logic  
--------------------------

Use a lightweight JavaScript component to auto-suggest the most relevant contact. Clean separation from default mail logic ensures customizability and avoids spamming followers.

Work Efficiently  
-----------------

### View team time, manage better

Use the **group by User** or **Project** views in tasks or timesheets to review who's working on what, how long tasks are taking, and bill accordingly. Visual indicators help highlight missing data or unassigned effort.



Automation & Cron  
------------------

### Set feedback reminders with scheduled jobs

A scheduled cron job (`feedback_mailers_cron.py`) sends feedback request emails after task completion. Templates are configurable and can be edited via the UI.

Security and Access  
-------------------

Granular control via security groups:
- **Task Timer User**
- **Timer Admin**
- **Project Manager**

Security settings are defined in `ir.model.access.csv` and tied to relevant models and views.

Integrated Settings  
-------------------

Go to **Settings > General Settings > Task Timer** to enable or tweak:

- Enable/disable feedback emails
- Adjust timesheet behavior
- Manage recipient logic
- Define default templates

Smart Technology  
----------------

Built using modular and standard Odoo components:

- Python Models (`project_task.py`, `ts_start_timesheet.py`, etc.)
- Email Templates and Wizards (`task_email_wizard.py`)
- Cron Jobs (`feedback_mailers_cron.py`)
- Views (`project_task_views.xml`, `task_timer_description.xml`)
- JavaScript for UI logic (optional for advanced use cases)

What’s Next  
-----------

- [ ] Mobile timer controls  
- [ ] Advanced reporting dashboard  
- [ ] Slack/MS Teams integration  
- [ ] KPI tracker per project/task  