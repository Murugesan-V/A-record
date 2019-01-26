

var pid
$(document).ready(function(){
$("body").on("click", '#edit',function(event){
        var pid = $(this).closest('tr').children('td:nth(0)').text();
        //alert(pid)
        $('#edit_btn').show()
        $('#submit_btn').hide()
        $.ajax({
                url:"edit_record_details/"+pid,//+"/",
                //data:{csrfmiddlewaretoken: '{{ csrf_token }}'},
                type:"GET",
                dataType:"json",
                success: function (data) {
                	    //$('#atable').DataTable().ajax.reload();
                        //window.location.replace("")//{% url 'home_view' %})
                    	console.log(data)   
                        pid = data[0]['id'];
                        $("#domain_name").val(data[0]['domain_name'])
                        $("#redirect_url").val(data[0]['redirect_url'])
                        $("#region").val(data[0]['region'])
                        //$("#domain_name").val(data[0]['domain_name'])
                        $("#certificate").val(data[0]['ssl_cert'])
                        $("#pub_key").val(data[0]['pub_key'])
                        $("#chain_key").val(data[0]['chain_key'])


		$("#edit_btn").click(function update(){
			  //alert(pid)
		      var domain_name = $("#domain_name").val();
		      var redirect_url = $('#redirect_url').val()
		      var region = $('#region').val()
		      var protocol = $('[name="port"]:checked').val()
		      var ssl_certificate = $("#certificate").val()
		      var public_key = $("#pub_key").val()
		      var chain_key = $("#chain_key").val()	

		      var data= { 
			            csrfmiddlewaretoken: '{{ csrf_token }}',
			            domain_name:domain_name,
			            redirect_url:redirect_url,
			            region:region,
			            protocol:protocol,
			            ssl_certificate:ssl_certificate,
			            public_key:public_key,
			            chain_key:chain_key,
			            csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val()
			             }
			  $.ajax({
			          type:'POST',
			          url:'update/'+pid,
			          csrfmiddlewaretoken: '{{ csrf_token }}',
			          data:data,
			        success:function(data){
			        	if (data.status == true ){
			                 window.location.replace("")
			                 console.log(data.status)
			                 alert('Record Updated!! ')}
			            else{
			            	alert('Validation Failed!!')
			            }


			             }})


					})


                      }});

      })})


