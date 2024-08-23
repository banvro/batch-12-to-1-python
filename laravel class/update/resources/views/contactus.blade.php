@extends('base')

@section('mybody')
    <div style="padding-top: 2%; padding-left: 14%; padding-right: 14%;">
        <h1 style="text-align: center; color: red;">Contact Us</h1>

        <form action="/saving-data" method="post">
            @csrf
            <div class="mb-3">
              <label for="exampleInputEmail1" class="form-label">Full Name</label>
              <input type="text" name="fname" class="form-control" placeholder="Enter your name">
              @error('fname')
                  <span style="color: red">{{$message}}</span>
              @enderror
            </div>

            <div class="mb-3">
              <label for="exampleInputPassword1" class="form-label">Phone Number</label>
              <input type="tel" name="pnumber" class="form-control" placeholder="enter your number">
              @error('pnumber')
                <span style="color: red">{{$message}}</span>
            @enderror
            </div>

            <div class="mb-3">
              <label for="exampleInputPassword1" class="form-label">Email Address</label>
              <input type="email" name="email" class="form-control" placeholder="enter your email address">
              @error('email')
                <span style="color: red">{{$message}}</span>
            @enderror
            </div>

            <div class="mb-3">
              <label for="exampleInputPassword1" class="form-label">Message</label>
              <textarea type="text" name="msg" class="form-control" placeholder="enter your message here"></textarea>
              @error('msg')
                <span style="color: red">{{$message}}</span>
            @enderror
            </div>
           
            <div style="text-align: center;">
                <button type="submit" class="btn btn-primary">Submit</button>
            </div>
          </form>
    </div>
@endsection