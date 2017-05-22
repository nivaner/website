/**
 * Created by yangzhiqiang on 2017/4/28.
 */
/**
 * Created by yangzhiqiang on 2017/4/24.
 */

var width = 550;
var height = 550;
var padding = {top: 30, right: 30, bottom: 30, left: 30};


var showDate = function () {
    $.ajax({
            url: "/getuserdata",
            async: true,
            dataType: 'json',
            success: function (data) {
                console.log(data.result);
                jsondata = data.result;


                console.log(jsondata);
                console.log(jsondata.length);

                //判断数组里面是否有数据，有则以扇形图的样式显示
                //判断当天是否已经打卡，如果当天有记录，用户只能补签和修改
                if (jsondata.length > 0) {
                    for (var i = jsondata.length; i > 0; i--) {
                        console.log("在这里");
                        var date = new Date();
                        D = date.getDate();
                        console.log("日期：" + D);
                        console.log(jsondata[i-1][0]);
                        if (D == jsondata[i-1][0]) {
                            console.log("有没有进入这里")
                            $('.punch-main, .punch-head').css({
                                "filter": "blur(2px) contrast(.8) brightness(.8)"
                            });
                            $('.punch-main button').attr("disabled", "true");
                            $('.punch-dialog').show();
                            break;
                        }

                    }

                    //添加svg
                    var svg_two = d3.select(".chart_two")
                        .append("svg")
                        .attr("width", width)
                        .attr("height", height);

                    //数据库展示
                    var pie = d3.layout.pie()
                        // .sort(null)
                            .value(function (d) {
                                console.log(d[1]);
                                return d[1];
                            })
                        ;

                    var piedata = pie(jsondata);

                    var outerRadius = width / 3;
                    var innerRadius = 20;

                    var arc = d3.svg.arc()
                        .innerRadius(innerRadius)
                        .outerRadius(outerRadius);

                    var color = d3.scale.category20();


                    var arcs_two = svg_two.selectAll("g")
                        .data(piedata)
                        .enter()
                        .append("g")
                        .attr("transform",
                            "translate(" + (width / 2) + "," + (height / 2) + ")");

                    arcs_two.append("path")
                        .attr("fill", function (d, i) {
                            return color(i);
                        })
                        .attr("d", function (d) {
                            return arc(d);
                        });


                    arcs_two.append("text")
                        .attr("transform", function (d) {
                            var x = arc.centroid(d)[0] * 1.4;
                            var y = arc.centroid(d)[1] * 1.4;
                            return "translate(" + x + "," + y + ")";
                        })
                        .attr("text-anchor", "middle")
                        .text(function (d, i) {
                            // console.log(d);
                            // console.log(data[0]);
                            // console.log(jsondata[i][0]);
                            return jsondata[i][0] + "号";
                        });

                    arcs_two.append("text")
                        .attr("transform", function (d) {
                            var x = arc.centroid(d)[0] * 2.4;
                            var y = arc.centroid(d)[1] * 2.4;
                            return "translate(" + x + "," + y + ")";
                        })
                        .attr("text-anchor", "middle")
                        .text(function (d, i) {
                            return jsondata[i][1] + '天';
                        });

                    arcs_two.append("text")
                    // .attr("dy",".35em")
                        .attr("text-anchor", "middle")
                        .text(function (d) {
                            return jsondata[0][4] + "月";
                        });

                }
                //没有，则给用户提示
                else {
                    $(".none-jsondata").show();
                }


            }
        }
    )
    ;
}

showDate();


var showMonthDate = function () {
    $.ajax({
        url: "/getusermonthdata",
        async: true,
        dataType: 'json',
        success: function (data) {
            console.log(data.result);
            monthdata = data.result;
            if (monthdata.length > 0) {

                var svg_one = d3.select(".chart_one")
                    .append("svg")
                    .attr("width", width)
                    .attr("height", height);

                var pie = d3.layout.pie()
                        .value(function (d) {
                            console.log(d[1]);
                            return d[1];
                        })
                    ;

                var piedata = pie(monthdata);

                var outerRadius = width / 3;
                var innerRadius = 20;

                var arc = d3.svg.arc()
                    .innerRadius(innerRadius)
                    .outerRadius(outerRadius);

                var color = d3.scale.category20();


                var arcs = svg_one.selectAll("g")
                    .data(piedata)
                    .enter()
                    .append("g")
                    .attr("transform",
                        "translate(" + (width / 2) + "," + (height / 2) + ")");

                // 添加提示框
                // var tip = d3.tip()
                //     .attr('class', 'd3-tip')
                //     .offset([0,0])
                //     .html(function (d,i) {
                //         console.log(d);
                //         console.log(d[i]);
                //         return 'hello' + ": <span style='color:orangered'>" + 'world' + "</span>";
                //     });


                arcs.append("path")
                    .attr("fill", function (d, i) {
                        return color(i);
                    })
                    .attr("d", function (d) {
                        return arc(d);
                    })
                // .on('mouseover', tip.show())
                // .on('mouseout',tip.hide());


                arcs.append("text")
                    .attr("transform", function (d) {
                        var x = arc.centroid(d)[0] * 1.2;
                        var y = arc.centroid(d)[1] * 1.2;
                        return "translate(" + x + "," + y + ")";
                    })
                    .attr("text-anchor", "middle")
                    .text(function (d, i) {
                        console.log(d);
                        console.log(data[0]);
                        console.log(monthdata[i][0]);
                        return monthdata[i][0] + "月";
                    });
                //
                // arcs.append("line")
                //     .attr("stroke", "blank")
                //     .attr("x1", function (d) {
                //         return arc.centroid(d)[0] * 2;
                //     })
                //     .attr("y1", function (d) {
                //         return arc.centroid(d)[1] * 2;
                //     })
                //     .attr("x2", function (d) {
                //         return arc.centroid(d)[0] * 2.2;
                //     })
                //     .attr("x2", function (d) {
                //         return arc.centroid(d)[1] * 2.2;
                //     });
                //
                arcs.append("text")
                    .attr("transform", function (d) {
                        var x = arc.centroid(d)[0] * 2.2;
                        var y = arc.centroid(d)[1] * 2.2;
                        return "translate(" + x + "," + y + ")";
                    })
                    .attr("text-anchor", "middle")
                    .text(function (d, i) {
                        return monthdata[i][1] + "天";
                    });

                arcs.append("text")
                    .attr("dy", ".35em")
                    .attr("text-anchor", "middle")
                    .text(function (d) {
                        return "2017年";
                    });
            }
            else {
                $(".none-monthdata").show();
            }
        }
    });
}

showMonthDate();
// d3.json("/getuserdata", function (error, data) {
//
//     dataset = console.log(data);
//
//
//     var center = [[0.5, 0.5], [0.7, 0.8], [0.4, 0.9],
//         [0.11, 0.32], [0.88, 0.25], [0.75, 0.12],
//         [0.5, 0.1], [0.4, 0.1], [0.6, 0.7]];
//
//     console.log(center.length);
//     var pie = d3.layout.pie()
//         .value(function (d) {
//             console.log(d[2]);
//             return d[2];
//         });
//
//     var piedata = pie(dataset);
//
//     console.log(piedata);
//
// })


// function output(json) {
//     var Data = eval(json);
//     var html = '';
//     for(var i=0;i<Data.length;i++){
//         //具体键值根据你返回的字符串来
//         html += '日期' + Data[i][0] + '时间' + Data[i][1] + '描述' + Data[i][2] + '名字' + Data[i][3];
//     }
//     //插入到元素
//     document.getElementById('el').innerHTML = html;
//
// }



