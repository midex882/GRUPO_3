<?php
Route::middleware(['simple.auth'])->group(function () {
    Route::get('','NameController@saludo');
    Route::get('names', 'NameController@index');       // List all names
    Route::get('names/{id}', 'NameController@show');   // Show specific Name by id
    Route::post('names', 'NameController@store');      // Create new Name
    Route::put('names/{id}', 'NameController@update'); // Update Name by id
    Route::delete('names/{id}', 'NameController@destroy'); // Delete Name by id
});



?>
