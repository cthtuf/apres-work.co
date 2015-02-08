<?php
    $emailto = "sergey@summerneverends.ru"; /* YOUR EMAIL GOES HERE */
    $subject = "SNE Website Contact"; /* SUBJECT GOES HERE */

    $name = $_POST["name"];
    $phone = $_POST["phone"];
    $message = $name." wants to trip with us! His or her phone: ".$phone;

    $headers   = array();
    $headers[] = "MIME-Version: 1.0";
    $headers[] = "Content-type: text/plain; charset=iso-8859-1";
    $headers[] = "From: SNE Website <no-reply@summerneverends.ru>";
    $headers[] = "Subject: ".$subject;
    $headers[] = "X-Mailer: PHP/".phpversion();

    $message_info = mail( $emailto, $subject, $message, implode( "\r\n",$headers ) );

    if( $message_info === true ){
    	$rpo = (object) array('result' => 0);
    }
    else{
    	$rpo = (object) array('result' => 1);	
    }
	echo json_encode($rpo);
?>