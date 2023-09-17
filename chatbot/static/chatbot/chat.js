// chat.js
function sendMessage() {
    let userMessage = $('#user_input').val();
    $('#chatbox').append('<p>You: ' + userMessage + '</p>');
    $.ajax({
        url: '/get_response/',
        method: 'POST',
        data: {
            'message': userMessage,
            'csrfmiddlewaretoken': '{{ csrf_token }}'
        },
        success: function(response) {
            $('#chatbox').append('<p>Bot: ' + response.message + '</p>');
        }
    });
    $('#user_input').val('');
}
