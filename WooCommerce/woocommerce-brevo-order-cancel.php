<?php
/**
 * Plugin Name: WooCommerce Brevo Order Cancel
 * Description: Sends an API call to Brevo when an order is cancelled.
 * Version: 1.0
 */

if (!defined('ABSPATH')) exit;

require_once plugin_dir_path(__FILE__) . 'brevo-autoload.php';

use Brevo\Client\Configuration;
use Brevo\Client\Api\TransactionalEmailsApi;
use GuzzleHttp\Client;

add_action('woocommerce_order_status_cancelled', function ($order_id) {
    $order = wc_get_order($order_id);
    if (!$order) return;

    $config = Configuration::getDefaultConfiguration()->setApiKey('api-key', 'your-brevo-api-key');
    $apiInstance = new TransactionalEmailsApi(new Client(), $config);

    $email = [
        'sender' => ['name' => 'My Store', 'email' => 'noreply@example.com'],
        'to' => [['email' => $order->get_billing_email(), 'name' => $order->get_billing_first_name()]],
        'subject' => 'Your Order Has Been Cancelled',
        'htmlContent' => '<p>Hello, your order #' . $order_id . ' has been cancelled.</p>',
    ];

    try {
        $apiInstance->sendTransacEmail($email);
    } catch (Exception $e) {
        error_log('Brevo API Error: ' . $e->getMessage());
    }
});
