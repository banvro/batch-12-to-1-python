<?php

use Illuminate\Support\Facades\Route;

Route::get('/', function () {
    return view('welcome');
});

Route::get("/set_session", "App\Http\Controllers\learnsession@set_session");

Route::get("/get_session", "App\Http\Controllers\learnsession@get_session");

Route::get("/check_session", "App\Http\Controllers\learnsession@check_session");

Route::get("/delete_session", "App\Http\Controllers\learnsession@delete_session");