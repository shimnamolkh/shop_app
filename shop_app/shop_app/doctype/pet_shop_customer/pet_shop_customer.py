# Copyright (c) 2022, shimna and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from dateutil import relativedelta
from datetime import datetime

class PetShopCustomer(Document):
	
	def before_save(self):
		self.mobile_number_validation()
		self.full_name = f'{self.first_name} {self.last_name or ""}'
	@frappe.whitelist()
	def get_age(self):
		if(self.date_of_birth):
			today = datetime.now()
			date_of_birth = datetime.strptime(self.date_of_birth, '%Y-%m-%d')
			t = relativedelta.relativedelta(today, date_of_birth)
			return t.years

	@frappe.whitelist()
	def pet_check_session(self,doctype):
		data = frappe.get_all(doctype,fields=["*"])

		self.pet_table = []
		for d in data:
			
			self.append("pet_table",{
				"pet_name":d.pet_name,
				"pet_category":d.pet_category,
				"pet_price":d.pet_price,
				"number":d.number
			})

	
	def mobile_number_validation(self):
		if self.phone_number:
			if not (self.phone_number).isdigit():
				frappe.throw("Field Contact Number Accept Digits Only")
			if len(self.phone_number)>10:
				frappe.throw("Field Contact Number must be 10 Digits")
			if len(self.phone_number)<10:
				frappe.throw("Field Contact Number must be 10 Digits")
	
