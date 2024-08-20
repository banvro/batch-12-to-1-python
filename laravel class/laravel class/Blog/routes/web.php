<?php

use Illuminate\Support\Facades\Route;

Route::get('/', function () {
    return view('welcome');
});


Route::view("/contact", "contactus");

Route::post("/saving-data", "App\Http\Controllers\ContactusController@savedata");


Route::get("/show-data", "App\Http\Controllers\ContactusController@showdata");