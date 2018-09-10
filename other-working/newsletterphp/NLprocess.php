<?php

// Hello! welcome to the settings page.
// Here's your two steps guide:

// FIRST: 
// Instead of newsletter@test.com put the email address of the mailing list,
// (the same that SendBlaster uses in Manage Subscriptions Section)
// ... please pay attention to the  ' ' apostrophes, they must remain around the email address.

$emailmanager = 'info@test.com';

// SECOND:
// save this file, and close it. Thank you!


error_reporting(0);

$email = trim($_POST['email']);
$Ok = ereg("^([a-zA-Z0-9_\.-]+)@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.)|(([a-zA-Z0-9\-]+\.)+))([a-zA-Z]{2,4}|[0-9]{1,3})(\]?)$", $email);
if ($Ok) {
	mail($emailmanager,'Subscribe','','From: '.$email);

	if(!ereg("^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,3})$",$UNameFrm))
	{
	?>
<script language = 'javascript'>
	alert('Thank you, your address was added to our Mailing List');
	history.go(-1);
	</script>
<?
	exit();
	}
} 

else {
	if(!ereg("^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,3})$",$UNameFrm))
	{
	?>
<script language = 'javascript'>
	alert('Sorry, please provide a valid Email address.');
	history.go(-1);
	</script>
<?
	exit();
	}
}
?>

#########################################################################################################################
#########################################################################################################################
#########################################################################################################################
#########################################################################################################################
#


//mycode
//  https://www.tutorialspoint.com/php/connect_to_mysql_using_php.htm




##
##  Create DB
##   --db code-- set un-pw- db names ect
##


## todo add   a join_date  update script   check example on tuts point


<?php
   
   $dbhost = 'localhost:3036';
   $dbuser = 'root';
   $dbpass = 'rootpassword';
   $conn = mysql_connect($dbhost, $dbuser, $dbpass);
   
   if(! $conn ) {
      die('Could not connect: ' . mysql_error());
   }
   
   echo 'Connected successfully';
   
   $sql = 'CREATE TABLE subscribers( '.
      'sub_id INT NOT NULL AUTO_INCREMENT, '.
      'sub_email VARCHAR(20) NOT NULL, '.
      'sub_name  VARCHAR(20) NOT NULL, '.
      'join_date  VARCHAR(20) NOT NULL, '.
      'primary key ( emp_id ))';
   mysql_select_db('test_db');
   $retval = mysql_query( $sql, $conn );
   
   if(! $retval ) {
      die('Could not create table: ' . mysql_error());
   }
   
   echo "Table employee created successfully\n";
   
   mysql_close($conn);
?>



##  
##  Todo  DB
##   --insert data from form into database
##
##   https://www.tutorialspoint.com/php/mysql_insert_php.htm
##


INSERT INTO `subscribers`( `sub_email`, `sub_name`, `join_date`) 
VALUES ([value-2],[value-3],[value-4])

 <?php
         if(isset($_POST['add'])) {
            $dbhost = 'localhost:3036';
            $dbuser = 'root';
            $dbpass = 'rootpassword';
            $conn = mysql_connect($dbhost, $dbuser, $dbpass);
            
            if(! $conn ) {
               die('Could not connect: ' . mysql_error());
            }
            
            if(! get_magic_quotes_gpc() ) {
               $emp_name = addslashes ($_POST['sub_email']);
               $emp_address = addslashes ($_POST['sub_name']);
            }else {
               $emp_name = $_POST['sub_email'];
               $emp_address = $_POST['sub_name'];
            }
            
            $emp_salary = $_POST['sub_email'];
            
            $sql = "INSERT INTO subscribers ". "(sub_email,sub_name, 
               join_date) ". "VALUES('$sub_email','$sub_name', NOW())";
               
            mysql_select_db('subscribers_db');
            $retval = mysql_query( $sql, $conn );
            
            if(! $retval ) {
               die('Could not enter data: ' . mysql_error());
            }
            
            echo "Entered data successfully\n";
            
            mysql_close($conn);
         }else {
            ?>
            










#########################################################################################################################
#########################################################################################################################
#########################################################################################################################
#########################################################################################################################
# ex. 01
# https://www.tutorialspoint.com/php/mysql_insert_php.htm
<?php
   $dbhost = 'localhost:3036';
   $dbuser = 'root';
   $dbpass = 'rootpassword';
   $conn = mysql_connect($dbhost, $dbuser, $dbpass);
   
   if(! $conn ) {
      die('Could not connect: ' . mysql_error());
   }
   
   $sql = 'INSERT INTO employee '.
      '(emp_name,emp_address, emp_salary, join_date) '.
      'VALUES ( "guest", "XYZ", 2000, NOW() )';
      
   mysql_select_db('test_db');
   $retval = mysql_query( $sql, $conn );
   
   if(! $retval ) {
      die('Could not enter data: ' . mysql_error());
   }
   
   echo "Entered data successfully\n";
   
   mysql_close($conn);
?>



# ex. 02
# https://www.tutorialspoint.com/php/mysql_insert_php.htm<html>
   
   <head>
      <title>Add New Record in MySQL Database</title>
   </head>
   
   <body>
      <?php
         if(isset($_POST['add'])) {
            $dbhost = 'localhost:3036';
            $dbuser = 'root';
            $dbpass = 'rootpassword';
            $conn = mysql_connect($dbhost, $dbuser, $dbpass);
            
            if(! $conn ) {
               die('Could not connect: ' . mysql_error());
            }
            
            if(! get_magic_quotes_gpc() ) {
               $emp_name = addslashes ($_POST['emp_name']);
               $emp_address = addslashes ($_POST['emp_address']);
            }else {
               $emp_name = $_POST['emp_name'];
               $emp_address = $_POST['emp_address'];
            }
            
            $emp_salary = $_POST['emp_salary'];
            
            $sql = "INSERT INTO employee ". "(emp_name,emp_address, emp_salary, 
               join_date) ". "VALUES('$emp_name','$emp_address',$emp_salary, NOW())";
               
            mysql_select_db('test_db');
            $retval = mysql_query( $sql, $conn );
            
            if(! $retval ) {
               die('Could not enter data: ' . mysql_error());
            }
            
            echo "Entered data successfully\n";
            
            mysql_close($conn);
         }else {
            ?>
            
               <form method = "post" action = "<?php $_PHP_SELF ?>">
                  <table width = "400" border = "0" cellspacing = "1" 
                     cellpadding = "2">
                  
                     <tr>
                        <td width = "100">Employee Name</td>
                        <td><input name = "emp_name" type = "text" 
                           id = "emp_name"></td>
                     </tr>
                  
                     <tr>
                        <td width = "100">Employee Address</td>
                        <td><input name = "emp_address" type = "text" 
                           id = "emp_address"></td>
                     </tr>
                  
                     <tr>
                        <td width = "100">Employee Salary</td>
                        <td><input name = "emp_salary" type = "text" 
                           id = "emp_salary"></td>
                     </tr>
                  
                     <tr>
                        <td width = "100"> </td>
                        <td> </td>
                     </tr>
                  
                     <tr>
                        <td width = "100"> </td>
                        <td>
                           <input name = "add" type = "submit" id = "add" 
                              value = "Add Employee">
                        </td>
                     </tr>
                  
                  </table>
               </form>
            
            <?php
         }
      ?>
   
   </body>
</html>






