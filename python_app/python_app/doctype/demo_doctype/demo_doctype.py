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
	
 
    # # create a new document
    # def new_doc(self):
    #     doc = frappe.new_doc('Task')
    #     doc.title = 'New Task 2'
    #     doc.insert()
    
    # def delete_doc(self):
    #     frappe.delete_doc('Test',"nidhi")
        
    # def rename_doc(self):
    #     frappe.rename_doc('Test Doctype','202263519e','def')
        

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
    # def validate(self):
    #     self.delete_document()
    # def delete_document(self):
    #     doc=frappe.delete_doc("Test Doctype","abc")  
    
    
    # # frappe.db.exist(doctype,name)
    # def validate(self):
    #     if frappe.db.exist("Client side scripting","nidhi@gmail.com"):
    #         frappe.msgprint("The document is exist in database")
    #     else:
    #         frappe.msgprint("The document does not exist in database")
    
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
    
    
    
    # def before_save(self):
    #     frappe.throw("hello frappe from before_save event")
        
    # def before_insert(self):
    #     frappe.throw("hello frappe from before_insert event")
        
    # def after_insert(self):
    #     frappe.throw("hello frappe from after_insert event")
    
    # def on_update(self):
    #     frappe.throw("hello frappe from on_update event")
    
    # def before_submit(self):
    #     frappe.throw("hello frappe from before_submit event")
    
    # def on_submit(self):
    #     frappe.throw("hello frappe from on_submit event")
    
    # def on_cancel(self):
    #     frappe.throw("hello frappe from on_cancel event")
    
    # def on_trash(self):
    #     frappe.throw("hello frappe from on_trash event")
    
    # def after_delete(self):
    #     frappe.throw("hello frappe from after_delete event")
        
    # def get_meta(self): 
    #     frappe.get_doc('DocType', 'Demo Doctype')
    #     meta = frappe.get_meta('Demo')
    #     meta.has_field('status') # True
    #     meta.get_custom_fields() # [field1, field2, ..]
    
    # def doc_delte(self):
    #     frappe.doc.delete()
        
    # def check_permission(self):
    #     frappe.doc.check_permission(permtype='write') # throws if no write permission
    
    # def get_title(self):
    #     title =frappe.doc.get_title("Demo Doctype")
    
    # updates value in database, updates the modified timestamp
    # def db_set(self):
    #     frappe.doc.db_set('first_name', 'dwiti')

    # # updates value in database, will trigger doc.notify_update()
    #     frappe.doc.db_set('price', 2300, notify=True)

    # # updates value in database, will also run frappe.db.commit()
    #     frappe.doc.db_set('price', 2300, commit=True)

    # # updates value in database, does not update the modified timestamp
    #     frappe.doc.db_set('price', 2300, update_modified=False)
    
    # # add john to list of seen
    # def add_seen(self):
    #     frappe.doc.add_seen('nidhi@gmail.com')
    #     # add session user to list of seen
    #     frappe.doc.add_seen()

    # def queue_action(self):
    #     frappe.doc.queue_action('send_emails', emails='Email', message='Howdy')
    
    
    # def db_insert(self):
    #     frappe.doc = frappe.get_doc(doctype="Demo Doctype", data="")
    #     frappe.doc.db_insert()
    
    
    # def get_list(self):
    #    frappe.db.get_list('Demo Doctype')
    #    frappe.db.get_list('Demo Doctype', pluck='name')
    
    # def db_exist(self):
    #     db=db.exists("Demo Doctype", "nidhi@gmail.com")
    
    # def db_delete(self):
    #     frappe.db.delete("Demo Doctype")
    #     # frappe.db.delete("Error Log")
    #     # frappe.db.delete("__Test Table")
        
    # def db_truncate(self):
    #     frappe.db.truncate(" Doctype")
    
    # def db_sql(self):
    #     data = frappe.db.sql("""
    #     SELECT last_name FROM `tabDemo Doctype` """, as_dict=0)
    
    # def db_describe(self):
    #     frappe.db.describe("Demo Doctype")
        
    # def create_file(self):
    #     self.write_file()
    #     # This ensures rollback if DB transaction is rolledback
    #     frappe.db.after_rollback.add(self.rollback_file)

    # def rollback_file(self):
    #     self.delete_file()
   
    # def add_unique(self):
    #     frappe.db.add_unique("Demo Doctype",["first_name","last_name"])



        
        

       





    




    