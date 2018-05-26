var update_eval_table = function (fen){
    $.ajax({
        url: "/rest/eval/read-table",
        type: "POST",
        data: JSON.stringify({fen : fen}),
        contentType: 'application/json',
        dataType: "json",
        success: function(response){
          //$("#eval-tbl > tr").slice(1).remove();
          $("#eval-tbl").find("tr:gt(0)").remove();
          //response = $.parseJSON(data);
          $.each(response, function(i, item) {
            var $tr = $('<tr>').append(
                $('<td>').text(item.score),
                $('<td>').text(item.moves),
                $('<td>').text(item.depth),
                $('<td>').text(item.engine)
            ).appendTo('#eval-tbl');
            //console.log($tr.wrap('<p>').html());
        });
        }
      });
};