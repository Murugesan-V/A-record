$(document).ready(function(){
$("body").on("click", '#remove',function(event){
        var answer= confirm("Confirm Deletion")
        if (answer){
          var pid = $(this).closest('tr').children('td:nth(0)').text();
          $.ajax({
                url:"delete/"+pid,//+"/",
                //data:{csrfmiddlewaretoken: '{{ csrf_token }}'},
                type:"GET",
                dataType:"json",
                success: function (data) {
                        //$('#atable').DataTable().ajax.reload();
                        window.location.replace("")//{% url 'home_view' %})
                        alert(data.message);

                      }});
        }

      })})