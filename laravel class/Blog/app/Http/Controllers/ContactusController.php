<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;

class ContactusController extends Controller
{
    function savedata(Request $request){
        $request->validate([
            "fname" => "required|min:5|max:10",
            "pnumber" => "required",
            "email" => "required|email",
            "msg" => "required"
        ]);

        echo "vaidaitoon doneee";
    }
}
