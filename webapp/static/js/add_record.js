$(document).ready(function(){
  $('#atable').dataTable({
    //'dom':'Bfrtip',
    //'buttons':['csv','excel','pdf','print']
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
                      // $("#atable > tbody").append("<tr><td>"+data.id_data+"</td><td>"+domain_name+"</td><td>"+redirect_url+"</td><td>"+region+"</td><td>"+data.updated_date+"</td> <td>" +data.comment+ "</td><td>"+ data.user +"</td> <td><button type='button' class='btn btn-success' data-toggle='modal' data-target='#myModal'>Edit</button></td><td><button type='button' data="+data.id_data+" class='btn btn-danger' id='btn-del'>Delete</button></td></tr>");
                      // $("#myModal").modal("hide");
                      // $("#domain_name").val("");
                      // $("#redirect_url").val("");
                      // $("#region").val("");
                      // //$('[name="port"]:checked').val("http");
                      // $("#certificate").val("");
                      // $("#pub_key").val("");
                      // $("#chain_key").val("");

                      

                      //$("#atable > tbody").append("<tr><td>"+domain_name"</td><td>"data.redirect_url }}</td><td>{{ data.region }}</td><td>{{ data.updated_date }}</td> <td>{{ data.comment }}</td><td>{{ data.user }}</td></tr>")
                      
                 }

        }
    });
  });
});


// valdata= {  domain_name:domain_name,
//             redirect_url:redirect_url;
//             region:region;
//             protocol:protocol;
//             ssl_certificate:ssl_certificate;
//             public_key:public_key;
//             chain_key:chain_key;
//             csrfmiddlewaretoken: '{{ csrf_token }}' },


  // val datas= { domain_name:$("#domain_name").val(),
  //             redirect_url:$("#redirect_url").val(),
  //             region:$("#region").val(),
  //             commant:$("").val()
  //             protocol:$("").val()
  //             ssl_certificate:$("").val()
  //             public_key:$("").val()
  //             chain_key:$("").val()
  //             csrfmiddlewaretoken: '{{ csrf_token }}' },