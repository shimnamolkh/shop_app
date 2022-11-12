// Copyright (c) 2022, shimna and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Pet Shop Add Pet script report"] = {
	"filters": [
		// {
		// 	"fieldname": "idn",
		// 	"label": __("idn"),
		// 	"fieldtype": "Int",
		// 	"reqd": 1
		// },
		{
			"fieldname": "pet_name",
			"label": __("Pet name"),
			"fieldtype": "Data",
			// "reqd": 1
		},
		{
			"fieldname": "pet_category",
			"label": __("Pet category"),
			"fieldtype": "Data",
			// "reqd": 1
		},
		// {
		// 	"fieldname": "pet_name",
		// 	"label": __("Pet name"),
		// 	"fieldtype": "Data",
		// 	"options": "Pet Shop Pets"
		// },
		// {
		// 	"fieldname": "pet_category",
		// 	"label": __("Pet category"),
		// 	"fieldtype": "Data",
		// 	"options": "Pet Shop Pets"
		// },
		{
			"fieldname": "pet_price",
			"label": __("Pet price"),
			"fieldtype": "Int",
			// "options": "Pet Shop Pets",
			// "reqd": 1
		},
		{
			"fieldname": "number",
			"label": __("Number"),
			"fieldtype": "Int",
			// "options": "Pet Shop Pets"
		},


	]
};
