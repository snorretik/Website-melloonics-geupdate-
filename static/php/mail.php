<?php
// The message

$message = "Naam: ".$_POST["naam"]."\r\n"."Email: ".$_POST["emailAdress"]."\r\n"."Vraag: ".$_POST["vraag"]."\r\n";

// In case any of our lines are larger than 70 characters, we should use wordwrap()
$message = wordwrap($message, 70, "\r\n");

// Send
mail('info@melloonics.nl', "Vragen van melloonics.nl", $message);
?>

<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Email Page</title>
</head>
<body>
    <h1>U hebt uw vraag succesvol verstuurd!</h1>
</body>
</html>