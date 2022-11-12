// Copyright (c) 2022, shimna and contributors
// For license information, please see license.txt

frappe.ui.form.on('Customer Bill', {
    validate: function(frm){
        var temp = cur_frm.doc.items_ordered;
        var sum = 0;
        for ( var i = 0; i < temp.length; i++)
        {
            var obj = temp[i];
            var amount = obj.price;
            sum = sum + amount;
        }
        frm.set_value("total",sum)
    },
    before_save:function(frm) {
		frm.set_value('net_amount',frm.doc.total - frm.doc.discount_amount)
    },
    customer_id: function(frm) {
		frappe.call({
			method:"frappe.client.get",
			args:{
				doctype:"Customer",
				name:frm.doc.customer_id,
			},
			callback:(r=>{
				if(r.message){
					frm.set_value('customer_name',r.message.customer_name)
				}
			})
		})
	},
	refresh: function(frm) {
		frm.add_custom_button('Back', () => {
            frappe.new_doc('Shop Customer Order', {
                student: frm.doc.name
            })
        })
	},

    // items_ordered: function(frm) {
	// 	frappe.call({
	// 		method:"frappe.client.get",
	// 		args:{
	// 			doctype:"Shop Item",
	// 			name:frm.doc.item_name,
	// 		},
	// 		callback:(r=>{
	// 			if(r.message){
    //                 for i in doc.items_ordered:
    //                     frm.set_value('item_name',r.message.i.item_name)
	// 				    frm.set_value('price',r.message.i.price)
	// 			}
	// 		})
	// 	})
	// },
// 	menu_check:function(frm) {
// 		frm.call({
// 			method:'all_menu_items_section',
// 			doc:frm.doc,
// 			args: {
// 				doctype:"Menu"
	
// 			},
// 			callback: function(r) {
// 				frappe.msgprint(__("successfully  updated"))
// 				frm.refresh_field('menu_table');
	
 });