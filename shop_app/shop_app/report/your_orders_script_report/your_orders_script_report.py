# Copyright (c) 2022, shimna and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
from six import iteritems
from frappe import _
import frappe
field_map = {
	"Your Orders": [
		"order_id"
		"customer_id",
		"ccustomer_name"
	],	
}

def execute(filters=None):
	if not filters:filters = {}

	columns, data = [], []
	columns = get_columns()
	cs_data = get_cs_data(filters)

	if not cs_data:
			frappe.msgprint(_("no records found")) 
			return columns, cs_data

	data = []
	for d in cs_data:
		row = frappe._dict({
				'order_id' :d.order_id,
				'ccustomer_name':d.ccustomer_name,
				'customer_id':d.customer_id,
			})
		data.append(row)
	return columns, data





def get_columns():
		return [
			{
				'fieldname': 'ccustomer_name',
				'label': ('CCustomer Name'),
				'fieldtype': 'Data',
				'width': '120'
			},
			{
				'fieldname': 'customer_id',
				'label': ('Customer Id'),
				'fieldtype': 'Link',
				'width': '120'
			},
			{
				'fieldname': 'order_id',
				'label': ('Order Id'),
				'fieldtype': 'Link',
				'width': '120'
			}  
		]


def get_cs_data(filters): 
		conditions = get_conditions(filters)
		data = frappe.get_all(
			doctype = 'Your Orders',
			fields = ['order_id','ccustomer_name','customer_id'],
			filters = conditions,
			order_by = 'customer_id desc'
		)
		return data


def get_conditions(filters):
		conditions = {}
		for key, value in filters.items():
			if filters.get(key):
				conditions[key] = value
		return conditions
	