$(document).ready(function() {
    $("#search").keypress(function() {
        var searchVal =  $("#search").val();
        var url = 'http://localhost:9200/question-index/_search?q=' + searchVal + '~'
            jQuery.ajax({
            'url': url,
            'type': "get",
            success(data) {
                //console.log(data.hits.hits);
                var result = "";
                var hits = data.hits.hits;
                for(var i=0;i<hits.length; i++){
                    
                result += '<li><a href="#">'+ hits[i]._id + ' ' + hits[i]._source.content+'</a></li>';
                }
                result = '<ul>' + result + '</ul>'
                $("#searchResult").html(result);
            }
        });
    });
});
