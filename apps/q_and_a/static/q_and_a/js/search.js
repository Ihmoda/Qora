$(document).ready(function() {
    $("#search").keyup(function() {
        var searchVal =  $("#search").val();
        if(searchVal.length > 3){
            var url = 'http://localhost:9200/question-index/_search?q=' + searchVal + '~'
                jQuery.ajax({
                'url': url,
                'type': "get",
                success(data) {
                    //console.log(data.hits.hits);
                    var result = "";
                    var hits = data.hits.hits;
                    for(var i=0;i<hits.length; i++){
                        
                    result += '&nbsp; <a href="/answers/question/'+ hits[i]._id + '"> ' + hits[i]._source.content+'</a><br>';
                    }
                    if(result.length > 0){
                        // result = '<ul>' + result + '</ul>'
                        $("#searchResult").html(result);
                    } else {
                        result = "";
                        $("#searchResult").html(result);
                    }
                    
                }
            });
        } else {
            result = "";
            $("#searchResult").html(result);
        }
    });
});
