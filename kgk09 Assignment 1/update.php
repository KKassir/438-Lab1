<html>
<body>



<?php

	// set your infomation.
	$host		=	'localhost';
	$user		=	'root';
	$pass		=	'';	
	$database	=	'telephone';
	
	
	// connect to the mysql database server.
	$connect = @mysql_connect ( $host, $user, $pass ) ;
    $name= $_POST['contact_name'];
    $mobile= $_POST['contact_mobile_number'];
    $profession= $_POST['contact_profession'];
    $tel= $_POST['contact_tel_number'];

	if ( $connect )
	{
		mysql_select_db ( $database, $connect );

		$query="UPDATE `contacts` SET 
        `contact_mobile_number` = '$mobile', 
        `contact_profession` = '$profession', 
        `contact_tel_number` = '$tel'
        WHERE contact_name='" . $name . "'" ;

		
		if ( @mysql_query ( $query ) )
			{
				echo 'Record Updated Successfuly';
			}
			else {
				die ( mysql_error() );
			}	
	        
	}
	else {
		trigger_error ( mysql_error(), E_USER_ERROR );
	}

	

        
			
?>
</body>
</html>