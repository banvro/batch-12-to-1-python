<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use App\Models\contactus;

class ContactusController extends Controller
{
    function savedata(Request $request){
        $request->validate([
            "fname" => "required|min:5|max:10",
            "pnumber" => "required",
            "email" => "required|email",
            "msg" => "required"
        ]);

        $my_record = new contactus;
        // instance_name->columname = value from frontend
        $my_record->full_name = $request->input("fname");
        $my_record->email = $request->input("email");
        $my_record->phone_number = $request->input("pnumber");
        $my_record->message = $request->input("msg");
        $my_record->save();
        
        return redirect("/show-data");

    }


    function showdata(){
        return view("show")->with("mydata", contactus::all());
    }

    function deletedata($myid){
        // echo $myid;
        contactus::destroy($myid);
        return redirect("/show-data");
    }
}