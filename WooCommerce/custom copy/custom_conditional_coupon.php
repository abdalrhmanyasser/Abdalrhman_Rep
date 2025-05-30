<?php
/**
 * Plugin Name: Custom Conditional Coupon
 * Description: Applies different discount amounts based on cart total and currency using the same logic for multiple coupon codes.
 * Version: 1.7
 * Author: Abdalrhman Yaser
 */

// Define the coupon codes that should trigger the custom logic
function get_custom_coupon_codes1() {
    return ['Reem10']; // Add more codes here
}
function get_custom_coupon_codes() {
    return ['FAY8', 'SAF8', 'MUS10', 'Sla10', 'ht10', 'Hamda10', 'Ahlam10', 'She10', 'Asma10', 'Gamila10']; // Add more codes here
}

function get_cart_subtotal_excluding_eye_care() {
    $parent_category_slug = 'eye-care-product'; // Replace with actual slug
    $custom_subtotal = 0;

    // Get the term object for the parent category
    $parent_term = get_term_by('slug', $parent_category_slug, 'product_cat');

    if (!$parent_term || is_wp_error($parent_term)) {
        return WC()->cart->get_subtotal(); // Fallback to full subtotal
    }

    // Get all child category IDs including parent
    $excluded_term_ids = get_term_children($parent_term->term_id, 'product_cat');
    $excluded_term_ids[] = $parent_term->term_id;

    foreach (WC()->cart->get_cart() as $cart_item) {
        $product = $cart_item['data'];
        $product_id = $product->get_id();
        $quantity = $cart_item['quantity'];

        // Get the term IDs the product belongs to
        $product_term_ids = wp_get_post_terms($product_id, 'product_cat', ['fields' => 'ids']);

        // Skip product if it belongs to any excluded category
        if (array_intersect($product_term_ids, $excluded_term_ids)) {
            continue;
        }

        // Add to subtotal
        $custom_subtotal += $product->get_price() * $quantity;
    }

    return $custom_subtotal;
}


