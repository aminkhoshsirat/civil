<?php
// Turn on error reporting for development (should be off in production)
error_reporting(E_ALL);
ini_set('display_errors', 1);

// Security functions
function sanitize_input($data) {
    // Prevent XSS by cleaning input
    return htmlspecialchars(trim($data), ENT_QUOTES, 'UTF-8');
}

function validate_email($email) {
    // Validate email format
    return filter_var($email, FILTER_VALIDATE_EMAIL);
}

// Check if the request is POST
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    // Check if email is set in the request
    if (isset($_POST['email-form'])) {
        $email = sanitize_input($_POST['email-form']);
        
        // Validate email
        if (!validate_email($email)) {
            echo json_encode(['status' => 'error', 'message' => 'The email address provided is not valid.']);
            exit;
        }

        // CSRF protection check
        if (!isset($_SESSION['csrf_token']) || $_POST['csrf_token'] !== $_SESSION['csrf_token']) {
            echo json_encode(['status' => 'error', 'message' => 'There was an issue with your request.']);
            exit;
        }

        // Database connection and saving email (adjust this according to your database)
        try {
            // Assuming database connection is established
            $pdo = new PDO('mysql:host=localhost;dbname=your_database', 'username', 'password');
            $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

            // Check if the email already exists
            $stmt = $pdo->prepare("SELECT id FROM subscribers WHERE email = :email");
            $stmt->execute(['email' => $email]);
            if ($stmt->rowCount() > 0) {
                echo json_encode(['status' => 'error', 'message' => 'This email is already subscribed.']);
                exit;
            }

            // Insert email into database
            $stmt = $pdo->prepare("INSERT INTO subscribers (email) VALUES (:email)");
            $stmt->execute(['email' => $email]);

            // Return success response
            echo json_encode(['status' => 'success', 'message' => 'Your email has been successfully subscribed.']);
        } catch (PDOException $e) {
            // If database connection fails
            echo json_encode(['status' => 'error', 'message' => 'A server error occurred. Please try again later.']);
        }
    } else {
        echo json_encode(['status' => 'error', 'message' => 'Please provide a valid email address.']);
    }
} else {
    echo json_encode(['status' => 'error', 'message' => 'Invalid request.']);
}
?>
