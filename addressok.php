<?php

function AddressOK_GetData($req) {
    $addressok_url = 'http://addressok:14000/';

    $req = http_build_query($req);

    $ch = curl_init();
    curl_setopt($ch, CURLOPT_URL, $addressok_url);
    curl_setopt($ch, CURLOPT_POST, true);
    curl_setopt($ch, CURLOPT_HEADER, false);
    curl_setopt($ch, CURLOPT_NOBODY, false);
    curl_setopt($ch, CURLOPT_POSTFIELDS, $req);
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
    curl_setopt($ch, CURLOPT_PROTOCOLS, CURLPROTO_HTTP);

    $data = curl_exec($ch); 
    $httpCode = curl_getinfo($ch, CURLINFO_HTTP_CODE); 
    $err     = curl_errno( $ch );
    $errmsg  = curl_error( $ch );
    curl_close($ch);

    return $data;
}

?>