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
alert(3);
        var service = new google.maps.places.PlacesService(map);
        alert(3);

        

        document.getElementById('facetrade').addEventListener('click', function() {
        calculateAndDisplayRoute(directionsService, directionsDisplay, geocoder, service, map);
        });
    
  }


function calculateAndDisplayRoute(directionsService,directionsDisplay,geocoder,service,map) {
    
    var address = document.getElementById('id_Address').value;


  
    geocoder.geocode({'address': address}, function(results, status) {
        
        if (status === google.maps.GeocoderStatus.OK) 
        {

            map.setCenter(results[0].geometry.location); 
            

            var marker = new google.maps.Marker({
            map: map,
            label: '您',
            position: results[0].geometry.location,
            animation: google.maps.Animation.BOUNCE
            });
            var callbackCount = 0;
            var Max = 0;
            var Response;

            service.nearbySearch({
                location: results[0].geometry.location,
                radius: 500,
                types: ['store']
              }, function(results2, status1) {

                if (status1 === google.maps.places.PlacesServiceStatus.OK) 
                {
              
                  for(var i=0;i<results2.length;i++)
                  {
                                       
                      var request = {
                          origin: results[0].geometry.location, 
                          destination: results2[i].geometry.location,
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

            });
            

          

            
          
        } 

        else {
            alert('Geocode was not successful for the following reason: ' + status);
        }
      

        
    });
}
