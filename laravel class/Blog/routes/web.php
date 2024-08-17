<?php

use Illuminate\Support\Facades\Route;

Route::get('/', function () {
    return view('welcome');
});


Route::view("/contact", "contactus");

Route::post("/saving-data", "App\Http\Controllers\ContactusController@savedata");