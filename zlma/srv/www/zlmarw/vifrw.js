/* vifrw.js - Make HMTL tables editable, using Bootstrap - original author Tito Hinostroza */
"use strict";
var params = null;  		//Parameters
var colsEdi =null;
var newColHtml = '<div class="btn-group pull-right">'+
'<button id="bEdit" type="button" class="btn btn-sm btn-default" onclick="butRowEdit(this);">' +
'<span class="glyphicon glyphicon-pencil" > </span>'+
'</button>'+
'<button id="bAcep" type="button" class="btn btn-sm btn-default" style="display:none;" onclick="butRowAcep(this);">' + 
'<span class="glyphicon glyphicon-ok" > </span>'+
'</button>'+
'<button id="bCanc" type="button" class="btn btn-sm btn-default" style="display:none;" onclick="butRowCancel(this);">' + 
'<span class="glyphicon glyphicon-remove" > </span>'+
'</button>'+
  '</div>';

var colEdicHtml = '<td name="buttons">'+newColHtml+'</td>'; 
$.fn.SetEditable = function (options) {
  var defaults = {
      columnsEd: null,                     // Index to editable columns. If null all td editables. Ex.: "1,2,3,4,5"
      $addButton: null                     // Jquery object of "Add" button
  };
  params = $.extend(defaults, options);
  var $tabedi = this;          //Read reference to current table
  $tabedi.find('thead tr').append('<th name="buttons"></th>');  //Add empty column
  $tabedi.find('tbody tr').append(colEdicHtml); //Add column for buttons to all rows.
  if (params.$addButton != null) { //Process "addButton" parameter
      params.$addButton.click(function() {
          rowAddNew($tabedi.attr("id"));
      });
  }
  if (params.columnsEd != null) {            // process columnsEd
      colsEdi = params.columnsEd.split(','); // extract fields
  }
};

function getLocalWebserverURL() {
  const protocol = window.location.protocol;
  const hostname = window.location.hostname;
  const port = window.location.port;
  let url = `${protocol}//${hostname}`;
  if (port !== "") {
    url += `:${port}`;
  }
  return url;
}

async function onEdit(fields) {
  const username = 'root';
  const password = 'pi';
  const credentials = btoa(`${username}:${password}`);

  // Split fields: fields = &hostname&cpus&memory&created&app&env&group
  const parts = fields.split('&').map(decodeURIComponent);
  if (parts.length < 3) {
    console.error("Not enough fields to update CPUs and Memory");
    return;
  }

  const hostName = parts[1];    // part[0] is empty string due to initial &
  const cpus     = parts[2];
  const memory   = parts[3];

  // Construct URL - update endpoint for this host
  const baseURL = getLocalWebserverURL();
  const url = `${baseURL}/zlmarw/api/v1/machine/${hostName}`;

  const requestBody = {
    cpus: cpus,
    memory: memory
  };

  try {
    const response = await fetch(url, {
      method: "PUT",                      // use PUT for updating existing resource
      headers: {
        "Authorization": `Basic ${credentials}`,
        "Content-Type": "application/json"
      },
      body: JSON.stringify(requestBody)
    });

    if (!response.ok) {
      throw new Error(`Failed to update ${hostName}: ${response.status} ${response.statusText}`);
    }

    const result = await response.json();
    console.log("Update result:", result);
    return result;
  }
  catch (error) {
    console.error("ERROR: Failed to update host:", error);
    throw error;
  }
}

function iterateColumns($cols, action) {   // iterate through editable fields 
  var n = 0;
  $cols.each(function() {
      n++;
      if ($(this).attr('name')=='buttons') return;  //Exclude buttons column
      if (!IsEditable(n-1)) return;        // not editable
      action($(this));
  });
}
  
function IsEditable(idx) {                 // check if column is editable
      if (colsEdi==null) {                 // not editable
          return true;  
      } else {  
          for (var i = 0; i < colsEdi.length; i++) {
            if (idx == colsEdi[i]) return true;
          }
          return false;  
      }
  }
}

function ModoEdicion($row) {
  if ($row.attr('id')=='editing') {
      return true;
  } else {
      return false;
  }
}

function SetButtonsNormal(but) {           // set button state to normal
  $(but).parent().find('#bAcep').hide();
  $(but).parent().find('#bCanc').hide();
  $(but).parent().find('#bEdit').show();
  var $row = $(but).parents('tr'); 
  $row.attr('id', '');  //quita marca
}

function SetButtonsEdit(but) {             // set button state to editing
  $(but).parent().find('#bAcep').show();
  $(but).parent().find('#bCanc').show();
  $(but).parent().find('#bEdit').hide();
  var $row = $(but).parents('tr'); 
  $row.attr('id', 'editing'); 
}

function butRowAcep(but) {                 // have any columns been changed 
  // construct a uu-encoded QUERY_STRING of the form "host_name&value1&value2&value3"
  var $row = $(but).parents('tr');         // access the queue
  var $cols = $row.find('td');  
  if (!ModoEdicion($row)) return;          // currently being edited
  var col0 = $cols.eq(0).get(0)
  var hostName = col0.innerText;
  console.log("hostName: ", hostName); 
  var fields = "&"+hostName                // host name is first param 
  iterateColumns($cols, function($td) { 
    var value = $td.find('input').val();   // read content of input
    var safeValue = encodeURIComponent(value) // uu-encode so URL is safe 
    $td.html(value);                       // replace new content and remove controls
    fields = fields+'&'+safeValue;         // append safe value with a preceding '&'
    });
  console.log("fields: ", fields);
  SetButtonsNormal(but);
  onEdit(fields);                          // update the database
}

function butRowCancel(but) {               // cancel any changes              
  var $row = $(but).parents('tr');         // access the row
  var $cols = $row.find('td');             // read fields
  if (!ModoEdicion($row)) return;          // already being edited
  iterateColumns($cols, function($td) { 
    var cont = $td.find('div').html(); 
    $td.html(cont);  
  });
  SetButtonsNormal(but);
}

function butRowEdit(but) {                 // editing row
  var $row = $(but).parents('tr');         // access the row
  var $cols = $row.find('td');             // read fields
  if (ModoEdicion($row)) return;           // already being edited
  var focused = false;
  iterateColumns($cols, function($td) {  
      var cont = $td.html(); 
      var div  = '<div style="display: none;">' + cont + '</div>';  // save previous content in a hidden <div>
      var input= '<input class="form-control input-sm"  value="' + cont + '">';
      $td.html(div + input);               // set new content
      if (!focused) {                      // set focus to first column
        $td.find('input').focus();
        focused = true;
      }
  });
  SetButtonsEdit(but);
}

