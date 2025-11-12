<?php

    use Illuminate\Support\Facades\Route;
    use App\Http\Controllers\ItemController;


    Route::apiResource('items', ItemController::class);

    /**
     * apiResource methos over Route Facade create next routes:
     *
     * Route::get('/items', [ItemController::class, 'index']);
     * Route::get('/items/{id}', [ItemController::class, 'show']);
     * Route::post('/items', [ItemController::class, 'store']);
     * Route::put('/items/{id}', [ItemController::class, 'update']);
     * Route::delete('/items/{id}', [ItemController::class, 'destroy']);
     */
