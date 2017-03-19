    function initialize1() {

        var map = new google.maps.Map(document.getElementById('mapa'), {
            zoom: 15,
            center: new google.maps.LatLng(-2.13657, -79.89571),
            mapTypeId: google.maps.MapTypeId.ROADMAP
        });

        function car () {

        $.ajax({
            url: "/transporte/listapar/1/",
            dataType: "json",
            type: "POST",
            success: function (data) {
                var puntos = data[0];
                var paradas = data[1];
                carro = data[2];
                var infowindow = new google.maps.InfoWindow();

                for (var j = 0; j < paradas.length; j++) {
                    marker = new google.maps.Marker({
                        position: new google.maps.LatLng(paradas[j]['latitud'], paradas[j]['longitud']),
                        map: map,
                        icon: src = "/static/images/parada.png"
                    });

                    google.maps.event.addListener(marker, 'click', (function (marker, j) {
                        return function () {
                            infowindow.setContent(paradas[j]['nombre']);
                            infowindow.open(map, marker);
                        }
                    })(marker, j));
                }

                for (var i = 0; i < carro.length; i++) {
                    
                    marker = new google.maps.Marker({
                        position: new google.maps.LatLng(carro[i]['lat_final'], carro[i]['long_final']),
                        map: map,
                        icon: src = "/static/images/iconcar.png"
                    });
                }
                //positionFinal(carro);

                for (var i = 0; i < puntos.length - 1; i++) {
                    var l1 = new google.maps.LatLng(puntos[i]['r_list']['rlat'], puntos[i]['r_list']['rlong']);
                    var l2 = new google.maps.LatLng(puntos[i + 1]['r_list']['rlat'], puntos[i + 1]['r_list']['rlong']);
                    var miRuta = [l1, l2];
                    var trazo = new google.maps.Polyline({
                        path: miRuta,
                        strokeColor: "#0000FF",
                        strokeOpacity: 0.8,
                        strokeWeight: 3
                    });
                    trazo.setMap(map);
                }

            }
        });
    }
        setInterval(car,4000);
    }

        /*function positionFinal(carro){
            for (var i = 0; i < carro.length; i++) {
                    marker = new google.maps.Marker({
                        position: new google.maps.LatLng(carro[i]['lat_final'], carro[i]['long_final']),
                        map: map,
                        icon:src="/static/images/iconcar.png"
                    });
                }
        }*/



/*        $.ajax({
            url:"/transporte/lparada/1/",
            dataType:"json",
            type: "POST",
            success: function(data){
                    var marcadores = data;

                      var infowindow = new google.maps.InfoWindow();

                     markerterminal = new google.maps.Marker({
                        position: new google.maps.LatLng( -2.14009, -79.8802),
                        map: map,
                        icon: src="/static/images/par.png",
                        tittle: "Terminal Rio Daule"
                    });

                    for (var i = 0; i < marcadores.length; i++) {
                    marker = new google.maps.Marker({
                      position: new google.maps.LatLng(marcadores[i]['latitud'], marcadores[i]['longitud']),
                      map: map,
                        icon:src="/static/images/parada.png"
                    });
                
                    google.maps.event.addListener(marker, 'click', (function(marker, i) {
                      return function() {
                        infowindow.setContent(marcadores[i]['nombre']);
                        infowindow.open(map, marker);
                      }
                    })(marker, i));
                  }
            }
        });

       $.ajax({
            url:"/transporte/lruta/1/",
            dataType:"json",
            type: "POST",
            success: function(data){
                    var puntos = data;
                for (var i = 0; i < puntos.length; i++) {
                    var l1 = new google.maps.LatLng(puntos[i]['latitud'], puntos[i]['longitud']);
                    var l2 = new google.maps.LatLng(puntos[i+1]['latitud'], puntos[i+1]['longitud']);
                    var miRuta = [l1, l2];
                    var trazo = new google.maps.Polyline({path:miRuta,strokeColor:"#0000FF",strokeOpacity:0.8,strokeWeight:3});
                    trazo.setMap(map);
                }
            }
        });

        function posicion_car() { 
            $.ajax({
            url:"/transporte/lcar/1/",
            dataType:"json",
            type: "POST",
            success: function(data){
                    var posicion = data;
                    var infowindow = new google.maps.InfoWindow();
                    var a = posicion.length;
                    var i = a-1;

                    marker.setMap(null);
                    marker = new google.maps.Marker({
                      position: new google.maps.LatLng(posicion[i]['latitud'], posicion[i]['longitud']),
                      map: map,
                      icon:src="/static/images/iconcar.png"
                    });
                }
            });
        }
            setInterval(posicion_car,4000);*/

    google.maps.event.addDomListener(window, 'load', initialize1);

