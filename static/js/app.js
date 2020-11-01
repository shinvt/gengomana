$(document).ready(function(){
    // -----------------Like Button----------------------
    var likeBtnClick = function(e){
        var recipeID = e.currentTarget.id.split("_")[1];
        $.ajax({
            url: '/recipes/'+recipeID+'/like/',
            dataType: 'json',
            success: function (data) {
              var like_status = data;
        			if (like_status.Success == "True") {
          			$(e.currentTarget).css("color", "red");
          			$('#like-count' + '_' + recipeID).text(like_status.count);
        			} else if (like_status.Removed == "True") {
                $(e.currentTarget).css("color", "white");
          			$('#like-count' + '_' + recipeID).text(like_status.count);
              }
            },
            error: function(data) {
             	console.log("AJAX's like error")
            }/*  end of error */
        });
    }

    $('.like-icon').on('click', likeBtnClick);

    $(".dropdown-trigger").dropdown();

    $('.sidenav').sidenav();

    $('.tooltipped').tooltip();

});
