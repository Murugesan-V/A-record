$(function() {
  var trid;
  $('.edit').click(function() {
       trid = $(this).attr('data'); // table row ID
       var domain_name=$('#'+trid+'_domain_name').html();
       $('#domain_name').val(domain_name);
}) });
