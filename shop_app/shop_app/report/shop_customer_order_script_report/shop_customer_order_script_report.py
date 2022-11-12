# Copyright (c) 2022, shimna and contributors
# For license information, please see license.txt
from __future__ import unicode_literals
from six import iteritems
from frappe import _
import frappe

field_map = {
	"Shop Customer Order": [
		"order_no"
		"customer_id",
		"customer_name",
		"item_name"
		"price",
		# "item_count",
	],	
}
def execute(filters=None):
	if not filters: filters = {}
	columns, data = [], []
	columns = get_columns()
	data = get_data(filters)
	if not data:
		frappe.msgprint(_("no records found")) 
		return columns, data
	datas = []
	for d in data:
		row = frappe._dict({
			'order_no':d.order_no,
			'customer_id':d.customer_id,
			'customer_name':d.customer_name,
			# 'item_name':d.item_name,
			'price':d.price,
			# 'item_count':d.item_count,
		})
		datas.append(row)
	# chart = get_chart_data(datas)
	# report_summary = get_report_summary(datas)
	# return columns, datas, None, chart, report_summary

def get_columns():
	return [
		{
			'fieldname': 'order_no',
			'label': _('Order no'),
			'fieldtype': 'Int',
			'width': '120'
		},
		{
			'fieldname': 'customer_id',
			'label': _('Customer id'),
			'fieldtype': 'Int',
			'width': '120'
		},
		{
			'fieldname': 'customer_name',
			'label': _('Customer name'),
			'fieldtype': 'Data',
			'width': '120'
		},
		# {
		# 	'fieldname': 'item_name',
		# 	'label': _('Item name'),
		# 	'fieldtype': 'Data',
		# 	'width': '120'
		# },
		{
			'fieldname': 'price',
			'label': _('Price'),
			'fieldtype': 'Int',
			'width': '120'
		},
	]

def get_data(filters):
	conditions = get_conditions(filters)
	datas = frappe.get_all(
		doctype = 'Shop Customer Order',
		fields = ['order_no','customer_id','customer_name'],
		filters = conditions,
		order_by = 'customer_name desc'
	)
	return datas

def get_conditions(filters):
	conditions = ""
	for key, value in filters.items():
		if filters.get("key"):
			conditions[key] = value
	return conditions	

# def get_chart_data(data):
# 	if not data:
# 		return None	

# 	labels = ['Order no >= 50','Order no < 50']

# 	order_no_data = {
# 		'Order no >= 50' : 0,
# 		'Order no < 50' : 0,

# 	}
# 	datasets = []

# 	for entry in data:
# 		if entry.order_no >= 50:
# 			order_no_data['Order no >= 50'] += 1

# 		else:
# 			order_no_data['Order no < 50'] += 1

# 	datasets.append({
# 		'name': 'Order no',
# 		'values': [order_no_data.get('Order no >= 50'),order_no_data.get('Order no < 50')]

# 	})

# 	chart = {
# 		'data': {
# 			'labels': labels,
# 			'datasets': datasets

# 		},
# 		'type':'line',
# 		'height': 300,
# 	}

# 	return chart

# def get_report_summary(data):
# 	if not data:
# 		return None

# 	order_no_below_50, order_no_above_50 = 0, 0


# 	for entry in data:
# 		if entry.order_no >= 50:
# 			order_no_above_50 += 1

# 		else:
# 			order_no_below_50 += 1

# 	return [
# 		{
# 			'value': order_no_below_50,
# 			'indicator': 'Red',
# 			'label':'Order no Below 50',
# 			'datatype':'Int',
# 		},
# 		{
# 			'value': order_no_above_50,
# 			'indicator': 'Green',
# 			'label':'Order no Above 50',
# 			'datatype':'Int',
# 		}
# 	]

