// Copyright (c) 2022, shimna and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Shop Customer Order Script Report"] = {
	"filters": [

		{
			"reqd": 1,
			"fieldname":"order_id",
			"label": __("Select Order"),
			"fieldtype": "Link",
			"options": "Shop Customer Order",
			
		},

		
		{
			"fieldname":"customer_id",
			"label": __("Customer id"),
			"fieldtype": "Link",
			"options": "Customer",
				
				

				
		},

		{
			"fieldname":"price",
			"label": __("Select price"),
			"fieldtype": "Int",
			
		}
	]
		
};
