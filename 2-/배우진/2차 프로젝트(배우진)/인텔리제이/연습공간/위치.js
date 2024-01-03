const socket = new WebSocket("ws://localhost:8060");
socket.onopen = () => {
    console.log("웹소켓 연결!");
    const dataToSend = [latitude,longitude];
    socket.send(dataToSend);
    console.log("위도 : " + latitude + "경도 : " + longitude + "전송 완료!")
};

socket.onmessage = (event) => {
    console.log("날씨 데이터 수집 완료!")
    const dataToSend = { '': 'value' };

    fetch('/sendData', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(dataToSend)
    })
        .then(response => response.text())
        .then(result => {
            console.log('서버로부터의 응답:', result);
        })
        .catch(error => {
            console.error('에러 발생:', error);
        });

};

navigator.geolocation.getCurrentPosition((position) => {
    latitude = position.coords.latitude;
    longitude = position.coords.longitude;
}, (err) => {
    console.error('Error getting location:', err);
});