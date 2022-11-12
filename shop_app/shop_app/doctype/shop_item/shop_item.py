# Copyright (c) 2022, shimna and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class ShopItem(Document):
	pass
	def validate(self):
		self.create_available()
		


	def create_available(self):
		if self.i_status == 'Available' and not self.item_number:
			doc = frappe.get_doc({
				"doctype": "Shop Item Displays",
				"item_name":self.i_name,
				
				"item_image":self.item_image,
				"vehicle":self.i_vehicle,
				"price":self.i_price,
				"status":self.i_status,
				"item_id":self.i_id
				
			})
			doc.insert(ignore_permissions=True, ignore_mandatory=True)
			self.item_name = doc.name
