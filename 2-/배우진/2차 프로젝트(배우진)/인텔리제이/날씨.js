

$(document).ready(function () { // HTML 문서가 로드될 때 실행되는 함수를 정의
    var socket = new WebSocket("ws://localhost:8060");  // WebSocket 연결

        const list = document.querySelector('#a');

        const newListItem = document.createElement('li'); // 새로운 li 요소를 만듬
        newListItem.classList.add('list-item'); // list-item 클래스를 더해줌

        newListItem.innerHTML = "16시";

        list.appendChild(newListItem); // 리스트에 새로 만든 li를 추가



    socket.onmessage = function (event) {
        // 전달 받은 제이슨 형식을 자바스크립트의 객체로 변환
        var data = JSON.parse(event.data);  // 받은 데이터 파싱
    }


    });
