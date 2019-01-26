$(document).ready(function(){

var error_domain_name=false;
var error_redirect_url=false;
var error_region=false;
var error_ssl_cert=false;
var error_pub_key=false;
var error_chain_key=false;
var error_comment=false;

$("#error1").hide()


//$("#domain_name").on('input', function() {
$("#domain_name").on("change keyup paste click", function(){
    var len = $(this).val().length; //alert(len);
	if (len > 0 ){
                $("#domain_name").css("border-bottom","2px solid #34f458");
               //$("#error1").hide(); 
        } else{
               $("#domain_name").css("border-bottom","2px solid red");
               //$("#error1").show();
        }                                                              
})


$("#redirect_url").on("change keyup paste click", function(){
    var len = $(this).val().length; //alert(len);
        if (len > 0 ){
                $("#redirect_url").css("border-bottom","2px solid #34f458");
               $("#error2").hide();
        } else{
               $("#redirect_url").css("border-bottom","2px solid red");
               $("#error2").show();
        }
})

$("#region").on("change keyup paste click", function(){
    var len = $(this).val().length; //alert(len);
        if (len > 0 ){
                $("#region").css("border-bottom","2px solid #34f458");
               $("#error3").hide();
        } else{
               $("#region").css("border-bottom","2px solid red");
               $("#error3").show();
        }
})

$("#certificate").on("change keyup paste click", function(){
    var len = $(this).val().length; //alert(len);
        if (len > 0 ){
                $("#certificate").css("border-bottom","2px solid #34f458");
               $("#error4").hide();
        } else{
               $("#certificate").css("border-bottom","2px solid red");
               $("#error4").show();
        }
})

$("#pub_key").on("change keyup paste click", function(){
    var len = $(this).val().length; //alert(len);
        if (len > 0 ){
                $("#pub_key").css("border-bottom","2px solid #34f458");
               $("#error5").hide();
        } else{
               $("#pub_key").css("border-bottom","2px solid red");
               $("#error5").show();
        }
})

$("#chain_key").on("change keyup paste click", function(){
    var len = $(this).val().length; //alert(len);
        if (len > 0 ){
                $("#chain_key").css("border-bottom","2px solid #34f458");
               $("#error6").hide();
        } else{
               $("#chain_key").css("border-bottom","2px solid red");
               $("#error6").show();
        }
})





})





