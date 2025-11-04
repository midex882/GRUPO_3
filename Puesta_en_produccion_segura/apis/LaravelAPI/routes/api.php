Route::get('items', 'ItemController@index');       // List all items
Route::get('items/{id}', 'ItemController@show');   // Show specific item by id
Route::post('items', 'ItemController@store');      // Create new item
Route::put('items/{id}', 'ItemController@update'); // Update item by id
Route::delete('items/{id}', 'ItemController@destroy'); // Delete item by id
