<!DOCTYPE html>
<html>
  <head>
    <meta charset="UTF-8">
    <title>Flags of the World</title>
    <style>
    .flag_holder {
        border: 2px solid black;
        height: 200px;
        padding: 10px;
        float: left;
        margin: 10px;

    }
    .flag_svg {
        width: 200px;
        height: 150px;
    }
    .flag_name {
        font-size: 16px;
        width: 200px;
        text-align: center;
        font-family: Helvetica, Arial, Sans-Serif;
        word-wrap: break-word;
    }
    </style>
  </head>
  <body>
  {{#flag_list}}
    <div class="flag_holder">
       <img class="flag_svg" src="{{url}}">
       <div class="flag_name"><p>{{name}}</p></div>
    </div>
  {{/flag_list}}
  </body>
</html>
