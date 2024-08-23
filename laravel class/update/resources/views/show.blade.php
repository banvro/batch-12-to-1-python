@extends('base')

@section('mybody')

<div style="margin-top: 18px; margin-left: 5%; margin-right: 5%;">
    <div class="row">


        @foreach ($mydata as $item)
        <div class="col-sm-6 mb-3 mb-sm-0">
          <div class="card" style="margin-bottom: 10px;">
            <div class="card-body">
              <h5 class="card-title">{{$item->full_name}}</h5>
              <p class="card-text"><span style="font-width : 500">User Email : </span>{{$item->email}}</p>
              <p class="card-text"><span style="font-width : 500">User Phone Number : </span>{{$item->phone_number}}</p>
              <p class="card-text"><span style="font-width : 500">User Messsage : </span>{{$item->message}}</p>
            </div>

            <div style="display: flex; justify-content: space-around; margin-bottom: 5px;">

              <a href="/update-data/{{$item->id}}"><button type="button" class="btn btn-success">Update</button></a>
              
              <a href="/delete-data/{{$item->id}}"><button type="button" class="btn btn-danger">Delete</button></a>

            </div>



          </div>
        </div>
        @endforeach
      

      </div>
</div>

@endsection

