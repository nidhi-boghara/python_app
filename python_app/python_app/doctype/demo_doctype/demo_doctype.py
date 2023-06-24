# Copyright (c) 2023, python_app and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class DemoDoctype(Document):
    def before_save(self):
        self.full_name = self.first_name + " " + self.last_name
        # self.compute_age
        
    # def compute_age(self):
    #     if self.date_of_birth:
    #         self.age=frappe.utils.date_diff(frappe.utils.today(),self.date_of_birth)/365
     
     
    # def get_doc(self):
    #     if self.type == "Data":
    #         # self.validate_issue()
    #         test=frappe.get_doc("Test",self.test)
    #         # test.status='Issued'
    #         test.save()
            
    #frappe.get_doc(doctype,name)
    # def validate(self):
    #     self.get_document()
    # def get_document(self):
    #     doc=frappe.get_doc("Demo Doctype",self.demo_doctype)
    #     frappe.msgprint(("The first name is {0} and age is {1}").format(doc.firstname,doc.age))
    
            
    # # get an existing document
    # def get_doc(self):
    #     doc = frappe.get_doc('Test Doctype')
        # doc.title = 'Test'
        # doc.save()
        # doc.msgprint("doctype exist")
	
 
    # create a new document
    def new_doc(self):
        doc = frappe.new_doc('Task')
        doc.title = 'New Task 2'
        doc.insert()
    
    def delete_doc(self):
        frappe.delete_doc('Test',"nidhi")
        
    def rename_doc(self):
        frappe.rename_doc('Test Doctype','202263519e','def')
        

    #frappe.get_doc(doctype,name)
    # def validate(self):
    #     self.get_document()
    # def get_document(self):
    #     doc=frappe.get_doc("Client side scripting",self.client_side_doc)
    #     frappe.msgprint(("The first name is {0} and age is {1}").format(doc.firstname,doc.age))
    
    #frappe.new_doc(doctype,name)    
    # def validate(self):
    #     self.new_document()
    # def new_document(self):
    #     doc=frappe.new_doc("Client side scripting")  
    #     doc.firstname="nidhi"
    #     doc.lastname="patel"
    #     doc.age=21
    #     doc.append("familymembers",{"name":"shruti","relation":"sister","age":23})
    #     doc.insert()
    
    # #frappe.del_doc(doctype,name)    
    def validate(self):
        self.delete_document()
    def delete_document(self):
        doc=frappe.delete_doc("Test Doctype","abc")  
    
    
    # # frappe.db.exist(doctype,name)
    def validate(self):
        if frappe.db.exist("Client side scripting","nidhi@gmail.com"):
            frappe.msgprint("The document is exist in database")
        else:
            frappe.msgprint("The document does not exist in database")
    
    # # frappe.db.count(dtoctype,filters)
    # def validate(self):
        # doc_count=frappe.db.count("Client side scripting",{"enable":1})
        # frappe.msgprint(("The enable document count is {0}").format(doc_count))
          
    # frappe.db.sql(query,filter,as_dict)
    # def validate(self):
    #     self.sql
    # def sql(self):
    #     data=frappe.db.sql("select firstname,age from `tabClient side scripting` where enable=1",as_dict=1)
    #     for d in data:
    #         frappe.msgprint("The parent first name is {0} and last name is {1}").format(d.firstname,d.age)
        
        
    # def validate(self):
    #     frappe.msgprint(("hello my full name is '{0}'").format(self.firstname+ " "+self.middlename+" "+self.lastname))
    
    # def validate(self):
    #     for row in self.get("familymembers"):
    #         frappe.msgprint(("{0}. The family member name is '{1}' and relation is '{2}'").format(row.name,row.relation))
    
    
    
    def before_save(self):
        frappe.throw("hello frappe from before_save event")
        
    def before_insert(self):
        frappe.throw("hello frappe from before_insert event")
        
    def after_insert(self):
        frappe.throw("hello frappe from after_insert event")
    
    def on_update(self):
        frappe.throw("hello frappe from on_update event")
    
    def before_submit(self):
        frappe.throw("hello frappe from before_submit event")
    
    def on_submit(self):
        frappe.throw("hello frappe from on_submit event")
    
    def on_cancel(self):
        frappe.throw("hello frappe from on_cancel event")
    
    def on_trash(self):
        frappe.throw("hello frappe from on_trash event")
    
    def after_delete(self):
        frappe.throw("hello frappe from after_delete event")
    




    