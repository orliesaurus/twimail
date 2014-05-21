<?php

header('Content-type: text/xml');
echo '<?xml version="1.0" encoding="UTF-8"?>';
echo '<Response></Response>';
 
$to      = "orlando@opensauce.it";
$subject = "Message from {$_REQUEST['From']} at {$_REQUEST['To']}";
$message = "You have received a message from {$_REQUEST['From']}.
Body: {$_REQUEST['Body']}";
$headers = "From: sms2email@opensauce.it";
 
mail($to, $subject, $message, $headers);

?>
