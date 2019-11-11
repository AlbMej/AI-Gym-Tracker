var table = document.getElementById("calendar");
if (table != null) {
    for (var i = 0; i < table.rows.length; i++) {
        for (var j = 0; j < table.rows[i].cells.length; j++)
        if(table.rows[i].cells[j].innerHTML=="")
        {
            table.rows[i].cells[j].onclick = function () {
            tableText(this);
            };
        }
        
    }
}

$("a").click(function(){
    tableText(this)
});

function tableText(tableCell) {
    $("#baslik").val(tableCell.id)
    $("#etkinlik").modal('show');  
};

$(function () {
    $('#timepicker-start').datetimepicker({
        format: 'HH:mm:ss'
    });
    $('#timepicker-end').datetimepicker({
        format: 'HH:mm:ss'
    });
    $('#datepicker').datetimepicker({
        format: 'YYYY-MM-DD'
    });
});