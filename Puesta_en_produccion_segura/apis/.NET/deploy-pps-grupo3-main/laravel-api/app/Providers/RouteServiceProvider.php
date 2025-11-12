<?php

namespace App\Providers;

use Illuminate\Support\Facades\Route;
use Illuminate\Foundation\Support\Providers\RouteServiceProvider as ServiceProvider;

class RouteServiceProvider extends ServiceProvider
{
    /**
     * Register routes for the application.
     */
    public function boot(): void
    {
        $this->routes(function () {
            // Carga rutas API con prefijo /api
            Route::prefix('api')
                ->middleware('api')
                ->group(base_path('routes/api.php'));

            // Carga rutas web normales
            Route::middleware('web')
                ->group(base_path('routes/web.php'));
        });
    }
}
