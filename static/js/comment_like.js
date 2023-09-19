var passwordInput = document.getElementById("like-comment");
var likeUrl = passwordInput.getAttribute("data-like-url");
passwordInput.addEventListener("click", function () {
    $.ajax({
        url: likeUrl,
        type: "POST",
        data: { csrfmiddlewaretoken: csrf_token },
        success: function (json) {
            var commentLikesCountElement = document.getElementById("comment_likes_count");
            if (json.is_liked) {
                commentLikesCountElement.innerHTML = json.likes_count;
                $("#like-comment").html('<i class="fa fa-heart" style="color: red"></i>');
            } else {
                commentLikesCountElement.innerHTML = json.likes_count;
                $("#like-comment").html('<i class="far fa-heart"></i>');
            }
        },
        error: function (xhr, errmsg, err) {
            console.log(xhr.status + ": " + xhr.responseText);
        },
    })
});