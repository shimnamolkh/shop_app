# Copyright (c) 2022, shimna and contributors
# For license information, please see license.txt

# import frappe


from __future__ import unicode_literals
from six import iteritems
from frappe import _
import frappe

def execute(filters=None):
	columns, data = [], []
	columns = get_columns()
	data = get_data(filters)
	if not data:
		frappe.msgprint(_("no records found")) 
		return columns, data
	datas = []
	for d in data:
		row = frappe._dict({
			# 'pet_name':d.pet_name,
			# 'pet_category':d.pet_category,
			'customer_name':d.customer_name,
			'phone_number':d.phone_number,
			'order_id':d.order_id,
			'date':d.date,
			'discount':d.discount,
			'gst':d.gst,
		})
		datas.append(row)
	chart = get_chart_data(datas)
	report_summary = get_report_summary(datas)
	return columns, datas, None, chart, report_summary

def get_columns():
	return [
			{
				"fieldname": "customer_name",
				"label": ("Customer Name"),
				"fieldtype": "Data",
				# "reqd": 1
				'width':200
			},
			{
				"fieldname": "phone_number",
				"label": ("Phone Number"),
				"fieldtype": "Data",
				# "reqd": 1
				'width':200
			},
			{
				"fieldname": "order_id",
				"label": ("Order Id"),
				"fieldtype": "Int",
				# "options": "Pet Shop Pets"
				'width':200
			},
			{
				"fieldname": "date",
				"label": ("Date"),
				"fieldtype": "Date",
				# "options": "Pet Shop Order"
				'width':200
			},
			{
				"fieldname": "discount",
				"label": ("Discount"),
				"fieldtype": "Int",
				# "options": "Pet Shop Pets",
				# "reqd": 1
				'width':200
			},
			{
				"fieldname": "gst",
				"label": ("Gst"),
				"fieldtype": "Int",
				# "options": "Pet Shop Pets"
				'width':200
			},
		
	]
def get_data(filters):
	datas = frappe.get_all(
		doctype = 'Pet Shop Order',
		fields = ['customer_name','phone_number','order_id','discount','date','gst'],
		# filters = conditions,
		order_by = 'customer_name desc'
		)
	data = []
	filter_data = []
	if filters.get('customer_name'):
		for i in datas:
			if i.get('customer_name') == filters.get('customer_name'):
				filter_data.append(i)
		datas = filter_data
	filter_data = []
	if filters.get('phone_number'):
		for i in datas:
			if i.get('phone_number') == filters.get('phone_number'):
				filter_data.append(i)
		datas = filter_data
	filter_data = []
	if filters.get('order_id'):
		for i in datas:
			if i.get('order_id') == filters.get('order_id'):
				filter_data.append(i)	
		datas = filter_data
	filter_data = []
	if filters.get('date'):
		for i in datas:
			if i.get('date') == filters.get('date'):
				filter_data.append(i)
		datas = filter_data
	# return datas
	filter_data = []
	if filters.get('discount'):
		for i in datas:
			if i.get('discount') == filters.get('discount'):
				filter_data.append(i)
		datas = filter_data
	filter_data = []
	if filters.get('gst'):
		for i in datas:
			if i.get('gst') == filters.get('gst'):
				filter_data.append(i)
		datas = filter_data

	return datas

def get_chart_data(datas):
	if not datas:
		return None	

	labels = ['Discount > 500','Discount < 500']
	discount_data = {
		'Discount > 500' : 0,
		'Discount < 500' : 0,
	}
	datasets = []
	for entry in datas:
		if entry.discount > 500:
			discount_data['Discount > 500'] += 1
		else:
			discount_data['Discount < 500'] += 1
	datasets.append({
		'name': 'Discount',
		'values': [discount_data.get('Discount > 500'),discount_data.get('Discount < 500')]
	})
	chart = {
		'data': {
			'labels': labels,
			'datasets': datasets
		},
		'type':'pie',
		'height': 300,
	}

	return chart

def get_report_summary(datas):
	if not datas:
		return None	
	discount_below_500, discount_above_500 = 0, 0

	for entry in datas:
		if (entry.discount > 500):
			discount_above_500 += 1
		else:
			discount_below_500 += 1
	return [{
		'value': discount_below_500,
		'indicator': 'Green',
		'label': 'Discount below 500',
		'datatype': 'Int'
	},
	{
		'value': discount_above_500,
		'indicator': 'Blue',
		'label': 'Discount above 500',
		'datatype': 'Int'
	}		
	]