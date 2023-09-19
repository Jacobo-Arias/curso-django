var passwordInput = document.getElementById("like-post");
var likeUrl = passwordInput.getAttribute("data-like-url");
passwordInput.addEventListener("click", function () {
    $.ajax({
        url: likeUrl,
        type: "POST",
        data: { csrfmiddlewaretoken: csrf_token },
        success: function (json) {
            var postLikesCountElement = document.getElementById("post_likes_count");
            if (json.is_liked) {
                postLikesCountElement.innerHTML = json.likes_count;
                $("#like-post").html('<i class="fa fa-heart" style="color: red"></i>');
            } else {
                postLikesCountElement.innerHTML = json.likes_count;
                $("#like-post").html('<i class="far fa-heart"></i>');
            }
        },
        error: function (xhr, errmsg, err) {
            console.log(xhr.status + ": " + xhr.responseText);
        },
    })
});