$(document).ready(function () {
    $(".formDescription").hide();
    $("#dateForm").focus(function() {
        $(this).next().fadeIn("fast");
    }).blur(function() {
        $(this).next().fadeOut("fast");
    });

//    $(".minusIcon").hide();
//    $(".educationFormRedo").hide()
//    $(".addIcon").click( function(){
//        $(".educationFormRedo").show();
//        $(this).hide("slow");
//        $(".minusIcon").show();
//         return false;
//    });
////
//    $(".educationFormRedo2 .minusIcon").hide();
//    $(".educationFormRedo2").hide();
//    $(".educationFormRedo .addIcon").click( function(){
//        $(".educationFormRedo2").show();
//        $(this).hide("slow");
//        $(".educationFormRedo2 .minusIcon").show();
//        $(".educationFormRedo2 .addIcon").hide();
//         return false;
//    });



    $(".addPopUp").hide();
    $(".addIcon").hover(function (){
    $(this).next("").show();
    });

});