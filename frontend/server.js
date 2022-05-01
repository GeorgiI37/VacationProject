// load the things we need
var express = require('express');
var app = express();
var { BACKEND_API_URL} = require('./config/config');
const bodyParser  = require('body-parser');

// required module to make calls to a REST API
const axios = require('axios');
const { redirect } = require('express/lib/response');

app.use(bodyParser.urlencoded());

// set the view engine to ejs
app.set('view engine', 'ejs');

// root page to await login
app.get('/', function(req, res) {
    res.render('pages/index', {});
});

// login post
app.post('/process', function(req, res) {
    var user = req.body.username;
    var pass = req.body.password;
    if(user == 'admin' && pass == 'password'){
        res.render('pages/dashboard', {});
    }
});

//trips route
var go_trips = function(req, res)
{
    axios.get(BACKEND_API_URL + '/trips').then((response)=>{
        var tripres = response.data;
        res.render('pages/trips/index', {
            tripres: tripres
        });
    });
}

app.get('/trips', go_trips);

var toString = function(param)
{
    var date = new Date(param);
    return date.getFullYear() + '-' + parseInt((date.getMonth() + 1) / 10) + '' + parseInt((date.getMonth() + 1) % 10) + '-' + parseInt(date.getDate() / 10) + '' + parseInt(date.getDate() % 10); 
}

app.get('/trips/edit', function(req, res){
    console.log("trips/edit: " + req.query.trip_id);
    axios.get(BACKEND_API_URL + '/trips/' + req.query.trip_id).then((response)=>{
        var tripres = response.data;
        tripres[0].startdate = toString(tripres[0].startdate);
        tripres[0].enddate = toString(tripres[0].enddate);
        axios.get(BACKEND_API_URL + '/destinations').then((response)=>{
            var destinationres = response.data;
            res.render('pages/trips/edit_trips', {
                flag: true,
                tripres: tripres[0],
                destinationres: destinationres
            });
        });
    });
});

app.post('/trips/update', function(req, res){
    console.log("trips/update: " + req.body.trip_id);
    axios.post(BACKEND_API_URL + '/trips/update', {
        trip_id: req.body.trip_id,
        destination_id: req.body.destination_id,
        transportation: req.body.transportation,
        startdate: req.body.startdate,
        enddate: req.body.enddate,
        tripname: req.body.tripname,
    }).then((response)=>{
        res.redirect('/trips');
    });
});

app.get('/trips/create', function(req, res){
    axios.get(BACKEND_API_URL + '/destinations').then((response)=>{
        var destinationres = response.data;
        res.render('pages/trips/edit_trips', {
            flag: false,
            destinationres: destinationres
        });
    });
});

app.post('/trips/create', function(req, res){
    console.log("trips/create");
    axios.post(BACKEND_API_URL + '/trips/create', {
        destination_id: req.body.destination_id,
        transportation: req.body.transportation,
        startdate: req.body.startdate,
        enddate: req.body.enddate,
        tripname: req.body.tripname,
    }).then((response)=>{
        res.redirect('/trips');
    });
});

app.get('/trips/delete', function(req, res){
    console.log("trips/delete: " + req.query.trip_id);
    axios.get(BACKEND_API_URL + '/trips/delete/' + req.query.trip_id).then((response)=>{
        res.redirect('/trips');
    });
});

//destination route
var go_destinations = function(req, res)
{
    axios.get(BACKEND_API_URL + '/destinations').then((response)=>{
        var destinationres = response.data;
        res.render('pages/destinations', {
            destinationres: destinationres
        });
    });
}

app.get('/destinations', go_destinations);

app.get('/destinations/edit', function(req, res){
    axios.get(BACKEND_API_URL + '/destinations/' + req.query.destination_id).then((response)=>{
        var destinationres = response.data;
        res.render('pages/destinations/edit_destinations', {
            flag: true,
            destinationres: destinationres[0]
        });
    });
});

app.post('/destinations/update', function(req, res){
    axios.post(BACKEND_API_URL + '/destinations/update', {
        destination_id: req.body.destination_id,
        country: req.body.country,
        city: req.body.city,
        sightseeing: req.body.sightseeing,
    }).then((response)=>{
        res.redirect('/destinations');
    });
});

app.get('/destinations/create', function(req, res){
    res.render('pages/destinations/edit_destinations', {
        flag: false
    });
});

app.post('/destinations/create', function(req, res){
    axios.post(BACKEND_API_URL + '/destinations/create', {
        country: req.body.country,
        city: req.body.city,
        sightseeing: req.body.sightseeing,
    }).then((response)=>{
        res.redirect('/destinations');
    });
});

app.get('/destinations/delete', function(req, res){
    axios.get(BACKEND_API_URL + '/destinations/delete/' + req.query.destination_id).then((response)=>{
        res.redirect('/destinations');
    });
});

app.listen(8080);
console.log('8080 is the magic port');
