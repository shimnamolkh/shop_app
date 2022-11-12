// Copyright (c) 2022, shimna and contributors
// For license information, please see license.txt

frappe.ui.form.on('Item Orders', {
	item: function(frm) {
		frappe.call({
			method: "frappe.client.get",
			args: {
				doctype:"Shop Item",
				name:frm.doc.item

			},
			callback: (r) => {
				if (r.message) {
					frm.set_value('price',r.message.price)
					
				}
			}

	
		});
	},
});
