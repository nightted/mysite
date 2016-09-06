function initMap() {

        var directionsService = new google.maps.DirectionsService;
        var directionsDisplay = new google.maps.DirectionsRenderer;
        var geocoder = new google.maps.Geocoder();
        var infowindow = new google.maps.InfoWindow();
        var map = new google.maps.Map(document.getElementById('map'), {
        zoom: 14,
        center: {lat: 24.801957, lng:120.971401}
        });
        directionsDisplay.setMap(map);
        

        marker0 = new google.maps.Marker({
            map: map,
            label: 'A',
            animation: google.maps.Animation.DROP,
            position: {lat: 24.804088, lng: 120.973116}
        });
        marker1 = new google.maps.Marker({
            map: map,
            label: 'B',
            animation: google.maps.Animation.DROP,
            position: {lat: 24.804482, lng: 120.965304}
        });
        marker2 = new google.maps.Marker({
            map: map,
            label: 'C',
            animation: google.maps.Animation.DROP,
            position: {lat: 24.807731, lng: 120.961097}
        });
        marker3 = new google.maps.Marker({
            map: map,
            label: 'D',
            animation: google.maps.Animation.DROP,
            position: {lat: 24.804887, lng: 120.964102}
        });
        marker4 = new google.maps.Marker({
            map: map,
            label: 'E',
            animation: google.maps.Animation.DROP,
            position: {lat: 24.806825, lng: 120.968512}
        });   
        mkr = [marker0,marker1,marker2,marker3,marker4]

        
        $("#id_Catchlocation").on("change", function() {
            
            for(var i=0;i<mkr.length;i++)
                {mkr[i].setAnimation(null);}

            var loc = $("#id_Catchlocation").val()       
            
            if(loc=='新竹聖教會')
            {
                marker0.setAnimation(google.maps.Animation.BOUNCE);                  
            }
            if(loc=='城隍廟')
            {
                marker1.setAnimation(google.maps.Animation.BOUNCE);
            }
            if(loc=='棒球場')
            {
                marker2.setAnimation(google.maps.Animation.BOUNCE);
            }
            if(loc=='江山藝改所')
            {
                marker3.setAnimation(google.maps.Animation.BOUNCE);
            }
            if(loc=='新竹市政府')
            {
                marker4.setAnimation(google.maps.Animation.BOUNCE);
            }
        });


        

        document.getElementById('facetrade').addEventListener('click', function() {
        calculateAndDisplayRoute(directionsService, directionsDisplay, geocoder, map);
        });
    
    }


function calculateAndDisplayRoute(directionsService,directionsDisplay,geocoder,map) {
    
    var address = document.getElementById('id_Address').value;


  
    geocoder.geocode({'address': address}, function(results, status) {
        
        if (status === google.maps.GeocoderStatus.OK) {

            map.setCenter(results[0].geometry.location); 
            

            var marker = new google.maps.Marker({
            map: map,
            label: '您',
            position: results[0].geometry.location,
            animation: google.maps.Animation.BOUNCE
            });
            

            var latlng0 = new google.maps.LatLng(24.804088, 120.973116);
            var latlng1 = new google.maps.LatLng(24.804482,120.965304);
            var latlng2 = new google.maps.LatLng(24.807731, 120.961097);
            var latlng3 = new google.maps.LatLng(24.804887, 120.964102);
            var latlng4 = new google.maps.LatLng(24.806825, 120.968512);
            var facetrade = [latlng0,latlng1,latlng2,latlng3,latlng4];
            
            var callbackCount = 0;
            var Max = 0;
            var Response;
            
            
            for(var i=0;i<facetrade.length;i++)
            {
                                 
                var request = {
                    origin: results[0].geometry.location, 
                    destination: facetrade[i],
                    travelMode: google.maps.TravelMode.DRIVING
                }
                
                directionsService.route(request, function(response, status) {
                /*這邊要注意到,google api的callback是async(非同步執行)的,
                也就是說他會跑完所有request,response之後才會執行callback,
                (也就是外迴圈會跑到i=最後一個,才執行cb loop),這也是為什麼
                function裡要加額外標記參數callbackcount來幫忙作判別!!!*/   

                    var distance = 0;

                    if (status === google.maps.DirectionsStatus.OK) {
                        var route = response.routes[0];

                        for (var j=0;j<route.legs.length; j++)
                        {
                            distance += route.legs[j].distance.value;
                        }

                        var dist = parseFloat(distance/1000);

                        if (callbackCount == 0)
                        {
                            Max = dist;
                        }

                        if (dist <= Max )
                        {
                            Max = dist;
                            Response = response;                             
                        }

                        /*alert(callbackCount);*/

                        if (callbackCount==(facetrade.length-1))
                        {
                            document.getElementById('distance').innerHTML = '距離您:'+Max+'公里!';
                            directionsDisplay.setDirections(Response);
                            
                        }                           
                        

                        /*document.getElementById('distance').innerHTML = dist*/ ;

                        /*directionsDisplay.setDirections(response);*/
                    } 

                    else {
                      window.alert('Directions request failed due to ' + status);
                    }

                    callbackCount++;

                });

            }

        } 

        else {
            alert('Geocode was not successful for the following reason: ' + status);
        }

    });
}