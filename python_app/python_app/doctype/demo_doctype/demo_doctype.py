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
    
    
    
# utility functions

# # now()
    
# from frappe.utils import now

# now() 

# # getdate()

# from frappe.utils import getdate

# getdate() # datetime.date(2021, 5, 25)
# getdate('2000-03-18') # datetime.date(2000, 3, 18)

# # today()
    
# from frappe.utils import today

# today() # '2021-05-25'

# # add_to_date

# from datetime import datetime # from python std library
# from frappe.utils import add_to_date

# today = datetime.now().strftime('%Y-%m-%d')
# print(today) # '2021-05-21'

# after_10_days = add_to_date(datetime.now(), days=10, as_string=True)    
# print(after_10_days) # '2021-05-31'

# add_to_date(datetime.now(), months=2) # datetime.datetime(2021, 7, 21, 15, 31, 18, 119999)
# add_to_date(datetime.now(), days=10, as_string=True, as_datetime=True) # '2021-05-31 15:30:23.757661'
# add_to_date(None, years=6) # datetime.datetime(2027, 5, 21, 15, 32, 31, 652089)


# # pretty_date()

# from frappe.utils import pretty_date, now, add_to_date

# pretty_date(now()) # 'just now'


# # format_duration

# from frappe.utils import format_duration

# format_duration(50) # '50s'
# format_duration(10000) # '2h 46m 40s'
# format_duration(1000000) # '11d 13h 46m 40s'

# # Convert days to hours
# format_duration(1000000, hide_days=True) # '277h 46m 40s'


# # comma_and

# from frappe.utils import comma_and

# comma_and([1, 2, 3]) # "'1', '2' and '3'"
# comma_and(['Apple', 'Ball', 'Cat'], add_quotes=False) # 'Apple, Ball and Cat'
# comma_and('abcd') # 'abcd'


# # money_in_words

# from frappe.utils import money_in_words

# money_in_words(900) # 'INR Nine Hundred and Fifty Paisa only.'
# money_in_words(900.50) # 'INR Nine Hundred and Fifty Paisa only.'
# money_in_words(900.50, 'USD') # 'USD Nine Hundred and Fifty Centavo only.'
# money_in_words(900.50, 'USD', 'Cents') # 'USD Nine Hundred and Fifty Cents only.'

# # validate_json_string

# import frappe
# from frappe.utils import validate_json_string

# # No Exception thrown
# validate_json_string('[]')
# validate_json_string('[{}]')
# validate_json_string('[{"player": "one", "score": 199}]')

# try:
#     # Throws frappe.ValidationError
#     validate_json_string('invalid json')
# except frappe.ValidationError:
#     print('Not a valid JSON string')

# # random_string

# from frappe.utils import random_string

# random_string(40) # 'mcrLCrlvkUdkaOe8m5xMI8IwDB8lszwJsWtZFveQ'
# random_string(6) # 'htrB4L'
# random_string(6) #'HNRirG'

# # unique

# from frappe.utils import unique

# unique([1, 2, 3, 1, 1, 1]) # [1, 2, 3]
# unique('abcda') # ['a', 'b', 'c', 'd']
# unique(('Apple', 'Apple', 'Banana', 'Apple')) # ['Apple', 'Banana']


# # get_pdf

# import frappe
# from frappe.utils.pdf import get_pdf

# @frappe.whitelist(allow_guest=True)
# def generate_invoice():
#     cart = [{
#         'Samsung Galaxy S20': 10,
#         'iPhone 13': 80
#     }]

#     html = '<h1>Invoice from Star Electronics e-Store!</h1>'

#     # Add items to PDF HTML
#     html += '<ol>'
#     for item, qty in cart.items():
#         html += f'<li>{item} - {qty}</li>'
#     html += '</ol>'

#     # Attaching PDF to response
#     frappe.local.response.filename = 'invoice.pdf'
#     frappe.local.response.filecontent = get_pdf(html)
#     frappe.local.response.type = 'pdf'


# # get_abbr

# from frappe.utils import get_abbr

# get_abbr('Gavin') # 'G'
# get_abbr('Coca Cola Company') # 'CC'
# get_abbr('Mohammad Hussain Nagaria', max_len=3) # 'MHN'


# # validate_url

# from frappe.utils import validate_url

# validate_url('google') # False
# validate_url('https://google.com') # True
# validate_url('https://google.com', throw=True) # throws ValidationError


# # validate_email_address

# from frappe.utils import validate_email_address

# # Single valid email address
# validate_email_address('rushabh@erpnext.com') # 'rushabh@erpnext.com'
# validate_email_address('other text, rushabh@erpnext.com, some other text') # 'rushabh@erpnext.com'

# # Multiple valid email address
# validate_email_address(
#     'some text, rushabh@erpnext.com, some other text, faris@erpnext.com, yet another no-emailic phrase.'
# ) # 'rushabh@erpnext.com, faris@erpnext.com'

# # Invalid email address
# validate_email_address('some other text') # ''

# # validate_phone_number

# from frappe.utils import validate_phone_number

# # Valid phone numbers
# validate_phone_number('753858375') # True
# validate_phone_number('+91-75385837') # True

# # Invalid phone numbers
# validate_phone_number('invalid') # False
# validate_phone_number('87345%%', throw=True) # InvalidPhoneNumberError


# # frappe.cache()

# import frappe

# cache = frappe.cache()

# cache.set('name', 'frappe') # True
# cache.get('name') # b'frappe'








        
        

       





    




    