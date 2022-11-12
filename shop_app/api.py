import frappe
from frappe.model.document import Document


@frappe.whitelist()
# def get_choose_items_area(choose_items):
# 	area = frappe.db.sql(f""" SELECT i_id,i_price FROM `tabShop Item` WHERE i_name ='{choose_items}' """, as_dict=True)
# 	return area

# def get_item_name1_area(item_name1):
# 	area = frappe.db.sql(f""" SELECT item_id,price FROM `tabShop Item Displays` WHERE item_name ='{item_name1}' """, as_dict=True)
# 	return area
def get_pets_area(pets):
	area = frappe.db.sql(f""" SELECT pet_name,pet_category,pet_price FROM `tabPet Shop Add Pet` WHERE pet_name ='{pets}' """, as_dict=True)
	return area