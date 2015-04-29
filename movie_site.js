"use strict"
$(function () {
// Toggle the open/closed class setting for displaying supplemental movie info.
    $(".more_info button").each(function () {
        $(this).click(function () {
            $(this).parent().toggleClass("open closed");
            });
        });

    });


// Open modal and start playing the video whenever the trailer modal is opened
$(function () {
    $(".poster").each(function () {
        $(this).click(function () {
            $("#modal").css("display","block");
            $("#modal").parent().toggleClass("modal-parent");

            // Retrieve YouTube ID stored in data-trailer-youtube-id
            var trailerYouTubeId = $(this).parent().attr('data-trailer-youtube-id');
            var sourceUrl = 'http://www.youtube.com/embed/' + trailerYouTubeId + '?autoplay=1&html5=1';

            $("#video-container").empty().append($("<iframe></iframe>", {
                'id': 'trailer-video',
                'type': 'text-html',
                'src': sourceUrl,
                'frameborder': 0
            }));
        });
    });
});

// Close modal and remove iframe.
$(function () {
    $("#modal-close").click(function () {
        $("#video-container").empty();
        $("#modal").parent().toggleClass("modal-parent");
        $("#modal").css("display","none");
    });
});
