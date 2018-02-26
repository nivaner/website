/**
 * Created by yangzhiqiang on 2018/2/23.
 */

// 生成二维数组
var a = new Array();
for(var i=0;i<4;i++){
  a[i] = new Array();
  for(var j=0;j<4;j++){
    a[i][j] = 0;
  }
}

//随机选择队列
var b = [[0,0],[0,1],[0,2],[0,3],[1,0],[1,1],[1,2],[1,3],[2,0],[2,1],[2,2],
  [2,3],[3,0],[3,1],[3,2],[3,3]]

var change = 0;

var score = 0;

//初始化
init()

//刷新
function refresh(){
  window.location.reload();
}


$(document).keydown(function(event){
  switch(event.keyCode){
    case 65 : //left
      left(0);
      $('.score').text("");
      $('.score').append("score: " + score);
      break;
    case 87 : //up
      up(0);
      $('.score').text("");
      $('.score').append("score: " + score);
      break;
    case 68 : //right
      right(0);
      $('.score').text("");
      $('.score').append("score: " + score);
      break;
    case 83 : //down
      down(0);
      $('.score').text("");
      $('.score').append("score: " + score);
      break;
    default : //default
      break;
  }
});


function init(){
  showNumber();
  showNumber();
}


//向上
function up(judge) {
  change = 0;
  b = [];
  for(var i=0;i<4; i++){
    var ctrStack = [];
    //用于判断是否发生变化
    var tet = [];
    for(var j=0;j<4;j++){
      if(a[i][j] != 0 ){
        ctrStack.push(a[i][j]);
      }
      tet.push(a[i][j])
    }
    for(var m = 4; m > 0; m--){
      if(tet[m] == 0){
        tet.pop()
      }
    }
    if(ctrStack.length != 0 && (tet.toString() != ctrStack.toString()) ){
      change = 1
    }


    var res =  add(ctrStack).slice();
    if(judge != 1){
      for(var k=0;k<4;k++){
        if(k < res.length){
          a[i][k] = res[k];
          str = '.block-'+i+'-'+k;
          // console.log(str)
          $(str).text("");
          $(str).append(a[i][k]);
          $(str).removeClass().addClass('block block-'+i+'-'+k +" _"+a[i][k]);
        }else{
          a[i][k] = 0;
          str = '.block-'+i+'-'+k;
          $(str).text("").removeClass().addClass('block block-'+i+'-'+k);
          b.push([i,k]);
        }
      }
    }
  }
  if(judge == 1){
    return change==1 ? false : true;
  }else{
    if(change == 1){
      showNumber();
      if(b.length < 1){
        if(left(1) && right(1) && down(1) && up(1)){
          alert("游戏结束！ 总分： "+ score)
        }
      }
    }
  }
}

//向左
function left(judge) {
  change = 0
  b = [];
  for(var i=0;i<4; i++){
    var ctrStack = [];
    //用于判断是否发生变化
    var tet = [];
    for(var j=0;j<4;j++){
      if(a[j][i] != 0 ){
        ctrStack.push(a[j][i]);
      }
      tet.push(a[j][i])
    }
    for(var m = 4; m > 0; m--){
      if(tet[m] == 0){
        tet.pop()
      }
    }
    if(ctrStack.length != 0 && (tet.toString() != ctrStack.toString())){
      // console.log(tet.toString(), ctrStack.toString())
      change = 1
    }
    var res =  add(ctrStack).slice();

    if(judge != 1){
      for(var k=0;k<4;k++){
        if(k < res.length){
          a[k][i] = res[k];
          str = '.block-'+k+'-'+i;
          $(str).text("");
          $(str).append(a[k][i]);
          $(str).removeClass().addClass('block block-'+k+'-'+i +" _"+a[k][i]);
        }else{
          a[k][i] = 0;
          str = '.block-'+k+'-'+i;
          $(str).text("").removeClass().addClass('block block-'+k+'-'+i);;
          b.push([k,i]);
        }
      }
    }

  }
  if(judge == 1){
    return change==1 ? false : true;
  }else{
    if(change == 1){
      showNumber();
      if(b.length < 1){
        if(left(1) && right(1) && down(1) && up(1)){
          alert("游戏结束！ 总分： "+ score)
        }
      }
    }
  }

}

