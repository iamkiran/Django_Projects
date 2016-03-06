$(document).ready(function(){

$("#loading-image").hide();

$("div[id^='rnd']").mouseenter(function(){
    $(this).css({
        "margin-bottom": "13px",
        "background-color": "#bebebe",
         "color":"#ffffff",
         "margin-top": "18px",
        });
   $(this).find("#imgh5").css( {
    "margin-top": "18px"} );
});
$("div[id^='rnd']").mouseleave(function(){
   $(this).css({
        "margin-bottom": "23px",
    });
    $(this).removeAttr( 'style' );
});


 

$("img[id$='thumb']").mouseenter(function(){
   
    $(this).css({
      
   "width":"220px",
   "height":"220px",
});
});

$("img[id$='thumb']").mouseleave(function(){
    
    $(this).css({
     "width":"200px","height":"200px",
});
});

$("li[id^='songs']").click( function(){
    
    $("#loading-image").hide();
   //alert($(this).children("a").text()) ;
    $.ajax({

    data:{songType: $(this).children("a").text()},
    url: "classical",

    success: function(result){
   // alert(result);
    $("#main-content").html(result);
    //$("#loading-image").hide();
    }})
});

});

function goHome(){
    location.reload();
}
