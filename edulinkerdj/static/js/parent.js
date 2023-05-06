// function createPost() {
//     var form = document.getElementById("post-form");
//     var postContent = document.getElementsByName('postcontent');
//     if(postContent == '')
//         alert("Content cannot be empty");
//     else
//         form.submit();
// }

function roll()
{
    var roll = document.getElementById("roll_num").value;
    var regex = /^[A-N]{1}[AB]{1}[0-9]{3}$/g;
    if(!roll.match(regex))
    {
        alert("Enter a valid Roll Number!");

    }
}

function phno()
{
    var phno = document.getElementById("ph_num").value;
    var reg = "^[0-9]{10}$";
    if(!phno.match(reg))
    {
        alert("Enter a valid Phone Number");
    }


}

// function hello() {
//     console.log("hello");
// }
function pswdLenCheck()
{
    var pswd = document.getElementById("pswd").value;
    console.log(pswd.length)
    if(pswd.length<8)
    {
        alert("Enter a strong password!");
    }
}

function c_pswd()
{
    var c_pswd= document.getElementById("conf_pswd").value;
    var pswd = document.getElementById("pswd").value;
    
    if(pswd!=c_pswd)
    {
        alert("Password does not match!");
    }
}

function submitLeave()
{
    var rollNum = document.getElementById("roll_number").value;
    var regex=/^[A-N]{1}[AB]{1}\d{3}$/g;
    if(rollNum.match(regex))
        alert("Leave Applied Successfully!")
    else
            alert("Invalid Roll Number!Cannot apply leave")
    
    //Check the pair of pid and rollNum matches with the pair in the DB //


}
