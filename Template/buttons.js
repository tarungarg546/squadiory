<script>
$(document).ready(function() {
        $.fn.myFunction = upvote(user_id,question_id)
        $.ajax({
            url: 'QueAns/ajax/upvote/'
            data: {
                user_id,question_id
            }
            type: "POST",
            success: function(data) {
              alert("Upvoted");
             },
            error: function(data) {
             alert("User has already voted for this question");
            },
        });
    });
</script>
    $(document).ready(function() {
    $.fn.myFunction = downvote(user_id,question_id)
        $.ajax({
            url: 'QueAns/ajax/downvote/'
            data: {
                user_id,question_id
            }
            type: "POST",
            success: function(data) {
              alert("Downvoted");
             },
            error: function(data) {
             alert("User has already voted for this question");
            },
        });
    });

    $(document).ready(function () {
    $.fn.myFunction = satisfied(user_id,question_id)
        $.ajax({
            url: 'QueAns/ajax/satisfied/'
            data: {
                user_id,question_id
            }
            type: "POST",
            success: function(data) {
              alert("Feedback Recorded");
             },
            error: function(data) {
             alert("You have already given your feedback");
            },
        });
    });

    $(document).ready(function () {
    $.fn.myFunction = disatisfied(user_id,question_id)
        $.ajax({
            url: 'QueAns/ajax/disatisfied/'
            data: {
                user_id,question_id
             }
            type: "POST",
            success: function(data) {
              alert("Feedback Recorded");
             },
            error: function(data) {
             alert("You have already given your feedback");
            },
        });
    });

