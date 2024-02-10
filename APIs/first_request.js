const request = require('request');

request('http://127.0.0.1:8000/api/trucks/', function(error, response, body) {
    if(error) {
        console.log("Something went wrong!");
        console.log(error);
    } else {
        if (response.statusCode === 200) {
            const trucksData = JSON.parse(body); // Parse the JSON response
            const truckList = trucksData.all_trucks.map(truck => ({
                id: truck.id,
                cab_plate: truck.cab_plate,
                driver: truck.driver
            }));
            console.log(truckList);
        }
    }
});
