// ----------removes active nav indicator----------
$(document).on('click', '.nav-link.active', function() { 
    var href = $(this).attr('href').substring(1); 
    //alert(href); 
    $(this).removeClass('active'); 
    $('.tab-pane[id="' + href + '"]').removeClass('active'); 
    
}); 
$(document).mouseup(function(e) { 
    var container = $("#tablist"); // target ID or class 
    // if the target of the click isn't the container nor a descendant of the container 
    if (!container.is(e.target) && container.has(e.target).length === 0) { 
        // get Event here 
        $('.active').removeClass('active'); 
    } 
}); 
//----------/removes active nav indicator----------