def get_config():
    return {
        "for_doctype":{
            "Issue": {"status":"open"},
            "Issue": {"status":"open"},
        },
        "for_module_doctypes":{
            "ToDo": "To Do",
            "Event": "Calendar",
            "Comment": "Messages"
        },
        "for_module": {
            "To Do": "frappe.core.notifications.get_things_todo",
            "Calendar": "frappe.core.notifications.get_todays_events",
            "Messages": "frappe.core.notifications.get_unread_messages"
        }
    }
