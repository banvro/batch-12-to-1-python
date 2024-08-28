<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;

class learnsession extends Controller
{
    function set_session(Request $r){
        // session()
        // put()---> help to set session 
        $r->session()->put("username", "kriss moris");
    }

    function get_session(Request $r){
        $my_data = $r->session()->get("username");
        echo $my_data;
    }

    function check_session(Request $r){
        if ($r->session()->has("username")){
            echo "User login";
        }else{
            echo "User not login";
        }
    }

    function delete_session(Request $r){
        $r->session()->remove("username");
    }
}



// session() --> to manage sessions 
    // put() ----> help to set session 
    // get() ----> help to get session
    // has() ----> help to check session
    // remove() ---> to remove session