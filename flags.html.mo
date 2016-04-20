<!DOCTYPE html>
<html>
  <head>
    <meta charset="UTF-8">
    <title>Flags of the World</title>
    <style>
    @media print {
      div{
        page-break-inside: avoid;
      }
    }
    .flag_holder {
        border: 2px solid black;
        padding: 5px;
        float: left;
        margin: 10px;
        width: 200px;
        height: 200px;
    }
    .flag_svg {
        width: 200px;
        height: 150px;
    }
    .flag_name {
        font-size: 16px;
        text-align: center;
        font-family: Helvetica, Sans-Serif;
        word-wrap: break-word;
        margin-top: 0px;
        margin-bottom: 0px;
        width: 95%;
    }
    p {
        margin-top: 0px;
        margin-bottom: 0px;
    }
    h1 {
        font-family: Helvetica, Sans-Serif;
        text-align: center;
    }
    </style>
  </head>
  <body>
      <h1>Sovereign State Flags</h1>
  {{#flag_list}}
    <div class="flag_holder">
       <img class="flag_svg" src="{{url}}">
       <div class="flag_name"><p>{{name}}</p></div>
    </div>
  {{/flag_list}}
  </body>
</html>
