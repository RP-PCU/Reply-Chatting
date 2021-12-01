// variables
let userName = null;
let state = 'SUCCESS';

// functions
function Message(arg) {
    this.text = arg.text;
    this.message_side = arg.message_side;

    this.draw = function (_this) {
        return function () {
            let $message;
            $message = $($('.message_template').clone().html());
            $message.addClass(_this.message_side).find('.text').html(_this.text);
            $('.messages').append($message);

            return setTimeout(function () {
                return $message.addClass('appeared');
            }, 0);
        };
    }(this);
    return this;
}

function getMessageText() {
    let $message_input;
    $message_input = $('.message_input');
    return $message_input.val();
}

function sendMessage(text, message_side) {
    let $messages, message;
    $('.message_input').val('');
    $messages = $('.messages');
    message = new Message({
        text: text,
        message_side: message_side
    });
    message.draw();
    $messages.animate({scrollTop: $messages.prop('scrollHeight')}, 300);
}

function greet() {
    setTimeout(function () {
        return sendMessage("배재봇에 오신걸 환영합니다.", 'left');
    }, 1000);

    setTimeout(function () {
        return sendMessage("사용할 닉네임을 알려주세요.", 'left');
    }, 2000);
}

function onClickAsEnter(e) {
    if (e.keyCode === 13) {
        onSendButtonClicked()
    }
}

function setUserName(username) {

    if (username != null && username.replace(" ", "" !== "")) {
        setTimeout(function () {
            return sendMessage("반갑습니다." + username + "님. 닉네임이 설정되었습니다.", 'left');
        }, 1000);
        setTimeout(function () {
            return sendMessage("저는 배재대학교의 관련된 내용을 알려주는 배재봇입니다.", 'left');
        }, 2000);
        setTimeout(function () {
            return sendMessage("배재대학교 건물위치,맛집, 교수님 정보에 대해 물어봐주세요!", 'left');
        }, 3000);
        setTimeout(function () {
            return sendMessage("질문앞에 배재대 혹은 배재대학교를 붙여서 질문해주세요!", 'left');
        }, 4000);

        return username;

    } else {
        setTimeout(function () {
            return sendMessage("올바른 닉네임을 이용해주세요.", 'left');
        }, 1000);

        return null;
    }
}

function requestChat(messageText, url_pattern) {
    $.ajax({
        url: "http://127.0.0.1:8080/" + url_pattern + '/' + userName + '/' + messageText + '/' + professor,
        type: "GET",
        dataType: "json",
        success: function (data) {
            state = data['state'];

            if (state === 'SUCCESS') {
                return sendMessage(data['answer'], 'left');
            } else if (state === 'REQUIRE_LOCATION') {
                return sendMessage('배재대 혹은 배재대학교를 입력해주세요!', 'left');
            } else {
                return sendMessage('죄송합니다. 무슨말인지 잘 모르겠어요.', 'left');
            }
        },

        error: function (request, status, error) {
            console.log(error);

            return sendMessage('죄송합니다. 서버 연결에 실패했습니다.', 'left');
        }
    });
}

function onSendButtonClicked() {
    let messageText = getMessageText();
    sendMessage(messageText, 'right');

    if (userName == null) {
        userName = setUserName(messageText);

    } else {
        if (messageText.includes('안녕')) {
            setTimeout(function () {
                return sendMessage("안녕하세요. 저는 배재봇입니다.", 'left');
            }, 1000);
        } else if (messageText.includes('고마워')) {
            setTimeout(function () {
                return sendMessage("천만에요. 더 물어보실 건 없나요?", 'left');
            }, 1000);
        } else if (messageText.includes('없어')) {
            setTimeout(function () {
                return sendMessage("그렇군요. 알겠습니다!", 'left');
            }, 1000);
<<<<<<< HEAD
        }
        else if (messageText.includes('교수님')){
            setTimeout(function () {
                return sendMessage("찾으실 교수님 성함을 입력해주세요", 'left');
            }, 1000);
        } 
        else if (state.includes('REQUIRE')) {
=======


        }else if (messageText.includes('교수님')){
                setTimeout(function () {
                    return sendMessage("찾으실 교수님 성함을 입력해주세요", 'left');
                }, 1000);
                return requestChat(messageText, 'get_prof');
            
    
        
        
        } else if (state.includes('REQUIRE')) {
>>>>>>> 8ff3379d27a573de21409c5a3112cd4798963c32
            return requestChat(messageText, 'fill_slot');
        } else if(state.includes('REQUEST_PROF')) {
            return requestChat(messageText, 'get_prof');
        } else {
            return requestChat(messageText, 'request_chat');
        }   
    }
}
/*
function professorAnswer() {
    if(messageText.includes("교수님")) {
        setTimeout(function () {
            return sendMessage("찾으실 교수님 성함을 입력해주세요.", 'left');
        }, 1000);
        // 1. child-process모듈의 spawn 취득 
        const spawn = require('child_process').spawn;
        // 2. spawn을 통해 "python 파이썬파일.py" 명령어 실행
        const result = spawn('python', ['hyocrawl.py']); 
        // 3. stdout의 'data'이벤트리스너로 실행결과를 받는다. 
        result.stdout.on('data', function(data) { 
            console.log(data.toString());}); 
        // 4. 에러 발생 시, stderr의 'data'이벤트리스너로 실행결과를 받는다. 
        result.stderr.on('data', function(data) { 
            console.log(data.toString()); });
    }
}
*/