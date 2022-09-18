<html>
<body>
Test3
<?php

	// set your infomation.
	$host		=	'localhost';
	$user		=	'root';
	$pass		=	'';	
	$database	=	'telephone';
	
	
	// connect to the mysql database server.
	$connect = @mysql_connect ( $host, $user, $pass ) ;

	if ( $connect )
	{
		mysql_select_db ( $database, $connect );
		$sql = "SELECT contact_name,contact_profession,contact_tel_number,contact_mobile_number FROM contacts";
		
		?>
		<table border ="1" cellspacing="0" cellpadding="10">
		<tr>
			<th>Name</th>
			<th>Profession</th>
			<th>Tel</th>
			<th>Mobile</th>

		</tr>
		<?php
		if ( @mysql_query ( $sql) )
		{
			$query = mysql_query ( $sql );

			$row = mysql_fetch_assoc ( $query );
			do {

				?>
				<tr>
				  <td><?php echo $row['contact_name']; ?> </td>
				  <td><?php echo $row['contact_profession']; ?> </td>
				  <td><?php echo $row['contact_tel_number']; ?> </td>
				  <td><?php echo $row['contact_mobile_number']; ?> </td>
			   
				<tr>
				<?php
			} while ( $row = mysql_fetch_assoc ( $query ) );
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