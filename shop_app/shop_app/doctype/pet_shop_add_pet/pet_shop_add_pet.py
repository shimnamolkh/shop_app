# Copyright (c) 2022, shimna and contributors
# For license information, please see license.txt
import frappe
from frappe.model.document import Document

class PetShopAddPet(Document):

	def validate(self):
		self.create_available()

	def create_available(self):
		if self.status == 'Available' and not self.idn:
			doc = frappe.get_doc({
				"doctype": "Pet Shop Pets",
				"pet_name": self.pet_name,
				"pet_category":self.pet_category,
				"pet_price":self.pet_price,
				
			})
			doc.insert(ignore_permissions=True, ignore_mandatory=True)
			self.idn = doc.name

	