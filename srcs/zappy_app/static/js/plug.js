$(document).ready(function(){
    var socket = new WebSocket('ws:127.0.0.1:8000/chat/');
    socket.onopen = websocket_welcome;
    socket.onmessage = websocket_message_show;
    $("#chatform").submit(function(e){
        e.preventDefault();
        message_data = {
            'username': $('input[name="username"]').val(),
            'usermsg': $('input["name="usermsg"]')val()
        }
        socket.send(JSON.strinify(message_data));
        $("#chatform")[0].reset();
    });

});
function websocket_welcome(){
    alert("welcome to chat room");
};
function websocket_message_show(e){
    message_data = JSON.parse(e.data);
    coding = "<h5>" + message_data.username + "</h5>" +
              "<p class='coding'>" + message_data.usermsg + "</p>";
     $("#messageCanvas").append(coding);
};