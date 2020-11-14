// JavaScript Document
$(document).ready(function(){
     
    $('input').click(function(){
     
        resizeFont($(this));
     
    });
     
    function resizeFont( object ) {
         
        var o = object.val();
        var a = $('a,p,button,h6,strong,td');
         
        switch( o ) {
            case "A+"      : a.css('font-size',19); break;
            case "A"   : a.css('font-size',17); break;
            case "A-"    : a.css('font-size',14); break; 
        }
         
    }
 
});