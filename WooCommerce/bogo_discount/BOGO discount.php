<?php
/**
 * Plugin Name: BOGO Coupon
 * Description: Applies different discount amounts based on cart total and currency using the same logic for multiple coupon codes.
 * Version: 1.2
 * Author: Abdalrhman Yaser
 */

// Define the coupon codes that should trigger the custom logic
function get_custom_coupon_codes1() {
    return ['test1']; // Add more codes here
}
add_filter('woocommerce_before_calculate_totals', function () {
    global $timesForBogo;
    $timesForBogo = 0;
});

add_action('woocommerce_coupon_get_discount_amount', 'apply_bogo_discount_for_lenses', 10, 5);
function apply_bogo_discount_for_lenses($discount, $discounting_amount, $cart_item, $single, $coupon) {
    if (is_admin() && !defined('DOING_AJAX')) return;

    $cart = WC()->cart;
    $eligible_items = [];
    $custom_codes = ['test1'];
    $applied_coupons = $cart->get_applied_coupons();
    $matched_coupon = null;
    foreach ($applied_coupons as $code) {
        if (in_array(strtoupper($code), array_map('strtoupper', $custom_codes))) {
            $matched_coupon = $code;
            break;
        }
    }
    global $timesForBogo;
    $timesForBogo++;
    if (!$matched_coupon) return $discount;
    
    // Collect eligible cart items
    foreach ($cart->get_cart() as $cart_item_key => $cart_item) {
        $product = $cart_item['data'];
        $price = $product->get_price();
        $quantity = $cart_item['quantity'];

        for ($i = 0; $i < $quantity; $i++) {
            $eligible_items[] = [
                'price' => $price,
                'cart_item_key' => $cart_item_key,
            ];
        }
    }

    // Sort items by price (ascending)
    usort($eligible_items, function($a, $b) {
        return $a['price'] <=> $b['price'];
    });
    
    // Every second item is free
    $discount = 0;
    for ($i = 0; $i < floor(count($eligible_items) / 2); $i++) {
        $discount += $eligible_items[$i]['price'];
    }
    
    $itemCount = 0;
    foreach (WC()->cart->get_cart() as $cart_item) {
        $itemCount++;
    }

    
    if (  $discount > 0 && $timesForBogo == 1) {
        return $discount;
    } elseif ($timesForBogo == 1){
        remove_code1();
        throw new Exception( __( 'Sorry, this coupon requires two or more products.', 'woocommerce' ), 109 );
    }
}

// Validate coupon conditions based on cart total and currency
add_filter('woocommerce_coupon_is_valid', 'custom_coupon_check_conditions_and_throw_error1', 10, 2);
function custom_coupon_check_conditions_and_throw_error1($valid, $coupon) {
    $custom_codes = get_custom_coupon_codes1();
    
    if (!in_array(strtoupper($coupon->get_code()), array_map('strtoupper', $custom_codes))) {
        return $valid;
    }
    $cart = WC()->cart;
    $eligible_items = [];
    // Collect eligible cart items
    foreach ($cart->get_cart() as $cart_item_key => $cart_item) {
        $product = $cart_item['data'];
        $price = $product->get_price();
        $quantity = $cart_item['quantity'];

        for ($i = 0; $i < $quantity; $i++) {
            $eligible_items[] = [
                'price' => $price,
                'cart_item_key' => $cart_item_key,
            ];
        }
    }
    if (count($eligible_items) >= 2) {
        return true;
    }
    else{
        throw new Exception( __( 'Sorry, this coupon requires two or more products.', 'woocommerce' ), 109 );
    }
}

function remove_code1(){
    $cart = WC()->cart;
	foreach ($cart->get_coupons() as $code => $coupon) {
        $cart->remove_coupon($code);
    }
}

