$(document).ready(function(){

	$('.nav_cell').hover(
   		function(){
      		$(this).css("background-color", "#A4A4A4");
   		}, function(){
      		$(this).css("background-color", "#D8D8D8");
   		}
	);
	
	$( ".nav_cell" ).click(function() {
  		team_id = $(this).attr('id');
  		//alert(team_id);
  		document.location.href = '/teams/' + team_id;
  	});
	
});
