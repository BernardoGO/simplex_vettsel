function control( ) {


    var json = '{ "data": { "result": [ 0, 3.6923076923076925, 1.076923076923077, 0, 1.2307692307692306 ], "sens": [ [ 0.5714285714285714, 8 ], [ 0.25, 3.5 ] ], "status": "otima", "table": [ [ "vnb", "ml", 5, 3 ], [ "f", 8.461538461538462, -0.2692307692307692, -0.05769230769230768 ], [ 2, 3.6923076923076925, -0.15384615384615385, 0.038461538461538464 ], [ 1, 1.076923076923077, 0.03846153846153846, -0.1346153846153846 ], [ 4, 1.2307692307692306, 0.11538461538461539, 0.09615384615384615 ] ] } }';

  var myList = JSON.parse(json);


    $("#calcbutton").click(function(e) {
        e.preventDefault();
        sendData( );

    });

    $("#addCampo").click(function(e) {
        e.preventDefault();

        var $base = $("#campoBase").clone();
        $("#tabela").append($base);

    });

    $("#deleteCampo").click(function(e) {
        e.preventDefault();

        var count = $("#tabela input").length;

        if ( count > 1) {

            $("#tabela input:last").fadeOut().detach()
        }

    });


    function sendData() {

        //var formData = $('#login').serializeArray()
        //  .reduce(function(a, x) { a[x.name] = jQuery.parseJSON( x.value); return a; }, {});
        var $inputs = $('#tabela :input');
        jsow = "{ \"data\" : [";
        $inputs.each(function() {
            jsow += "[";
            jsow += $(this).val() ;
            jsow += "]";
        });
        jsow = jsow.replace(/\]\[/g, "],[");
        jsow += "] }";
        //jsow = "{ \"data\" : " + $('campo[name=tcol1]').attr('value') + "}"
        $('body').append($('<div>', {
           text: jsow
        }));
        var formData = jQuery.parseJSON(jsow);
        $.ajax({
            type: "POST",
            url: "http://ec2-35-160-139-230.us-west-2.compute.amazonaws.com/simplex",
            data: JSON.stringify(formData),
            success: function (data) {
                //$.each(data, function(index, element) {
                  //  $('body').append($('<div>', {
                    //    text: element.name
                    //}));
                //});
              myList = data;
            },
            dataType: "text",
            contentType : "application/json"
        });
    }







    function buildHtmlTable(selector, data) {



        var row$ = $('<tr/>');
        for (var i = 0 ; i <  data.length; i++ ){
            row$.append($('<td/>').html(data[i] ));
        }

        $(selector).append(row$);
    }

    function buildHtmlTable2(selector, data) {


        for (var j = 0 ; j <  data[0].length; j++ ){
            var row$ = $('<tr/>');

            for (var i = 0 ; i <  data.length; i++ )
            {
                row$.append($('<td/>').html( data[j][i] ) );

            }

            $(selector).append(row$);

        }

    }



    function addAllColumnHeaders( selector, data ) {

        var headerTr$ = $('<tr/>');
        for ( var i= 0 ; i < data.length  ; i++) {
            headerTr$.append($('<th/>').html("x"+i ));
        }

        $(selector).append(headerTr$);
    }


    addAllColumnHeaders ( '#resultTable', myList.data.result);

    buildHtmlTable( '#resultTable', myList.data.result);

    buildHtmlTable2( '#simplexTable', myList.data.table);

    buildHtmlTable( '#statusTable', myList.data.status);

    buildHtmlTable2( '#sensTable', myList.data.sens);

    //buildHtmlTable( '#sensTable', myList.data.sens);







}
