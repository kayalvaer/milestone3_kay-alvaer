/*
    jQuery for Bootstrap-MaterializeCSS initialization
*/

$(function() {
    $('#collapse-search').on('hidden.bs.collapse', function() {
      $('#search').val('')
    })
  });

/* bootstrapmaterial-design modal js */

$('#myModal').on('shown.bs.modal', function () {
  $('#myInput').trigger('focus')
})

$('#exampleModal').on('show.bs.modal', function (event) {
  var button = $(event.relatedTarget) // Button that triggered the modal
  var recipient = button.data('whatever') // Extract info from data-* attributes
  // If necessary, you could initiate an AJAX request here (and then do the updating in a callback).
  // Update the modal's content. We'll use jQuery here, but you could use a data binding library or other methods instead.
  var modal = $(this)
  modal.find('.modal-title').text('Details for' + recipient)
  modal.find('.modal-body input').val(recipient)
})

//collapsible enabler
$('.collapse').collapse()


//Tooltip enabler
$(function () {
  $('[data-toggle="tooltip"]').tooltip()
  
})

//bootstrapMaterialDesign
$(document).ready(function() { 
  $('body').bootstrapMaterialDesign(); 
});


//add multiple fields
$(document).ready(function() {
	var max_fields      = 10; //maximum input boxes allowed
	var wrapper   		= $(".input_fields_wrap"); //Fields wrapper
	var add_button      = $(".add_field_button"); //Add button ID
	
	var x = 1; //initlal text box count
	$(add_button).click(function(e){ //on add input button click
		e.preventDefault();
		if(x < max_fields){ //max input box allowed
			x++; //text box increment
			$(wrapper).append('<div><input type="text" name="mytext[]"/><a href="#" class="remove_field">Remove</a></div>'); //add input box
		}
	});
	
	$(wrapper).on("click",".remove_field", function(e){ //user click on remove text
		e.preventDefault(); $(this).parent('div').remove(); x--;
	})
});

//nav active
$(function() {
  $('nav a[href^="/' + location.pathname.split("/")[1] + '"]').addClass('active');
});