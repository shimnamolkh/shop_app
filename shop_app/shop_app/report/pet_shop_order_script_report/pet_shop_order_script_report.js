// Copyright (c) 2022, shimna and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["pet shop order script report"] = {
	"filters": [
		// {
		// 		"fieldname": "id",
		// 		"label": __("ID"),
		// 		"fieldtype": "Int",
		// 		"reqd": 1
		// 	},
			{
				"fieldname": "customer_name",
				"label": __("Customer Name"),
				"fieldtype": "Data",
				// "reqd": 1
			},
			{
				"fieldname": "phone_number",
				"label": __("Phone Number"),
				"fieldtype": "Data",
				// "reqd": 1
			},
			{
				"fieldname": "order_id",
				"label": __("Order Id"),
				"fieldtype": "Int",
				// "options": "Pet Shop Pets"
				// "reqd": 1
			},	
			{
				"fieldname": "date",
				"label": __("Date"),
				"fieldtype": "Date",
				// "options": "Pet Shop Order",
				// "reqd": 1
			},
			{
				"fieldname": "discount",
				"label": __("Discount"),
				"fieldtype": "Int",
				// "options": "Pet Shop Pets",
				// "reqd": 1
			},
			{
				"fieldname": "gst",
				"label": __("Gst"),
				"fieldtype": "Int",
				// "options": "Pet Shop Pets"
			},
	
	

	]
};
