/*
*
 * Created by yangzhiqiang on 2017/4/26.
 */

var chess = document.getElementById("chess");
var context = chess.getContext('2d');
context.strokeStyle = "#2";

//绘制棋板
var drawChessBoard = function () {
    for (var i = 0; i < 9; i++) {
        context.moveTo(50 + i * 50, 50);
        context.lineTo(50 + i * 50, 450);
        context.fillText(i, 45 + i * 50, 30);
        context.stroke();
        context.moveTo(50, 50 + i * 50);
        context.lineTo(450, 50 + i * 50);
        context.fillText(i, 25, 55 + i * 50);
        context.stroke();
    }
}

//给棋盘设置背景
//var img = new Image();
//img.src = "/static/imgs/chessbackground.png";
//img.onload = function () {
  //  context.drawImage(img, 0, 0, 500, 500);
drawChessBoard();
//}

// drawChessBoard();

//下一颗棋子，x为true是黑棋 false是白棋
var onestep = function (j, i, x) {
    context.beginPath();
    context.arc(50 + i * 50, 50 + j * 50, 20, 0, 2 * Math.PI);
    context.closePath();
    var gradient = context.createRadialGradient(50 + i * 50 + 2, 50 + j * 50 - 2, 20, 50 + i * 50 + 2, 50 + j * 50 - 2, 0);
    if (x) {
        gradient.addColorStop(0, "#0A0A0A");
        gradient.addColorStop(1, "#636766");
    } else {
        gradient.addColorStop(0, "#D1D1D1");
        gradient.addColorStop(1, "#F9F9F9");
    }
    context.fillStyle = gradient;
    context.fill();
}


var Alocation = true;
var Blocation = false;

// 设置全局的数组，存放棋子步骤
var step = [];

//getDate函数，与后台通信
function getData() {
    $.ajax({
        type: "GET",

        async: true,

        url: "/getdata",

        dataType: "json",

        success: function (data) {

            // console.log(data.result);

            //             console.log(data.result.length);
            if (data.result.length == 0) {
                location.reload([bForceGet = true])
            }
            step = [];
            for (r in data.result) {
                console.log(data.result[r]);
                res = data.result[r];
                if (res[2] != "") {
                    a = res[2].split(",");
                    console.log(res[2]);
                    a.push("Alocation");
                    step.push(a);
                }
                if (res[3] != "") {
                    b = res[3].split(",");
                    // b.push("Blocation");
                    console.log(res[3]);
                    step.push(b);
                }
            }

            // for(s in step){
            //         onestep(step[s][0],step[s][1], step[s][2]);
            //     }


            // onestep(step[s][0], step[s][1], step[s][2]);
            // onestep(step[0][0],step[0][1],step[0][2]);


            //

            // console.log(data.result[0][4]);
            // console.log(data.result[0][4].split(","));
            // a = data.result[0][4].split(",");
            // onestep(a[0],a[1],Alocation);
            // console.log(data.result[0][3]);
            // b = data.result[0][3].split(",");
            // onestep(b[0],b[1],Blocation);


            //设置长轮询，2秒的延迟。就是不断的运行getData()函数
            setTimeout(function () {

                getData();

            }, 800);

        }　　　　　　　　　　　　　　//成功时的回调函数，处理返回数据，并且延时建立新的请求连接

    });
}


// function timeMachine() {
//     console.log("timeMachine：" + timeControl);
//     if (timeControl == 1) {
//         setTimeout(function () {
//
//             n();
//
//         }, 200);
//     }
// }

//打开网页时，就运行获取getData函数
getData();


var s = -1;

//下棋
var next = function (s) {
    onestep(step[s][0], step[s][1], step[s][2]);
}


// var n = function () {
//     x = s + 1;
//     if (step.length > x) {
//         s++;
//         next(s);
//         console.log(s);
//     }
// }/


// var timeControl = 1;




//上一步
var upstep = function (j, i, x) {
     var context1 = chess.getContext('2d');
    context1.beginPath();
    context1.arc(50 + i * 50, 50 + j * 50, 20, 0, 2 * Math.PI);
    context1.closePath();
    var gradient = context.createRadialGradient(50 + i * 50 + 2, 50 + j * 50 - 2, 20, 50 + i * 50 + 2, 50 + j * 50 - 2, 0);
    if (x) {
        gradient.addColorStop(0, "#f0d7af");
        gradient.addColorStop(1, "#f0d7af");
    } else {
        gradient.addColorStop(0, "#f0d7af");
        gradient.addColorStop(1, "#f0d7af");
    }
    context1.fillStyle = gradient;
    context1.fill();
    x = 50 + i * 50;
    xa= 30 + j * 50;
    xb = 70 + j *50;

    y = 50 + j*50;
    ya = 30 + i *50;
    yb = 70 + i *50;
    console.log("原值为："+ i + " " + j +" "+ x + xa + xb + " "+ y + ya + yb);

    if (i == 0){
        xa = xa + 20;
    }
    if (j == 0){
        ya = ya + 20;
    }
    if (i == 8){
        yb = yb - 20;
    }
    if (j == 8){
        xb = xb - 20;
    }
    context.moveTo(x, xa);
    context.lineTo(x, xb);
    context.stroke();
    context.moveTo(ya, y);
    context.lineTo(yb, y);
    context.stroke();

}

//按钮，上一步按钮
var up = function (s) {
    upstep(step[s][0], step[s][1], step[s][2]);
}


function n() {
    clearTimeout(autotime);

    timeControl = 0;
    x = s + 1;
    console.log("step长度:" + step.length);
    if (step.length > x) {
        s++;
        next(s);
        console.log(s);
    }


    // timeMachine();
    // setTimeout(function () {
    //
    //     n();
    //
    // }, 2000);

}

//自动播放
function auto() {
    x = s + 1;
    console.log("step长度:" + step.length);
    if (step.length > x) {
        s++;
        next(s);
        console.log(s);
    }
    autotime = setTimeout(function () {

        auto();

    }, 10);

}

auto()


var u = function () {
    clearTimeout(autotime);
    up(s);
    s--;
    console.log(s)
    console.log("上一步time" + timeControl)
    // var a = s--;
    // location.reload([bForceGet = true])
    // for(a; a>=0;a--){
    //     onestep(step[s][0], step[s][1], step[s][2]);
}


// function getData() {
//     $.ajax({
//         type: "GET",
//
//         async: true,
//
//         url: "/getdata",
//
//         dataType: "json",
//
//         success: function (data) {
//
//             console.log(data.result);
//             console.log(data.result.length);
//             if (data.result.length == 0){
//                 location.reload([bForceGet = true])
//             }
//
//             for (r in data.result) {
//                 console.log(data.result[r]);
//                 res = data.result[r];
//                 if (res[2] != null) {
//                     a = res[2].split(",");
//                     onestep(a[0], a[1], Alocation);
//                 }
//                 if (res[3] != null) {
//                     b = res[3].split(",");
//                     onestep(b[0], b[1], Blocation);
//                 }
//             }
//
//             //长轮询
//             setTimeout(function () {
//
//                 getData();
//
//             }, 2000);
//
//         }　　　　　　　　　　　　　　//成功时的回调函数，处理返回数据，并且延时建立新的请求连接
//
//     });
// }
//
//
// getData();









