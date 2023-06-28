app_name = "python_app"
app_title = "python_app"
app_publisher = "python_app"
app_description = "python_app"
app_email = "python_app"
app_license = "MIT"
# required_apps = []

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/python_app/css/python_app.css"   
# app_include_js = "/assets/python_app/js/python_app.js"

# include js, css files in header of web template
# web_include_css = "/assets/python_app/css/python_app.css"
# web_include_js = "/assets/python_app/js/python_app.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "python_app/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------


# add methods and filters to jinja environment
# jinja = {
#	"methods": "python_app.utils.jinja_methods",
#	"filters": "python_app.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "python_app.install.before_install"
# after_install = "python_app.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "python_app.uninstall.before_uninstall"
# after_uninstall = "python_app.uninstall.after_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "python_app.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
#	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
#	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
#	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
#	"*": {
#		"on_update": "method",
#		"on_cancel": "method",
#		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
#	"all": [
#		"python_app.tasks.all"
#	],
#	"daily": [
#		"python_app.tasks.daily"
#	],
#	"hourly": [
#		"python_app.tasks.hourly"
#	],
#	"weekly": [
#		"python_app.tasks.weekly"
#	],
#	"monthly": [
#		"python_app.tasks.monthly"
#	],
# }

# Testing
# -------

# before_tests = "python_app.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
#	"frappe.desk.doctype.event.event.get_events": "python_app.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
#	"Task": "python_app.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["python_app.utils.before_request"]
# after_request = ["python_app.utils.after_request"]

# Job Events
# ----------
# before_job = ["python_app.utils.before_job"]
# after_job = ["python_app.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
#	{
#		"doctype": "{doctype_1}",
#		"filter_by": "{filter_by}",
#		"redact_fields": ["{field_1}", "{field_2}"],
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_2}",
#		"filter_by": "{filter_by}",
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_3}",
#		"strict": False,
#	},
#	{
#		"doctype": "{doctype_4}"
#	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"python_app.auth.validate"
# ]

# # hooks.py

# test_string = "value"
# test_list = ["value"]
# test_dict = {
#     "key": "value"
# }

#  sound hook
# ------------

# sounds = [
#     {"name": "MessageTone", "src": "/assets/app/python_app/python_app/public/MessageTone.mp3", "volume": 0.3}
# ]

# Migrate hooks
# -------------

# before_migrate = "app.migrate.before_migrate"
# after_migrate = "app.migrate.after_migrate"

# file hooks
# ----------

# before_write_file="app.overrides.file.before_write"
# write_file="app.overrides.file.write_file"
# delete_file_data_content="app.overrides.file.delete_file"

# email hooks
# ------------

# override_email_send="app.overrides.email.send"
# get_sender_details="app.overrides.email.get_sender_details"

# extend bootinfo
# ---------------

# extend_bootinfo = "app.boot.boot_session"

# website controller context
# --------------------------

# extend_website_page_controller_context = {
#     "frappe.www.404": "app.pages.context_404"
# }

# website clear cache
# -------------------

# website_clear_cache = "app.overrides.clear_website_cache"


# website 404
# -----------

# website_catch_all = "not_found"


# default homepage
# ------------------

# homepage = "homepage"

# portal sidebar
# --------------

# portal_menu_items = [
#     {"title": "Dashboard", "route": "/dashboard", "role": "Customer"},
#     {"title": "Orders", "route": "/orders", "role": "Customer"}
# ]

# brand HTML
# ----------

# brand_html = '<div><img src="image.jpg"> TennisMart</div>'

# website context
# ---------------

# website_context = {
#     #  "favicon": "/assets/sfa_sigzen/img/Varmora Logo Leaf.png",
#      "app_logo":"/assets/app/python_app/python_app/public/Image/image.jpg",
#     }

# calendar hook
# --------------

# calendars = ["Appointment"]

# clear cache
# ----------

# clear_cache = "app.cache.clear_cache"

# session hooks
# ------------

# on_login = "app.overrides.successful_login"
# on_session_creation = "app.overrides.allocate_free_credits"
# on_logout = "app.overrides.clear_user_cache"


# fixtures
# --------

fixtures = [
    # export all records from the Category table
    "Demo Doctype"
]












