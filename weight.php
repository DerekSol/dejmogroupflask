<?php
// Connect to the database
$servername = "localhost";
$username = "username";
$password = "password";
$dbname = "myDB";

$conn = mysqli_connect($servername, $username, $password, $dbname);

// Check connection
if (!$conn) {
    die("Connection failed: " . mysqli_connect_error());
}

// Process the form data
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $name = $_POST["name"];
    $weight = $_POST["weight"];
    $date = $_POST["date"];

    // Insert the data into the table
    $sql = "INSERT INTO weight_data (name, weight, date)
            VALUES ('$name', '$weight', '$date')";

    if (mysqli_query($conn, $sql)) {
        echo "Data saved successfully";
    } else {
        echo "Error: " . $sql . "<br>" . mysqli_error($conn);
    }
}

// Close the database connection
mysqli_close($conn);
?>
