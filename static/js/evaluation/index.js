function listaResult(){
	$.ajax({
		url:"/result-evaluativo/",
		type:"get",
		dataType: "json",
		success: function(response){
			console.log(response);
		},
		error: function(error){
			console.log(error);
		}
	});

}

$(document).ready(function (){
	listaResult();
});