from frappe.desk.doctype.todo.todo import ToDo

class CustomToDo(ToDo):
    def on_update(self):
        self.my_custom_code()
        super().on_update()

    def my_custom_code(self):
        pass
