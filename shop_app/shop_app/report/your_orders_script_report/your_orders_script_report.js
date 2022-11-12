// Copyright (c) 2022, shimna and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Your Orders Script Report"] = {
	"filters": [
		{
			"reqd": 1,
			"fieldname": "Your Orders",
			"label": ("Select Order Id"),
			"fieldtype": "Link",
			"options": "Your Orders",
			

		
				
		},
		
		{
		"fieldname":"customer_id",
			"label":("Customer Id"),
			"fieldtype": "Link",
			"options": "Customer",
			



		},
	]
};