// Validate coupon conditions based on cart total and currency
add_filter('woocommerce_coupon_is_valid_for_cart', 'custom_coupon_check_conditions_and_throw_error', 10, 2);
function custom_coupon_check_conditions_and_throw_error($valid, $coupon) {
    $custom_codes = get_custom_coupon_codes();
    $custom_codes1 = get_custom_coupon_codes1();
    $currency = get_woocommerce_currency();
    $cart_total = get_cart_subtotal_excluding_eye_care();
    if (!in_array(strtoupper($coupon->get_code()), array_map('strtoupper', $custom_codes1))) {
        return $valid;
    }else if (!in_array(strtoupper($coupon->get_code()), array_map('strtoupper', $custom_codes))) {
        return $valid;
    }
    if (in_array(strtoupper($coupon->get_code()), array_map('strtoupper', $custom_codes1))) {
        // Check conditions based on currency
        if ($currency === 'AED'  && $cart_total < 200) {
            wc_add_notice(__('This coupon requires a minimum subtotal of 200 AED'), 'error');
            remove_code();
            return false;
        } elseif ($currency === 'SAR' && $cart_total < 200) {
            wc_add_notice(__('This coupon requires a minimum subtotal of 200 SAR'), 'error');
            remove_code();
            return false;
        } elseif ($currency === 'KWD' && $cart_total < 17) {
            wc_add_notice(__('This coupon requires a minimum subtotal of 17 KWD.'), 'error');
            remove_code();
            return false;
        } elseif ($currency === 'USD' && $cart_total < 55) {
            wc_add_notice(__('This coupon requires a minimum subtotal of 55 USD.'), 'error');
            remove_code();
            return false;
        } elseif ($currency === 'BHD' && $cart_total < 20.5) {
            wc_add_notice(__('This coupon requires a minimum subtotal of 20.5 BHD.'), 'error');
            remove_code();
            return false;
        } elseif ($currency === 'OMR' && $cart_total < 21) {
            wc_add_notice(__('This coupon requires a minimum subtotal of 21 OMR.'), 'error');
            remove_code();
            return false;
        } elseif ($currency === 'QAR' && $cart_total < 200) {
            wc_add_notice(__('This coupon requires a minimum subtotal of 200 QAR.'), 'error');
            remove_code();
            return false;
        } elseif (!in_array($currency, ['AED', 'SAR', 'KWD', 'USD', 'BHD', 'OMR', 'QAR'])) {
            wc_add_notice(__('This coupon is not valid for your store currency.'), 'error');
            remove_code();
            return false;
        }
        return true;
    }elseif (!in_array(strtoupper($coupon->get_code()), array_map('strtoupper', $custom_codes))){
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
}

add_filter('woocommerce_coupon_get_discount_amount', 'custom_coupon_apply_dynamic_discount', 10, 5);
function custom_coupon_apply_dynamic_discount($discount, $discounting_amount, $cart_item, $single, $coupon) {
    if (is_admin() && !defined('DOING_AJAX')) return;

    $cart = WC()->cart;
    $currency = get_woocommerce_currency();
    $custom_codes = get_custom_coupon_codes();
    $custom_codes = get_custom_coupon_codes1();
    $applied_coupons = $cart->get_applied_coupons();

    $matched_coupon = null;

    foreach ($applied_coupons as $code) {
        if (in_array(strtoupper($code), array_map('strtoupper', $custom_codes))) {
            $matched_coupon = $code;
            break;
        }
    }

    if (!$matched_coupon) return $discount;
    if (!in_array(strtoupper($coupon->get_code()), array_map('strtoupper', $custom_codes1))) {

        $cart_total = get_cart_subtotal_excluding_eye_care();
        $discount = 0;

        if ($currency === 'AED') {
            if ($cart_total > 300) {
                $discount = 100;
            } elseif ($cart_total >= 200) {
                $discount = 50;
            }
        } elseif ($currency === 'SAR') {
            if ($cart_total > 310) {
                $discount = 100;
            } elseif ($cart_total >= 200) {
                $discount = 50;
            }
        } elseif ($currency === 'KWD') {
            if ($cart_total > 25) {
                $discount = 8;
            } elseif ($cart_total >= 17) {
                $discount = 4;
            }
        } elseif ($currency === 'USD') {
            if ($cart_total > 82) {
                $discount = 27;
            } elseif ($cart_total >= 55) {
                $discount = 13;
            }
        } elseif ($currency === 'OMR') {
            if ($cart_total > 32) {
                $discount = 10.5;
            } elseif ($cart_total >= 21) {
                $discount = 5;
            }
        } elseif ($currency === 'BHD') {
            if ($cart_total > 31) {
                $discount = 10;
            } elseif ($cart_total >= 20.5) {
                $discount = 5;
            }
        } elseif ($currency === 'QAR') {
            if ($cart_total > 300) {
                $discount = 100;
            } elseif ($cart_total >= 200) {
                $discount = 50;
            }
        }
        $itemCount = 0;
        foreach (WC()->cart->get_cart() as $cart_item) {
            $itemCount++;
        }

        if ($discount > 0) {
            return $discount / $itemCount;
        } else {
            // If threshold isn't met, remove WooCommerce's default discount (just in case)
            remove_code();
            return 0;
        }
    }else{
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

        
        if (  $discount > 0 & $cart_item['']) {
            return $discount;
        } elseif ($timesForBogo == 1){
            remove_code1();
            throw new Exception( __( 'Sorry, this coupon requires two or more products.', 'woocommerce' ), 109 );
        }
    }
}

function remove_code(){

    $cart = WC()->cart;
    $custom_codes = get_custom_coupon_codes();
	foreach ($cart->get_coupons() as $code => $coupon) {
            if (in_array(strtoupper($code), array_map('strtoupper', $custom_codes)))
            {
                $cart->remove_coupon($code);
            }
        }
}