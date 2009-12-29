jQuery(document).ready(function($){
	$('#menu').css('height', 'auto');
	$('#menu ul').hide();
	$('#menu h3').click(function(){
		$(this).next().slideToggle(500).siblings('ul:visible').slideUp(500);
		$(this).toggleClass('corrente');
		$(this).siblings('#menu h3').removeClass('corrente');
	});
});
