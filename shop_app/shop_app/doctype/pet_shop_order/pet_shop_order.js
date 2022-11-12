// Copyright (c) 2022, shimna and contributors
// For license information, please see license.txt

frappe.ui.form.on('Pet Shop Order', {
	validate: function(frm){
        var temp = cur_frm.doc.items;
        var sum = 0;
        for ( var i = 0; i < temp.length; i++)
        {
            var obj = temp[i];
            var amount = (obj.pet_price) * (obj.number);
            sum = sum + amount;
        }
        frm.set_value("total",sum)
    },
    before_save:function(frm) {
		frm.set_value('net_amount',frm.doc.total - frm.doc.discount)
    },

  setup: function(frm){
    frm.check_items_duplicate = function(frm, row){
      console.log(row)
      frm.doc.items.foreach(item=>{
        if(row.pet_name=='' || row.idx==item.idx){

        } else {
          if(row.pet_name==item.pet_name){
            row.pet_name = '';
            frappe.throw(_(`$(item.pet_name) already existsrow $(item.idx)`));
            frm.refresh_field('items');

          }
          
        }
        
      })
    }


  },
  // refresh: function(frm) {

  // }
});

