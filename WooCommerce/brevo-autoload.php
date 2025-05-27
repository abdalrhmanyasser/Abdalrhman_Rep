<?php
// brevo-autoload.php
if (!class_exists(\Brevo\Client\Api\TransactionalEmailsApi::class)) {
    require_once __DIR__ . '/vendor/autoload.php';
}