//向下
function down(judge){
  change = 0;
  b = [];
  for(var i=0;i<4; i++){
    var ctrStack = [];
    var tet = []
    for(var j=3;j>=0;j--){
      if(a[i][j] != 0 ){
        ctrStack.push(a[i][j]);
      }
      tet.push(a[i][j]);
    }
    var res =  add(ctrStack).slice();
    var len = 4 - res.length;
    for(var m = 0;m < len ; m++){
      res.push(0)
    }
    if((tet.toString() != res.toString()) ){
      change = 1
    }
    res.reverse()
    if(judge != 1){
      for(var k=0;k<4;k++){
        a[i][k] = res[k];
        str = '.block-'+i+'-'+k;
        $(str).text("").removeClass().addClass('block block-'+i+'-'+k);
        if(res[k] != 0){
          $(str).append(a[i][k]);
          $(str).addClass("_"+a[i][k]);
        }else{
          b.push([i,k])
        }
      }
    }
  }
  if(judge == 1){
    return change==1 ? false : true;
  }else {
    if(change == 1){
      showNumber();
      if(b.length < 1){
        if(left(1) && right(1) && down(1) && up(1)){
          alert("游戏结束！ 总分： "+ score)
        }
      }
    }
  }
}

//向右
function right(judge){
  change = 0;
  b = [];
  for(var i=0;i<4; i++){
    var ctrStack = [];
    var tet = []
    for(var j=3;j>=0;j--){
      if(a[j][i] != 0 ){
        ctrStack.push(a[j][i]);
      }
      tet.push(a[j][i]);
    }
    var res =  add(ctrStack).slice();
    var len = 4 - res.length;
    for(var m = 0;m < len ; m++){
      res.push(0)
    }
    if((tet.toString() != res.toString()) ){
      change = 1
    }
    res.reverse()
    if(judge != 1){
      for(var k=0;k<4;k++){
        a[k][i] = res[k];
        str = '.block-'+k+'-'+i;
        $(str).text("").removeClass().addClass('block block-'+k+'-'+i);
        if(res[k] != 0){
          $(str).append(a[k][i]);
          $(str).addClass("_"+a[k][i]);
        }else{
          b.push([k,i])
        }
      }
    }
  }
  if(judge == 1){
    return change==1 ? false : true;
  }else {
    if(change == 1){
      showNumber();
      if(b.length < 1){
        if(left(1) && up(1) && down(1) && right(1)){
          alert("游戏结束！ 总分： "+ score)
        }
      }
    }
  }
}

// 数字移动，叠加
function add(arr){
  var addResult = [];
  var j = 0;
  if(arr.length > 1){
    for(var i = 1; i<arr.length; i++){
      if(arr[i-1] == arr[i]){
        change = 1;
        addResult.push(arr[i]*2);
        score = score + arr[i] * 2;
        var j = i+1;
        // 下标为2，存在第3块与第4块相等情况,防止越界
        if(j<=arr.length-2){
          if(arr[j] == arr[j+1]){
            change = 1;
            addResult.push(arr[j] *2)
            score = score + arr[j] * 2;
          }else{
            addResult.push(arr[j]);
            addResult.push(arr[j+1]);
          }
        }else{
          if(j==arr.length-1){
            addResult.push(arr[j])
          }
        }
        break;
      }else{
        addResult.push(arr[i-1]);
        if(i == arr.length-1){
          addResult.push(arr[i]);
        }
      }
    }
  }else{
    return arr;
  }
  return addResult;
}


// 将位置与数组对接，并在页面显示文字
function showNumber(){
  var getPos = randomPosition();
  if(getPos == 0){
    return false;
  }else{
    a[getPos[0]][getPos[1]] = randomValue();
    str = '.block-'+getPos[0]+'-'+getPos[1];
    $(str).append(a[getPos[0]][getPos[1]])
    $(str).addClass("_"+a[getPos[0]][getPos[1]]);
    var index = getPos[2];
    b.splice(index,1);
    return true;
  }
}


//随机生成位置
function randomPosition(){
  if(b.length > 0){
    var index = Math.floor(Math.random()*b.length)
    b[index].push(index);
    return b[index];
  }else{
    return 0;
  }
}


// 随机生成2，4 值
function randomValue(){
  var values = [2,4];
  var item = values[Math.round(Math.random())];
  return item
}

