$(document).ready(function(){
  
	$.ajax({
		url:'ajax/',
		method:'get',
		success: function(data){
			console.log(data[0])//[0]['fields'])
			$('#atable').dataTable({
  				data:data,

  				columns:[
  				{'data':'id'},//render:function(){return "id "}},
  				{'data':'domain_name'},
  				{'data':'redirect_url'},
  				{'data':'region'},
          {'data':'protocol'},
          {'data':'updated_date'},
          {'data':'user'},
          {'data':'comment'},
          {'data':null,render:function(){return '<button id="edit"  type="button" class="btn btn-primary" data-toggle="modal" data-target="#myModal">Edit</button>'}},
          {'data':null,render:function(){return "<button id='remove' class='btn btn-danger '>Delete</button>"} },          
  				]})

		}})

// $(document).ready(function(){
// $("body").on("click", '#remove',function(event){
//         var answer= confirm("Confirm Deletion")
//         if (answer){
//           var pid = $(this).closest('tr').children('td:nth(0)').text();
//           $.ajax({
//                 url:"delete/"+pid,//+"/",
//                 //data:{csrfmiddlewaretoken: '{{ csrf_token }}'},
//                 type:"GET",
//                 dataType:"json",
//                 success: function (data) {
//                         //$('#atable').DataTable().ajax.reload();
//                         window.location.replace("")//{% url 'home_view' %})
//                         alert(data.message);

//                       }});


//         }

//       })})


	})
  
    //'dom':'Bfrtip',
    //'buttons':['csv','excel','pdf','print']
  