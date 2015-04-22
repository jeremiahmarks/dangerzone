// function myFunction() {
//     document.getElementById("demo").innerHTML = "Hello World";
// }

function myFunction()
{
    $.ajax({
        url: "./presets.php",
        type: "POST",
        data: { 'preset': '1' },
        success: function(data)
        {
            alert(data);
        }
    });
}
