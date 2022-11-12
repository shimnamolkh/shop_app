// Copyright (c) 2022, shimna and contributors
// For license information, please see license.txt

frappe.ui.form.on('Customer', {
	// item: function(frm) {
	// 	frappe.call({
	// 		method: "frappe.client.get",
	// 		args: {
	// 			doctype:"Shop Item",
	// 			name:frm.doc.item

	// 		},
	// 		callback: (r) => {
	// 			if (r.message) {
	// 				frm.set_value('price',r.message.price)
					
	// 			}
	// 		}

	
	// 	});
	// },
	// order_2: function(frm) {
	// 	frappe.call({
	// 		method: "frappe.client.get",
	// 		args: {
	// 			doctype:"Shop Item Display",
	// 			name:frm.doc.order_2

	// 		},
	// 		callback: (r) => {
	// 			if (r.message) {
	// 				frm.set_value('price_2',r.message.i_price)
					
					
	// 			}
	// 		}

	
	// 	});
	// },
	// order_3: function(frm) {
	// 	frappe.call({
	// 		method: "frappe.client.get",
	// 		args: {
	// 			doctype:"Shop Item Display",
	// 			name:frm.doc.order_3

	// 		},
	// 		callback: (r) => {
	// 			if (r.message) {
	// 				frm.set_value('price_3',r.message.i_price)
					
					
	// 			}
	// 		}

	
	// 	});
	// },

	
		
	// before_save: function(frm) {
	// 	frm.set_value('total',(frm.doc.item_number) * (frm.doc.price))
		// frm.set_value('total_2',(frm.doc.number_order_2) * (frm.doc.price_2))           
		// frm.set_value('total_3',(frm.doc.number_order_3) * (frm.doc.price_3))
	// },	

});

