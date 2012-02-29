$(document).ready(function() {
    getWord("");
})

function getWord(prevLetter) {
    $.ajax({url:"/signlang", timeout: 10000000,
            dataType:'json', success: function(data) {
                //Push to html
                $("#currentImgTag").attr("src","/static/images/"+data.word+".png");
                if (prevLetter !== "") {
                    $("ul#recentTransList").append("<li>"+data.word+"</li>");
                }
                getWord(data);
            }
    });
}
