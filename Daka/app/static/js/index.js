/**
 * Created by yangzhiqiang on 2017/4/10.
 */

$('body').scrollspy({target: '#navbar-example'})

var register = function () {
    var password = document.getElementById("inputPassword");
    passwordValue = password.value;
    var password1 = document.getElementById("inputPassword1");
    password1Value = password1.value;
    var nickname = document.getElementById("inputName");
    nicknameValue = nickname.value;
    console.log(nicknameValue)
    if (passwordValue == '' || nicknameValue == '') {
        console.log("kong");
        $('.alert-input-null').show();

    }
    else if (passwordValue == password1Value) {
        console.log("success")
        $.ajax({
            url: "/register",
            data: {
                nicknameValue: nicknameValue,
                passwordValue: passwordValue,
            },
            dataType: 'JSON',
            success: function (data) {
                console.log(data.result);
                if (data.result == "success") {
                    $(".register").hide();
                    $(".register-success").show();
                    $(".modal-body").append("<p>Success</p>");
                    $("#register").hide()
                }
                else {
                    $(".modal-body").append("<p>UnSuccess</p>");
                }
            }
        });
    }
    else {
        $('.alert-password-error').show()
    }
}

var nav_register = function () {
    $("#register").show();
}


var logout = function () {
    $.ajax({
        url: "/logout",
    });
}

var login  = function () {
    console.log("hhhhh")
    console.log($('#nickname').val())
    console.log($('#password').val())
    $.ajax({
        url: "/login",
        data: {
            nicknameValue: $('#nickname').val(),
            passwordValue: $('#password').val(),
        },
        dataType: 'JSON',
        success: function (data) {
            console.log(data.result);
            if (data.result == "success") {
                location.reload([bForceGet = true])
            }
            else if (data.result == "Invalid_user") {
                $(".warning_li_user").show();
            }
            else {
                $(".warning_li_password").show();
            }
        }
    });
};


// setInterval("time.innerText=new Date().toLocaleString()", 1000)

var punchDay = function (descript, worktime) {
    var date = new Date()
    Y = date.getFullYear() + '-';
    M = (date.getMonth() + 1 < 10 ? '0' + (date.getMonth() + 1) : date.getMonth() + 1) + '-';
    D = date.getDate() + ' ';
    h = date.getHours() + ':';
    m = date.getMinutes();
    if (worktime > 0 && worktime <= 1) {
        $.ajax({
            url: "/punch",
            data: {
                descript: descript,
                time: Y + M + D + h + m,
                year: date.getFullYear(),
                month: date.getMonth() + 1,
                day: date.getDate(),
                hour: date.getHours(),
                worktime: worktime,
            },
            dataType: 'json',
            success: function (data) {
                console.log(data.result);
                if (data.result == "success") {
                    // $('.punch-main, .punch-head').css({
                        // "translation": "5s filter",
                        // "filter": "blur(2px) contrast(.8) brightness(.8)"
                    // });
                    //
                    // $('.punch-main button').attr("disabled","true");
                    //
                    // $('.punch-box').css("filter","blur(2px)");
                    location.reload([bForceGet = true]);

                }
            }
        });
    }
};


var customDay = function () {
    for (var i = 5; i <= 100; i++) {
        $('.custom').css("width", i + "%");
    }
}


// $(".a").mouseover(function () {
//     $(".a .punch-box").css("margin-top", "-2em");
// });
// $(".a").mouseout(function () {
//     $(".a .punch-box").css("margin-top", "0");
// });
// $(".b").mouseover(function () {
//     $(".b .punch-box").css("margin-top", "-2em");
// });
// $(".b").mouseout(function () {
//     $(".b .punch-box").css("margin-top", "0");
// });
// $(".c").mouseover(function () {
//     $(".c .punch-box").css("margin-top", "-2em");
// });
// $(".c").mouseout(function () {
//     $(".c .punch-box").css("margin-top", "0");
// });
// $(".d").mouseover(function () {
//     $(".d .punch-box").css("margin-top", "-2em");
// });
// $(".d").mouseout(function () {
//     $(".d .punch-box").css("margin-top", "0");
// });
