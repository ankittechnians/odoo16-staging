TS Project Teams  
----------------

### Manage your project teams with full flexibility and control.

`TS Project Teams` is a custom Odoo module that enhances the native project management flow by enabling project-specific team assignments, dynamic access rights, and notification handling. It's built for organizations that rely on collaborative teamwork and need clear control over project roles.

Designed for Real Project Collaboration  
---------------------------------------

Organize your project teams as per your organization’s structure. Assign multiple users to projects, define their roles, and manage permissions automatically. Every project can have a custom team with access tailored to project needs.

Easy Configuration  
------------------

### Configure once, work forever.

With integrated system settings, you can easily enable or disable automatic notifications, restrict views based on roles, and control how teams are formed. Built-in configuration options help you adapt the behavior without writing a line of code.

Project View Integration  
------------------------

### All team information inside your project.

Your project form now includes a dedicated **Team** tab to add, remove, and review project team members. You can track roles like Manager, User, or Reviewer directly in the project.

Smart Notifications  
-------------------

### Email templates and suggested recipients

Custom mail templates are triggered based on task updates. Suggested recipients are intelligently calculated, ensuring the right team members are informed at the right time. All email logic is extendable and cleanly separated.

Suggested Recipient Logic  
--------------------------

Get dynamic suggestions for notification recipients using built-in JavaScript logic. Avoid spamming unnecessary users and focus on relevant communication.

Work as a Team  
--------------

### Real-time task filtering, grouped by teams

Use the **group-by team member** filter to easily manage workloads and review who’s responsible for what. Handle missing assignments with visual warnings and get better clarity over your resources.



Team Access Rights  
------------------

### Set it and forget it.

Predefined groups like **Project User**, **Project Manager**, and **Admin** control access to team data. Each role has access rules defined in security files for safe collaboration.

Integrated Settings  
-------------------

Go to **Settings > General Settings > TS Project Teams** to enable or tweak:

- Notification behavior
- Role-based restrictions
- Default team configurations

Smart Technology  
----------------

Built using standard Odoo APIs, this module integrates:

- Email Templates (`mail_template.xml`)
- Security and Groups (`ir.model.access.csv`, `team_groups.xml`)
- JavaScript Suggestions (`src/js/`)
- UI Enhancements (`ts_project_team_views.xml`, `ts_project_project.xml`)

What’s Next  
-----------

- [ ] Drag-and-drop team management UI  
- [ ] Team performance reports  
- [ ] Slack integration for team updates  
- [ ] Gantt view support for team load
