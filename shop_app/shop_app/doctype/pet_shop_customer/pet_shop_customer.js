// Copyright (c) 2022, shimna and contributors
// For license information, please see license.txt

frappe.ui.form.on('Pet Shop Customer', {

	// validate: function(frm) {
	// 	if (frm.doc.phone_number.length<10) {
	// 		frappe.throw('phone number is invalid');
	// 		validate = false;
	// 	// elif (frm.doc.phone_number.isdigit()) {

		
		// }
	
	date_of_birth: function (frm) {
		frappe.call({
		  doc:frm.doc,
		  method:'get_age',
		  callback:function(r){
			let doc = frm.doc
			doc.age = r.message
			frm.refresh_field('age')
		  }
		})
	},

	pet_check:function(frm) {
		frm.call({
			method:'pet_check_session',
			doc:frm.doc,
			args: {
				doctype:"Pet Shop Pets"
	
			},
			callback: function(r) {
				
				frappe.msgprint(__("successfully  updated"))
				frm.refresh_field('pet_table');
	
			}
		});
	}
});
