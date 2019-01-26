
$(function() {
  var trid;
  $('#atable #btn-del').click(function() {
       trid = $(this).attr('data'); // table row ID
       //alert(trid);
       $.ajax({
        url:"delete/"+trid,//+"/",
        //data:{csrfmiddlewaretoken: '{{ csrf_token }}'},
        type:"GET",
        dataType:"json",
        success: function (data) {
                //$("#atable tr:eq("+trid+")").remove();
                window.location.replace("")//{% url 'home_view' %})
                //$("#"+trid).remove()
                alert(data.message)

              }
       //$.post("/delete/"+trid,{csrfmiddlewaretoken: '{{ csrf_token }}'}, function(data, status){
        //    alert("Status: " + status);
  });
})
  })
