$(document).ready(function(){
	$("body").on("click", '#entry-btn',function(event){
		$('#submit_btn').show()
		// alert('hu')
		$('#edit_btn').hide()
		
		$("#domain_name").val("")
        $("#redirect_url").val("")
        $("#region").val("")
        //$("#domain_name").val(data[0]['domain_name'])
        $("#certificate").val("")
        $("#pub_key").val("")
        $("#chain_key").val("")
	})
	$("#data-form").on("submit",function (e) {
      e.preventDefault();
      var domain_name = $("#domain_name").val();
      var redirect_url = $('#redirect_url').val()
      var region = $('#region').val()
      var protocol = $('[name="port"]:checked').val()
      var ssl_certificate = $("#certificate").val()
      var public_key = $("#pub_key").val()
      var chain_key = $("#chain_key").val()
     
      console.log(domain_name) 
      console.log(redirect_url)
      console.log(region)
      console.log(protocol)
      console.log(ssl_certificate)
      console.log(public_key)

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
          url:'create/',
          csrfmiddlewaretoken: '{{ csrf_token }}',
          data:data,
        success:function(data){
                 console.log(data.status)
                 if (data.status == false){
                      alert('Validation Failed')
                      console.log(data)
                    }
                 else {
                      alert('Data Entered')
                      window.location.replace("")

         }

        }
    });
  });
});