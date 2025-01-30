<?php
// Mailchimp API setup
$api_key = 'your_mailchimp_api_key'; // Replace with your Mailchimp API key
$list_id = 'your_mailchimp_list_id'; // Replace with your Mailchimp Audience ID

// Mailchimp API endpoint URL
$endpoint = 'https://<dc>.api.mailchimp.com/3.0/lists/' . $list_id . '/members/';

// Data from the subscription form
$email = isset($_POST['email-form']) ? $_POST['email-form'] : null;

if ($email) {
    // Prepare email for Mailchimp
    $data = [
        'email_address' => $email,
        'status' => 'subscribed', // This subscribes the user immediately
    ];

    // Setup cURL request to Mailchimp API
    $ch = curl_init();
    curl_setopt($ch, CURLOPT_URL, $endpoint);
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
    curl_setopt($ch, CURLOPT_CUSTOMREQUEST, "POST");
    curl_setopt($ch, CURLOPT_POSTFIELDS, json_encode($data));
    curl_setopt($ch, CURLOPT_HTTPHEADER, [
        'Authorization: Basic ' . base64_encode('anystring:' . $api_key),
        'Content-Type: application/json',
    ]);

    // Execute cURL request and get response
    $response = curl_exec($ch);
    $http_code = curl_getinfo($ch, CURLINFO_HTTP_CODE);
    curl_close($ch);

    // Check for successful response
    if ($http_code === 200) {
        echo json_encode(['status' => 'success', 'message' => 'You have been successfully subscribed to our Mailchimp list.']);
    } else {
        echo json_encode(['status' => 'error', 'message' => 'There was an error subscribing to the Mailchimp list.']);
    }
} else {
    echo json_encode(['status' => 'error', 'message' => 'Please provide a valid email address.']);
}
?>
