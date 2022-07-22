function validate(){
    var name = document.forms["Form"]["name"].value;
    var email = document.forms["Form"]["email"].value;
    var city = document.forms["Form"]["city"].value;
    var address = document.forms["Form"]["address"].value;
    var street = document.forms["Form"]["street"].value;
    var wardno = document.forms["Form"]["wardno"].value;
    var zipcode = document.forms["Form"]["zipcode"].value;

    if (name == "" || email == "" || city == "" || address == "" || street == "" || wardno == "" || zipcode == "") {
        console.log("false")
        document.getElementById('msgChk').classList.remove('d-none')
    }
    else{
        console.log("true")
        document.getElementById('make-payment').classList.add('d-none')
}
}

// function getPmValue(){
//     let paymentMethod = document.getElementById('pm')
//     switch(paymentMethod.value) {
//         case "Khalti":
//             document.getElementById('make-payment').classList.add('d-none')
//             document.getElementById('payment-buttonKhalti').classList.remove('d-none')    
            
//             break;
//         case "Cash on Delivery":
//             document.getElementById('make-payment').classList.remove('d-none')
//             document.getElementById('payment-buttonKhalti').classList.add('d-none')
//             break;
//     }
// }


