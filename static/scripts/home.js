
$("document").ready(function(){

   
 $("#addCommentBtn").click(function(){
    $.post("/addComment",
    {
        name: $("#commentName").val(),
        title:  $("#commentTitle").val(),
        content:  $("#commentContent").val()
    },
    function(data, status){
        location.reload();
    });
}); 


 $(".deleteButton").click(function(){
    $.post("/deleteComment",
    {
        id: this.id,
    },
    function(data, status){
        location.reload();
    });
}); 
});
